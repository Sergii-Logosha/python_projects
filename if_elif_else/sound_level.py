# Sergii Logosha, 22 Jul 2022

# The program asks user to input level of the sound in dB and prints out
# what that sound is equal to.

LIBRARY = 40
RADIO = 70
TRACTOR = 106
CHAIN_SAW = 120

sound_level = int(input("Sound level(dB): ").strip())

if sound_level < LIBRARY:
    print("The sound is lower then in a quiet room.")
elif sound_level == LIBRARY:
    print("The sound is equal to the sound in a library.")
elif sound_level < RADIO:
    print("The sound is similar to a conversation at home.")
elif sound_level == RADIO:
    print("The sound is equal to the sound of radio, TV.")
elif sound_level < TRACTOR:
    print("The sound is similar to the sound of a dishwasher.")
elif sound_level == TRACTOR:
    print("The sound is equal to the sound of a tractor.")
elif sound_level < CHAIN_SAW:
    print("That is how sounds auto horn at 1 meter.")
elif sound_level ==CHAIN_SAW:
    print("The sound is equal to the sound of a chain saw.")
else:
    print("The sound is louder than a chain saw.")

