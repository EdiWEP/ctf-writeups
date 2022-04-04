
users = []
passwords = []


with open('./leak/passwords.txt') as passwords_input, open('./leak/usernames.txt') as users_input:
	users = users_input.readlines()
	passwords = passwords_input.readlines()


for user,password in zip(users,passwords):
	if user.strip() == 'cultiris':
		print ('Username: {0} \t\t Password: {1}'.format(user.strip(),password.strip()))