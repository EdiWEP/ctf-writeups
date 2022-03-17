# CyberEdu - [why-xor](https://app.cyberedu.ro/challenges/f57d78e0-3639-11eb-993e-e927c3757fd3/) 
Written on 02/03/2022



## Description
Let's be fair, we all start with XOR, and we keep enjoying it.

Flag format: ctf{sha256}



## Analyzing xor.py

We get a file, xor.py. This is the content:

```python
xored = ['\x00', '\x00', '\x00', '\x18', 'C', '_', '\x05', 'E', 'V', 'T', 'F', 'U', 'R', 'B', '_', 'U', 'G', '_', 'V', '\x17', 'V', 'S', '@', '\x03', '[', 'C', '\x02', '\x07', 'C', 'Q', 'S', 'M', '\x02', 'P', 'M', '_', 'S', '\x12', 'V', '\x07', 'B', 'V', 'Q', '\x15', 'S', 'T', '\x11', '_', '\x05', 'A', 'P', '\x02', '\x17', 'R', 'Q', 'L', '\x04', 'P', 'E', 'W', 'P', 'L', '\x04', '\x07', '\x15', 'T', 'V', 'L', '\x1b']
s1 = ""
s2 = ""
# ['\x00', '\x00', '\x00'] at start of xored is the best hint you get
a_list = [chr(ord(a) ^ ord(b)) for a,b in zip(s1, s2)]
print(a_list)
print("".join(a_list))
```

It's declaring an array of bytes in hex representation(note the `\x`)
And then it declares two empty strings that it zips together and xors the characters of

Implicitly, we need to replace those empty strings with something in order to run the script and generate the flag

There are actually two major hints to take into account when solving this

1. The flag format
2. The comment inside the script

 *Note: in the original description, flag format is shown to be CTF{sha256} instead of ctf{sha256}. The original flag format is incorrect. This is important for reasons I'll get to next*

 
## Flag format

The flag format is pretty standard, **sha256** is a hashing algorithm that hashes data into 256-bit hexadecimal strings. 

256 bits = 32 bytes

And because the format is hexadecimal, we're looking at 64 characters inside the curly braces of the flag

It is also important to note that the flag starts with `ctf{` and ends with `}`


## The comment

As the name of the challenge implies, solving it has something to do with xor

With a simple `print(len(xored))` we see that it holds 69 bytes, which is exactly the length of our flag:

-  `ctf{` -> 4 bytes 
- `sha256` -> 64 bytes for the hexadecimal representation
- `}` ->  1 byte for the ending curly brace

So we can assume that `xored` contains the flag xored with **something**

The comment inside the code addresses this. What it means is that whatever string the original flag was xored with starts with  `ctf` as the first 3 characters.

To explain this, here are some properties of XOR:

- A xor A = 0
- A xor 0 = A
- Let C = A xor B, this imples => C xor A = B and C xor B = A
 
So in order for the first 3 bytes of the xored flag to be null bytes (`\x00`),  they must have been xored with the same 3 bytes, this is what the comment is hinting at.


## Solution

Next, let's look at the fourth and the last byte, we know these must be `{` and `}` respectively in the original flag, so `xored[3]` and `xored[-1]` are the xored curly braces

In the script, `xored[3]` is `\x18` and `xored[-1]` is `\x1b` 

In ASCII, `{` is `0x7b` and `}` is `0x7d`

To find out what they were xored with, we xor the values in xored with the ASCII table values:

- `0x7b` ^ `0x18` is `0x63`, which is `c` in ASCII
- `0x7d` ^ `x1b` is `0x66`, which is `f` in ASCII

 Seeing how there are **also** letters of "ctf", I decided to try and repeat the "ctf" pattern across the whole string of the original flag. Here's the solution in python

 ```python
xored = ['\x00', '\x00', '\x00', '\x18', 'C', '_', '\x05', 'E', 'V', 'T', 'F', 'U', 'R', 'B', '_', 'U', 'G', '_', 'V', '\x17', 'V', 'S', '@', '\x03', '[', 'C', '\x02', '\x07', 'C', 'Q', 'S', 'M', '\x02', 'P', 'M', '_', 'S', '\x12', 'V', '\x07', 'B', 'V', 'Q', '\x15', 'S', 'T', '\x11', '_', '\x05', 'A', 'P', '\x02', '\x17', 'R', 'Q', 'L', '\x04', 'P', 'E', 'W', 'P', 'L', '\x04', '\x07', '\x15', 'T', 'V', 'L', '\x1b']
s1 = "".join(xored)
s2 = "ctf" * 23 # 63 // 3 (3 is length of "ctf")

# ['\x00', '\x00', '\x00'] at start of xored is the best hint you get
a_list = [chr(ord(a) ^ ord(b)) for a,b in zip(s1, s2)]
print("".join(a_list)) 
```

Running this, we get a what looks like a legitimate flag, as the characters between curly braces are all hexadecimal digits

Inputing it onto CyberEdu confirms it is the correct flag!


## Conclusion

This was a nice beginner exercise that helps to remind you of xor properties and not overthinking when unnecessary.  



