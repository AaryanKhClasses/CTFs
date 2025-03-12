# Space Wars
From SeaTF @ NITK, 2025.

## Problem Statement:
You have intercepted the communication between two enemy spaceships. The enemies are known to hide credentials in riddles. Get their attack strategy Commander🫡

Intercepted text: Where no man has gone before, A Vulcan stands with logic pure. His raised hand, a sign so clever, Bids you to live long and ___.

His name is known through time and space, A Starfleet mind, calm and ace. Think of the one with pointed ears, The answer lies as truth appears. 🚀

https://ctf-other.onrender.com/

## My Approach / Solution:
1. On Googling the intercepted text, we found that the line is from the franchise "Star Trek".
2. The name of the Vulcan is Spock.
3. The answer to the riddle is `Prosper`.
4. On opening the website, and putting the username `Spock` and password `Prosper`, we get redirected to a page containing an image.
5. While opening the "Network" tab in the developer tools, we see that the image has a cookie attached to it.
6. It says "seatf-jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiQ2FwdGFpbiBLaXJrIiwicGFzc3dvcmQiOiJJbnJoJWgzbmJQK2siLCJpYXQiOjE3NDE3MDk3MzN9.JqyStQC8CAoh9SUfKilCVC34ddBmWIVf51HakGschwc".
7. On decoding the JWT token, we get the username `Captain Kirk` and password `Ihr*h3nbP+k*`.
8. Again going to the same login page and entering these credentials, we get our flag.

## Flag:
```
SeaTF{s14r_w4r5}
```