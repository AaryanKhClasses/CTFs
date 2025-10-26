# Dig Deeper
`cybertea`, `osint`

## Problem Statement
A collector recently uploaded a photographed tool from a private lot. The image itself may point back to its origin. Trace the story to its source. Identify the three route names associated with that site and combine them (in the historical order) with the exact price in which the item in the image was sold.

## My Solution
1. Download the `spoon_me.png` [image](spoon_me.png)
2. On running `exiftool`, we get a location: `51.6007476, 15.3089388`.
3. On going to Google Maps, we see a location in `The Great Escape Memorial, Poland`.
4. It is located near `Stalag Luft III`, `Wielka Ucieczka`, `Tunnel Harry`.
5. The three route/tunnel names associated the site are Tom, Dick, and Harry (historical order: Tom -> Dick -> Harry).
6. The item in the image appears to be the aluminum combined spoon/fork relic from Stalag Luft III; a recorded sale of that exact item shows it sold for $450.
7. Combining all these three, we get our flag.

### Flag
```
CTEA_CTF{tom_dick_harry_450}
```
