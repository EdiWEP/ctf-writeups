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