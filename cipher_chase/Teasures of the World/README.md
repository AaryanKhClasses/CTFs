# Teasures of the World
`cipher_chase`, `misc`

## Problem Statement
My grandfather used to tell me stories about some teasure, which was left by my great grandfather. He left some clues to us, through a friend, but we never got to see the teasure, nor were we close to deciphering the clues.

I'm sure you've heard of the teasure, and I'm sure you've seen the clues. Well, I think it might be under this gas station. Can you find the teasure?

Flag Format: `ZenseCTF{lat,long}` (Truncate down to the first 3 digits of the latitude and longitude (no rounding).) For example: `ZenseCTF{1.452,-12.789}`

**Attachment:** [original.png](./original.png)

## My Solution
1. From the image, we can notice some words written as "Lynchburg Salem" and also a gas station.
2. The location is [11244 W Lynchburg Salem Turnpike](https://www.google.com/maps/@37.3825979,-79.727369,3a,87.6y,234.51h,70.31t/data=!3m7!1e1!3m5!1sShzyo__6ZN-XzlCqR8N9HA!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D19.692389106422112%26panoid%3DShzyo__6ZN-XzlCqR8N9HA%26yaw%3D234.50705432265158!7i16384!8i8192)
3. The coordinates of the location are approximately `37.3825979, -79.727369`.

### Flag
```
ZenseCTF{37.382,-79.727}
```
