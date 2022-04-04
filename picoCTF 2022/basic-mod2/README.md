# picoCTF 2022 - basic-mod2
Written on 17/03/2022



## Description
Download the message. 

Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore. 

Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)



## Solution
I wrote a simple python script to read from the file and decode the message

```python
import string

MOD = 41

message = []
decode_dictionary = list('#'+ string.ascii_lowercase + string.digits + '_')

with open('message.txt', 'r') as message_file:
	content = message_file.read()
	message = content.split(' ')

decoded_message = []

for number in message:
	key = int(number) % MOD
	# Modular inverse 
	inv_mod = pow(key, -1, MOD)
	decoded_message.append(decode_dictionary[inv_mod])

decoded_message = 'picoCTF{' + ''.join(decoded_message) + '}'

print(decoded_message)
```



