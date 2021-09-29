# Author: Abhinav Bandaru
# KEY GENERATION: 
# This program is used to generate two 8-bit binary keys, from a given 10-bit binary key
# All the steps followed in this program are predefined steps of the Simplified DES Algorithm

key = input("Enter 10-bit binary Key: ")
p10 = "2416390875"   # Predefined permutation pattern
print("\nKey Generation: ")
print("P10: 3 5 2 7 4 10 1 9 8 6")

key = permutate(key,p10)
print("\nAfter Permutation using P10: ",key)
key = key[1:5]+key[0]+key[6:10]+key[5]  # Performing Left Shift
print("After Left Shift-1 for both Halves: ",key)

p8 = "52637498"  # Predefined permutation pattern
print("\nP8: 6 3 7 4 8 5 10 9")
key1 = permutate(key,p8)
print("After Permutation using P8, Key 1: ",key1)  # Key 1 Generated

key = key[1:5]+key[0]+key[6:10]+key[5] # Performing Left Shift
key = key[1:5]+key[0]+key[6:10]+key[5] # Performing Left Shift

print("\nAfter Left Shift-2 for both Halves: ",key)
key2 = permutate(key,p8)
print("After Permutation using P8, Key 2: ",key2)  # Key 2 Generated
