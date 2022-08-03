# Sergii Logosha, 03 Aug 2022

# The program prompts user to input musical note and outputs the frequency of
# the note

C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88

note = input("Note: ").strip()

if note == 'C4':
    print(f"Frequency of the note: {C4}Gz")
elif note == 'D4':
    print(f"Frequency of the note: {D4}Gz")
elif note == 'E4':
    print(f"Frequency of the note: {E4}Gz")
elif note == 'F4':
    print(f"Frequency of the note: {F4}Gz")
elif note == 'G4':
    print(f"Frequency of the note: {G4}Gz")
elif note == 'A4':
    print(f"Frequency of the note: {A4}Gz")
elif note == 'B4':
    print(f"Frequency of the note: {B4}Gz")

