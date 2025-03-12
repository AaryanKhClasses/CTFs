# Honest Mistake 🫠
From SeaTF @ NITK, 2025.

## Problem Statement:
One of organizers was a bit clumsy and revealed the questions to the public. However, they were smart enough to delete the solutions before leaking. But, hope you are smarter than them.

## My Approach / Solution:
1. Extracting the zip file contains 2 photos and a .git folder.
2. The images are of no use for this problem, all the importance is the .git folder.
3. Looking into the `./logs` folder, we see a `HEAD` file with all the commit history.
4. The `./logs/refs/heads` folder contains a `master` file with only one commit log.
5. Also the `./refs/heads` folder contains a `master` file with the latest commit hash.
6. Adding one commit from the "HEAD" file to the "master" file and and replacing the hash in the "master" file with the new hash, we run the `git log` command each time.
7. One time we see a `readme.txt` file being deleted, we restore the file using `git restore` and check its file contents.
8. The file had contents saying:
```txt
The participants have to decompile the image given to get a string.
Then they need to only take the characters in the odd places which gives them the encoded flag.
After decoding they will get SeaTF{goddamn_idiotic_truckload_of_sh*t} which
is a nod to the first commit of git by Linus Torvolds (http://github.com/git/git/commit/e83c5163316f89bfbde7d9ab23ca2e25604af290)
```

## Flag:
```
SeaTF{goddamn_idiotic_truckload_of_sh*t}
```