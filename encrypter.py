## enigma Machine##

# requirements:#
# 1. Take an input (number between 1-25 and that is the shift) #
# 2. Strip white space (strip white space and punctuation) #
# 3. Make single strings #
# 4. Split variables into individual letters in an array #
# 5. Find number value of each letter #
# 6. Add shift to letter value #
# 7. Get letter from shifted value #
# 8. Print #
import numpy
import tkinter

def shrunk():
    global shift_v
    if shift_v > 26:
        shift_v = shift_v - 26
        shrunk()
    elif shift_v == 26:
        print("try a better code")

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "zg", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

secret_m = input("What would you like your message to be?")
for char in secret_m:
    if char in " ?,.!?:;":
        secret_m = secret_m.replace(char, '')
shift_v = int(input("How many letters whould you like to shift your encryption?"))

shrunk()

#make a dictionary of values
dic = {"a":1,
       "b":2,
       "c":3,
       "d":4,
       "e":5,
       "f":6,
       "g":7,
       "h":8,
       "i":9,
       "j":10,
       "k":11,
       "l":12,
       "m":13,
       "n":14,
       "o":15,
       "p":16,
       "q":17,
       "r":18,
       "s":19,
       "t":20,
       "u":21,
       "v":22,
       "w":23,
       "x":24,
       "y":25,
       "z":26,
       }
dic_2 = {1:"a",
       2:"b",
       3:"c",
       4:"d",
       5:"e",
       6:"f",
       7:"g",
       8:"h",
       9:"i",
       10:"j",
       11:"k",
       12:"l",
       13:"m",
       14:"n",
       15:"o",
       16:"p",
       17:"q",
       18:"r",
       19:"s",
       20:"t",
       21:"u",
       22:"v",
       23:"w",
       24:"x",
       25:"y",
       26:"z",
       27:"a",
       28:"b",
       29:"c",
       30:"d",
       31:"e",
       32:"f",
       33:"g",
       34:"h",
       35:"i",
       36:"j",
       37:"k",
       38:"l",
       39:"m",
       40:"n",
       41:"o",
       42:"p",
       43:"q",
       44:"r",
       45:"s",
       46:"t",
       47:"u",
       48:"v",
       49:"w",
       50:"x",
       51:"y",
       52:"z",}

output_message = [dic.get(n, n) for n in secret_m.lower()]

arrayed_message = numpy.array(output_message)

shifted_output = arrayed_message + shift_v

#Optional#
#print(output_message)
#print(shifted_output)

letter_message = [dic_2.get(n, n) for n in shifted_output]

encrypt = numpy.array(letter_message)

letter_message = "".join(letter_message)

print(letter_message)

#print(secret_m)

