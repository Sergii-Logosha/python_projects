# Sergii Logosha, 11.11.2022

# The program include function that returns list of keys of the given
# dictionary by the values.

def search_of_keys(dictionary, value):
    keys = []
    for i in dictionary:
        if dictionary[i] == value:
            keys.append(i)
    return keys


girls = {1: "Ira",
         2: "Tanya",
         3: "Ira",
         4: "Nastya",
         5: "Alina",
         6: "Ira",
         7: "Marina",
         }

print(search_of_keys(girls, "Laura"))
