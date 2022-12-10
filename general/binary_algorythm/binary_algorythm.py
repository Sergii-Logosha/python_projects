# 10.12.2022, Sergii Logosha, sergiilogosha@gmail.com

# The program is a binary algorythm that finds index of guessed number in ordered list

def algorythm(item, list_of_numbers):
    lowest = 0
    highest = len(list_of_numbers) - 1

    while lowest <= highest:
        mid = round((lowest + highest) / 2)
        guess = list_of_numbers[mid]
        if guess == item:
            return mid
        elif guess > item:
            highest = mid - 1
        else:
            lowest = mid + 1
    return None
        
    print(lowest)
    print(highest)


my_list = [3, 4, 6, 8, 9, 12, 34, 56, 67, 78]

value = algorythm(34, my_list)
print(f'The index of the guessed number is {value}')

