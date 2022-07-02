# Ask user for name
name = input("What is your name? ")
# Ask user for age
age = input("How old are you? ")
# Ask user for city
city = input("What city do you live in? ")
# Ask user what they enjoy
love = input("What do you love? ")
# Create output text
phrase = "Your name is {} and you are {} years old. You live in {} and you love to {}."
output = phrase.format(name, age, city, love)
# Print output to the screen
print(output)