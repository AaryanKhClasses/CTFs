# Catch me if you can
`shaastra_ctf`, `web`

## Problem Statement:

## My Solution:
1. On opening the website, I looked into the `styles.css` file and found part of the flag (`Shaastra{buTt0n_ev@d3d`).
2. Looking more into the `script.js` file, it calls a fetch request to a route `/secret-message`.
3. I just did `curl https://click-web.shaastractf.kctf.cloud/secret-message` to get the rest of the flag (`_F_l@g_r3trI3v3d_123}`).
4. Combining both parts, I got the complete flag.

### Flag:
```
Shaastra{buTt0n_ev@d3d_F_l@g_r3trI3v3d_123}
```
