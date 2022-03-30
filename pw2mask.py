#!/usr/bin/env python3
# Get top x password masks from file.
# Author: Jessi
# Usage: ./pw2mask.py <passwords_file> <top-x> | Ex: ./pw2mask.py passwords.txt 3
# Description: Reads passwords from a file and generates a hashcat-like password mask, outputs the top x.
import sys
from collections import Counter


# Replace characters with mask.
def checkMask(char):
    if char.isdigit():
        return "?d"
    if char.isupper():
        return "?u"
    if char.islower():
        return "?l"
    return "?s";


# Error if not enough arguments.
if len(sys.argv) <= 1:
    print("Usage: ./pw2mask.py <passwords_file> <top-x>")
    print("Example: ./pw2mask.py passwords.txt 3")
    exit(0)


# Arguments.
passwords_file = sys.argv[1]
common_count = int(sys.argv[2]) # Set user input to int.


lines = open(passwords_file, "r").readlines() # Open password file and set lines to strings.
maskTable = [] # Create list to store password masks.


# Get masks for passwords in file.
for line in lines: 
    mask = [] # Blank array for generating the mask.
    cleanLine = line.replace('\r\n','').replace('\n','') # Cleanup the line.
    for c in cleanLine:
        mask.append(checkMask(c))
    maskTable.append("".join(mask)) # Add masks to table.


# Write to file.
with open("masks.txt", mode="wt", encoding="utf-8") as maskFile:
    maskFile.write("\n".join(maskTable))

# Get top x masks.
common = Counter(maskTable)
mostCommon = common.most_common(common_count)
commonTable = ["%i. %s" % (index + 1, value) for index, value in enumerate(mostCommon)] # Index with +1 to start at 1.
formattedTable = "\n".join(commonTable)


# Print top x masks.
print(f"    Top {common_count} Password Masks\n-----------------------------")
print(formattedTable.replace("(","").replace(")","").replace(","," :").replace("'",""))
print("\n[+] Wrote Passwords Masks to masks.txt")
