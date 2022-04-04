# picoCTF 2022 - credstuff 
Written on 17/03/2022


## Description

We found a leak of a blackmarket website's login credentials. Can you find the password of the user `cultiris` and successfully decrypt it? 

The first user in `usernames.txt` corresponds to the first password in `passwords.txt`. The second user corresponds to the second password, and so on.



## Solution
First, I used a script to find the password associated with username `cultiris`

```python
users = []
passwords = []

with open('./leak/passwords.txt') as passwords_input, open('./leak/usernames.txt') as users_input:
	users = users_input.readlines()
	passwords = passwords_input.readlines()


for user,password in zip(users,passwords):
	if user.strip() == 'cultiris':
		print ('Username: {0} \t\t Password: {1}'.format(user.strip(),password.strip()))
```

Seeing that it looked kinda like a flag, I first thought to try all ROT-N ciphers on it. So I modified the script to do that and look for a flag-like pattern, and it worked

```python
from string import ascii_lowercase, ascii_uppercase

users = []
passwords = []

flag = ''

# Read from input files
with open('./leak/passwords.txt') as passwords_input, open('./leak/usernames.txt') as users_input:
    users = users_input.readlines()
    passwords = passwords_input.readlines()


for user, password in zip(users,passwords):
    # Find the password we're looking for
    if user.strip() == 'cultiris':
        
        # Try all possible rotation ciphers
        for rot in range(1,26):
            rotated_password = []
            for c in password.strip():

                ascii_code = 0

                # Rotate lowercase letters
                if c in ascii_lowercase:
                    
                    ascii_code = ord(c) + rot
                    
                    if ascii_code > ord('z'):
                        ascii_code = ascii_code - ord('z') - 1 + ord('a')

                # Rotate uppercase letters
                elif c in ascii_uppercase:
                    ascii_code = ord(c) + rot
                    
                    if ascii_code > ord('Z'):
                        ascii_code = ascii_code - ord('Z') - 1 + ord('A')
                # For anything that's not a letter, make no changes
                else:
                    ascii_code = ord(c)
                
                rotated_password.append(chr(ascii_code))
            
            password_string = ''.join(rotated_password)
            print(f'ROT{rot}: {password_string}')

            # If the first characters look like a flag, save it 
            if password_string[:7].lower() == 'picoctf':
                flag = password_string

if flag != '':
    print(f'\nFOUND FLAG: {flag}')
```



