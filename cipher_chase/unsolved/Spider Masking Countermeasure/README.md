# Spider Masking Countermeasure
`cipher_chase`, `cryptography`

## Problem Statement
Bucket Head Nova and White tiger have secrets a and b each divided into 3 independent shares. They want to deliver a message to Iron fist without letting Spider man know. So they use ISW masking. They share c = a.b = c1 + c2 + c3 with Iron fist publically. Spider man gathers intel that only one value of randomness was used in masking the shares and finds a3 and b3.

Flag Format: `ZenseCTF{MD5(a)_MD5(b)_MD5(c3)}`

**Hint 1:** a,b, c3 are supposed to be reperesented in base 10 format, while calculating md5 hash.

**Hint 2:** Spider man also obtained a cipher_hex which was the XOR'd value of a message with the key as MD5(a)_MD5(b)_MD5(c3). cipher_hex=400c4d16565e165e0646115e521558061c080b5f5b5f0b045c0b05040e0a590d6259045b040d0a5e5b0f580a0c595e0b58050f0d0c0b0b0b0505045c58085e085b62085e580d0e5f590b595b04595c0b5b5e0f0c0c595e045b090d0d090b5b0f0b0c

The message will make it obvious that you got the answer!

**Attachment:** [message.txt](./message.txt)
