# Sergii Logosha, 26 Jun 2022

# The program asks user his username and password and returns message with the password length

user_name = input("Username: ")
password = input("Password: ")

password_length = len(password)

print(f"{user_name}, your password {('*' * password_length)} is {password_length} symbols long.")

