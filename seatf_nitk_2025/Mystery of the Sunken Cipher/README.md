# Mystery of the Sunken Cipher
From SeaTF @ NITK, 2025.

## Problem Statement:
Beneath the turquoise waves, a coral formation holds a riddle whispered by the currents. Those who seek the hidden path must first decipher its meaning to navigate the depths. But the ocean is layered with secrets. A closer inspection of the waters reveals something unseen—a hidden message carried by the tides of code. With the right adjustments, a vision appears, but not all that is seen can be understood at first glance. The ocean has a way of concealing messages within its shifting sands—some hide in the very colors of the sea, waiting for a sharp-eyed explorer to uncover them. Once found, the message remains entangled in an ancient dialect, one spoken in shifting patterns and elusive keys. Even deeper, an old mariner’s scroll awaits, its words guarded by twin sentinels of time—one known for shifting letters along the currents and another for folding messages into layers of oceanic echoes. Only those who can ride the right waves will piece together the final coordinates and claim the buried treasure.

Flag Format : CTF{flag}

DIG DEEPER : https://marvelous-heliotrope-29e086.netlify.app/

## My Approach / Solution:
> [!WARNING]
> This might not be the intended solution.

1. The given link redirects to a webpage related to ocean stuff.
2. The webpage has a link to a `/coral-reefs` route, which contained the text `"I am a box that holds clues, but you can never see the boundaries unless you look closely. I can change my appearance depending on my surroundings, yet I remain in my place. What am I?"`.
3. On searching the riddle on Google, a GitHub repository of the source code is found: https://github.com/ChetasiTrivedi/ctf_11
4. On looking to all the repositories of the person, a repository named "server" is found containing the server side code for the website.
5. The source code of the file https://github.com/ChetasiTrivedi/server/blob/main/server.js contains the flag in plain sight.

## Flag:
```
CTF{SURFER_YOU_CRACKED_IT}
```