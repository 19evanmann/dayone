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

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

secret_m = input("What would you like your message to be?")
for char in secret_m:
    if char in "  ?,.!?:;":
        secret_m = secret_m.replace(char, '')
shift_v = input("How many letters whould you like to shift your encryption?")

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
       "z":26
       }

output_message = [dic.get(n, n) for n in secret_m.lower()]
arrayed_message = numpy.array(output_message)
shifted_output = arrayed_message + 3
print(output_message)
print(shifted_output)



#print(secret_m)


