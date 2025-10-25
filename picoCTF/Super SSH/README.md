# Super SSH
`easy`, `ssh`, `general skills`

## Problem Statement:
Using a Secure Shell (SSH) is going to be pretty important.

Can you ssh as `ctf-player` to `titan.picoctf.net` at port `53459` to get the flag?

You'll also need the password `1db87a14`. If asked, accept the fingerprint with `yes`.

## My Solution:
1. Open a terminal and connect to the server using SSH:
```bash
ssh ctf-player@titan.picoctf.net -p 53459
```
2. On connecting, the following text is printed:
```
The authenticity of host '`[titan.picoctf.net]:53459` (`[3.139.174.234]:53459`)' can't be established.

ED25519 key fingerprint is `SHA256:4S9EbTSSRXXXXX+cdM5TyzthpQryv5kudRP9XXXXXXX`.

This key is not known by any other names
Are you sure you want to continue connecting `(yes/no/[fingerprint])`?
```
3. Type `yes` to accept the fingerprint.
```
Warning: Permanently added '[titan.picoctf.net]:53459' (ED25519) to the list of known hosts.

ctf-player@titan.picoctf.net's password:
```
4. Enter the password `1db87a14` when prompted. After successful login, you will see:
```
Welcome ctf-player, here's your flag: picoCTF{s3cur3_c0nn3ct10n_45a48857}

Connection to titan.picoctf.net closed.
```

### Flag:
```
picoCTF{s3cur3_c0nn3ct10n_45a48857}
```
