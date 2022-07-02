# Sergii Logosha, 24 Jun 2022

# Program asks user to input a credit card number, validates it and prints out the issuer of the card
# and either it is valid or not.

while 1:

    # Prompt user to enter the card number
    card_number = int(input("Enter the credit card number: ").strip())

    if 1000000000000 <= card_number <= 9999999999999:
        digits = str(card_number)
        en0 = int(digits[-2])
        en1 = int(digits[-4])
        en2 = int(digits[-6])
        en3 = int(digits[-8])
        en4 = int(digits[-10])
        en5 = int(digits[-12])

        on0 = int(digits[-1])
        on1 = int(digits[-3])
        on2 = int(digits[-5])
        on3 = int(digits[-7])
        on4 = int(digits[-9])
        on5 = int(digits[-11])
        on6 = int(digits[-13])

        en0_mult = str(en0 * 2)
        if len(en0_mult) == 2:
            x = int(en0_mult[0])
            y = int(en0_mult[1])
            z0 = x + y

        else:
            z0 = int(en0_mult)

        en1_mult = str(en1 * 2)
        if len(en1_mult) == 2:
            x = int(en1_mult[0])
            y = int(en1_mult[1])
            z1 = x + y

        else:
            z1 = int(en1_mult)

        en2_mult = str(en2 * 2)
        if len(en2_mult) == 2:
            x = int(en2_mult[0])
            y = int(en2_mult[1])
            z2 = x + y

        else:
            z2 = int(en2_mult)

        en3_mult = str(en3 * 2)
        if len(en3_mult) == 2:
            x = int(en3_mult[0])
            y = int(en3_mult[1])
            z3 = x + y

        else:
            z3 = int(en3_mult)

        en4_mult = str(en4 * 2)
        if len(en4_mult) == 2:
            x = int(en4_mult[0])
            y = int(en4_mult[1])
            z4 = x + y

        else:
            z4 = int(en4_mult)

        en5_mult = str(en5 * 2)
        if len(en5_mult) == 2:
            x = int(en5_mult[0])
            y = int(en5_mult[1])
            z5 = x + y

        else:
            z5 = int(en5_mult)

        even_sum = z0 + z1 + z2 + z3 + z4 + z5
        odd_sum = on0 + on1 + on2 + on3 + on4 + on5 + on6
        total_sum = even_sum + odd_sum
        if total_sum % 2 == 0:
            print("The card is VALID.")
            if on6 == 4:
                print("The card is issued by VISA.")
        else:
            print("The card is NOT VALID.")


    if 100000000000000 <= card_number <= 999999999999999:
        digits = str(card_number)
        en0 = int(digits[-2])
        en1 = int(digits[-4])
        en2 = int(digits[-6])
        en3 = int(digits[-8])
        en4 = int(digits[-10])
        en5 = int(digits[-12])
        en6 = int(digits[-14])

        on0 = int(digits[-1])
        on1 = int(digits[-3])
        on2 = int(digits[-5])
        on3 = int(digits[-7])
        on4 = int(digits[-9])
        on5 = int(digits[-11])
        on6 = int(digits[-13])
        on7 = int(digits[-15])

        en0_mult = str(en0 * 2)
        if len(en0_mult) == 2:
            x = int(en0_mult[0])
            y = int(en0_mult[1])
            z0 = x + y

        else:
            z0 = int(en0_mult)

        en1_mult = str(en1 * 2)
        if len(en1_mult) == 2:
            x = int(en1_mult[0])
            y = int(en1_mult[1])
            z1 = x + y

        else:
            z1 = int(en1_mult)

        en2_mult = str(en2 * 2)
        if len(en2_mult) == 2:
            x = int(en2_mult[0])
            y = int(en2_mult[1])
            z2 = x + y

        else:
            z2 = int(en2_mult)

        en3_mult = str(en3 * 2)
        if len(en3_mult) == 2:
            x = int(en3_mult[0])
            y = int(en3_mult[1])
            z3 = x + y

        else:
            z3 = int(en3_mult)

        en4_mult = str(en4 * 2)
        if len(en4_mult) == 2:
            x = int(en4_mult[0])
            y = int(en4_mult[1])
            z4 = x + y

        else:
            z4 = int(en4_mult)

        en5_mult = str(en5 * 2)
        if len(en5_mult) == 2:
            x = int(en5_mult[0])
            y = int(en5_mult[1])
            z5 = x + y

        else:
            z5 = int(en5_mult)

        en6_mult = str(en6 * 2)
        if len(en6_mult) == 2:
            x = int(en6_mult[0])
            y = int(en6_mult[1])
            z6 = x + y

        else:
            z6 = int(en6_mult)

        even_sum = z0 + z1 + z2 + z3 + z4 + z5 + z6
        odd_sum = on0 + on1 + on2 + on3 + on4 + on5 + on6 + on7
        total_sum = even_sum + odd_sum
        checker = str(card_number)
        checker = checker[0:2]
        if total_sum % 2 == 0:
            print("The card is VALID.")
            if checker == "34" or checker == "37":
                print("The card is issued by AMERICAN EXPRESS.")
        else:
            print("The card is NOT VALID.")


    if 1000000000000000 <= card_number <= 9999999999999999:
        digits = str(card_number)
        en0 = int(digits[-2])
        en1 = int(digits[-4])
        en2 = int(digits[-6])
        en3 = int(digits[-8])
        en4 = int(digits[-10])
        en5 = int(digits[-12])
        en6 = int(digits[-14])
        en7 = int(digits[-16])

        on0 = int(digits[-1])
        on1 = int(digits[-3])
        on2 = int(digits[-5])
        on3 = int(digits[-7])
        on4 = int(digits[-9])
        on5 = int(digits[-11])
        on6 = int(digits[-13])
        on7 = int(digits[-15])

        en0_mult = str(en0 * 2)
        if len(en0_mult) == 2:
            x = int(en0_mult[0])
            y = int(en0_mult[1])
            z0 = x + y

        else:
            z0 = int(en0_mult)

        en1_mult = str(en1 * 2)
        if len(en1_mult) == 2:
            x = int(en1_mult[0])
            y = int(en1_mult[1])
            z1 = x + y

        else:
            z1 = int(en1_mult)

        en2_mult = str(en2 * 2)
        if len(en2_mult) == 2:
            x = int(en2_mult[0])
            y = int(en2_mult[1])
            z2 = x + y

        else:
            z2 = int(en2_mult)

        en3_mult = str(en3 * 2)
        if len(en3_mult) == 2:
            x = int(en3_mult[0])
            y = int(en3_mult[1])
            z3 = x + y

        else:
            z3 = int(en3_mult)

        en4_mult = str(en4 * 2)
        if len(en4_mult) == 2:
            x = int(en4_mult[0])
            y = int(en4_mult[1])
            z4 = x + y

        else:
            z4 = int(en4_mult)

        en5_mult = str(en5 * 2)
        if len(en5_mult) == 2:
            x = int(en5_mult[0])
            y = int(en5_mult[1])
            z5 = x + y

        else:
            z5 = int(en5_mult)

        en6_mult = str(en6 * 2)
        if len(en6_mult) == 2:
            x = int(en6_mult[0])
            y = int(en6_mult[1])
            z6 = x + y

        else:
            z6 = int(en6_mult)

        en7_mult = str(en7 * 2)
        if len(en7_mult) == 2:
            x = int(en7_mult[0])
            y = int(en7_mult[1])
            z7 = x + y

        else:
            z7 = int(en7_mult)

        even_sum = z0 + z1 + z2 + z3 + z4 + z5 + z6 +z7
        odd_sum = on0 + on1 + on2 + on3 + on4 + on5 + on6 + on7
        total_sum = even_sum + odd_sum
        checker = str(card_number)
        checker = checker[0:2]
        if total_sum % 2 == 0:
            print("The card is VALID.")
            if on7 == 4:
                print("The card is issued by VISA.")
            if checker == "51" or checker == "52" or checker == "53" or checker == "54" or checker == "55":
                print("The card is issued by MASTER CARD.")
        else:
            print("The card is NOT VALID.")

    else:
        pass

