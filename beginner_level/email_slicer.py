# Author: Sergii Logosha
# Date Created: 05.06.2022
# Last Modified: 05.06.2022

# Description 
# Program cuts out pieces of an e-mail and prints it it to the screen.

# Usage
# 
# get user e-mail address
email = input("What is your e-mail address? ").strip()
# slice out the user name
user = email[:email.index("@")]
# slice domain name
domain = email[email.index("@") + 1 :]
# format message
output = "Your username is {} and your domain name is {}."
message = output.format(user, domain)
# display output message
print(message)