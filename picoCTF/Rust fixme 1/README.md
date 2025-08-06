# Rust Fixme 1
Tags: `easy`, `general skills`

## Problem Statement:
Have you heard of Rust? Fix the syntax errors in this Rust file to print the flag!
Download the Rust code [here](https://challenge-files.picoctf.net/c_verbal_sleep/3f0e13f541928f420d9c8c96b06d4dbf7b2fa18b15adbd457108e8c80a1f5883/fixme1.tar.gz).

## My Approach:
1. Download the file and do strings on it.
2. We can find a rust function that prints the flag, but it's broken.
3. The correct, fixed rust file is [here](./code.rs).
4. On running the `cargo run` command, we should see the flag printed.

### Flag:
```
picoCTF{4r3_y0u_4_ru$t4c30n_n0w?}
```