# Sergii Logosha, 08 Jun 2022
# Modified 09 Jun 2022

# Program calculates dog's age in human years

# Prompr user to input dog's name
dog_name = input("What is your dog's name?\n")

# Prompt user to input dog's age
dog_age = int(input("What is your dog's age?\n"))

# Calculate the dog age in human years
human_age = dog_age * 7

# Print out the final message
print("Your dog", dog_name, "is" , human_age, "years old in human years.")