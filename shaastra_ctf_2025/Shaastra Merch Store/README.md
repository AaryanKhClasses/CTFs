# Shaastra Merch Store
`shaastra`, `web`

## Problem Statement:
I heard that the Shaastra hoodie is really good. but its costly. Help me buy one. Access the Shaastra Merch Store [here](https://shaastra-merch-web.shaastractf.kctf.cloud/).

## My Solution:
1. On looking at the source code, we can see a string named "market_session" cookie and further seeing the code, the token is being parse as `JSON.parse(atob(market_session))`.
2. Decoding the cookie, we get an object `{credits: 0}`.
3. Replacing the 0 with 1000000, and doing `btoa(JSON.stringify({credits: 1000000}))`, we get the new cookie value as `eyJjcmVkaXRzIjoxMDAwMDAwfQ==`.
4. Setting the new cookie value in the browser and pressing the `Buy` button, we get the flag.

### Flag:
```
Shaastra{h0w's_th3_h0OdI3??_41537}
```
