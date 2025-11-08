(load "~/quicklisp/setup.lisp")
(ql:quickload :ironclad) ;

(defun bytes-to-long (byte-list)
  (reduce (lambda (acc b)
            (+ (* acc 256) b))
          byte-list
          :initial-value 0))

(defun long-to-bytes (n)
  (if (= n 0)
      '(0)
      (loop for x = n then (floor x 256)
            until (= x 0)
            collect (mod x 256))))

(defun get-prime (bits)
  (ironclad:generate-prime bits))

(defun make-m-fibo (m p)
  (let ((prev1 1)
        (prev2 1))
    (lambda ()
      (let* ((current (mod (+ prev1 (* m prev2)) p)))
        (setf prev1 prev2
              prev2 current)
        current))))

(let* ((flag (map 'list #'char-code "ZenseCTF{REDACTED}"))
       (m (bytes-to-long flag))
       (p (get-prime 512))
       (gen (make-m-fibo m p))
       c1 c2)

  (dotimes (i 13337)
    (let ((c (funcall gen)))
      (when (= i 1336)
        (setf c1 c))
      (setf c2 c)))

  (format t "c1 = ~A~%" c1)
  (format t "c2 = ~A~%" c2)
  (format t "p = ~A~%" p))

; c1 = 6446851029422343790041538443588498063115396922013781397631760130647832489284030354202901634599886089658317286559350434250772930156030729785534908554635476
; c2 = 9535982832076967937315493358913335391088892393140170858514806032313203254365227087143977832164904826738133186604941005082705231921350602917930804473351985
; p = 10185593478466450851109934291686755301942013572885247941258794367774242709887918496124483532431829003890414414011183636822073244713076488023802678563372201
