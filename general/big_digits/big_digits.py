# 30.11.23. Sergii Logosha sergiilogosha@gmail.com

import sys

zero = ['  *  ',
        '*   *',
        '*   *',
        '*   *',
        '*   *',
        '*   *',
        '  *  ']
one = ['  *  ',
       ' **  ',
       '* *  ',
       '  *  ',
       '  *  ',
       '  *  ',
       '*****']
two = [' *** ',
       '*   *',
       '*   *',
       '   * ',
       '  *  ',
       ' *   ',
       '*****']
three = [' *** ',
         '*   *',
         '    *',
         '   **',
         '    *',
         '*   *',
         ' *** ']
four = ["   * ",
        "  ** ",
        " * * ",
        "*  * ",
        "*****",
        "   * ",
        "   * "]
five = ["*****",
        "*    ",
        "*    ",
        " *** ",
        "    *",
        "*   *",
        " *** "]
six = [" *** ",
       "*    ",
       "*    ",
       "**** ",
       "*   *",
       "*   *",
       " *** "]
seven = ["*****",
         "    *",
         "   * ",
         "  *  ",
         " *   ",
         "*    ",
         "*    "]
eight = [" *** ",
         "*   *",
         "*   *",
         " *** ",
         "*   *",
         "*   *",
         " *** "]
nine = [" ****",
        "*   *",
        "*   *",
        " ****",
        "    *",
        "    *",
        "    *"]
all_digits = [zero, one, two, three, four, five, six, seven, eight, nine]

try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ''
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = all_digits[number]
            line += digit[row] + '  '
            column += 1
        print(line)
        row += 1
except IndexError:
    print('usage: big_digits.py <some number>')
except ValueError as err:
    print(err, 'in', digits)
