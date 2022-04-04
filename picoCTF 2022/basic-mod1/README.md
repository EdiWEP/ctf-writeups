# picoCTF 2022 - basic-mod1 
Written on 17/03/2022

## Description
We found this weird message being passed around on the servers, we think we have a working decrpytion scheme. Download the message. 

Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. 

Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)



## Solution
I wrote a simple python script to read from the file and decode the message

```python
import string

MOD = 37

message = []
decode_dictionary = list(string.ascii_lowercase + string.digits + '_')

with open('message.txt', 'r') as message_file:
	content = message_file.read()
	message = content.split(' ')

decoded_message = []

for number in message:
	key = int(number) % MOD
	decoded_message.append(decode_dictionary[key])

decoded_message = 'picoCTF{' + ''.join(decoded_message) + '}'
print(decoded_message)
```



