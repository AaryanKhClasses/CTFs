# A Special Order
`cybertea`, `web_exploitation`

## Problem Statement
The Admin of the CTEA Bakery is notoriously picky. Access to their office is only granted if you can perfectly prepare their special order from the dozens of items on the menu. Your task is to figure out the Admin's whim and validate the entire order.

[Press here for the challenge](https://bakery.cybertea.app/)

## My Solution
1. On opening the website, we go to the "Application" tab in our DevTools.
2. We inspect the cookies and find a key named `admin_order` with the value:
```
41646d696e2773207370656369616c206f726465723a206d61636164616d69615f6e75742c2073616c7465645f636172616d656c2c2063686f636f6c6174655f63686970
```
3. On decoding the hex string, we get the following text:
```
Admin's special order: macadamia_nut, salted_caramel, chocolate_chip
```
4. There's a list of ingredients in the cookies section, all with default values `false`.
5. Making the three given values `true` and refreshing the page gives us our flag.

### Flag
```
CTEA_CTF{4dm1n_1s_pr0b4bly_g00n4_b3_d14b3tic}
```
