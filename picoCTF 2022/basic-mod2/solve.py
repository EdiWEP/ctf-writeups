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
    inv_mod = pow(key, -1, MOD)
    decoded_message.append(decode_dictionary[inv_mod])

decoded_message = 'picoCTF{' + ''.join(decoded_message) + '}'

print(decoded_message)