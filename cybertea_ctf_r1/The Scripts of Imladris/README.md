# The Scripts of Imladris
`cybertea`, `reverse_engineering`

## Problem Statement
Hope...... you've revised all your Lord of the Rings homework and have a good base for it ;)

An ancient Elven console has been unearthed. Can you answer its riddles?

## My Solution
1. Download and open the `riddles.bin` [file](riddles.bin).
2. Open a windows command prompt and run the file.
3. The first riddle is:
```
I am the Hobbit who was tasked with destroying the One Ring. What is my first name?
```
to which the answer is `Frodo`. Converting it into a hex format gives us `46726f646f`, which is the solution for the first riddle.
4. The second riddle is:
```
I am the food of the Elves, a single bite of which can sustain a man for a day. What am I?
```
to which the answer is `Lembas`. Converting it into a hex format gives us `4c656d626173`, which is the solution for the second riddle.
5. The third riddle is:
```
I was the sword of Elendil that was broken, and later reforged for the heir of Gondor. What is my new name?
```
to which the answer is `Andúril`. Converting it into a hex format gives us `416e647572696c`, which is the solution for the third riddle.
6. The last riddle is:
```
What is the Elvish word for 'friend'?
```
to which the answer is `Mellon`. Converting it into a hex format gives us `4d656c6c6f6e`, which is the solution for the last riddle.
7. On submitting all the correct answers, we get the final flag.

### Flag
```
CTEA_CTF{sp34k_fr13nd_4nd_3nt3r}
```
