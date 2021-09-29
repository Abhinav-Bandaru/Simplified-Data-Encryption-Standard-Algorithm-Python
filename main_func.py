# Author: Abhinav Bandaru

# The below program is wwritten based on the predefined steps of the S-DES Algorithm
# This function is used for both Encryption and Decryption

# For Encryption: inputs = key1, key2
# For Decryption: inputs = key2, key1

# Example:

# Encryption:
  # Inputs = plaintext = "10010111", key1 = "10100100", key2 = "01000011"
  # Function call = func(key1, key2)
  # Output = ciphertext = "00111000"
  
# Decryption:
  # Inputs = plaintext = "00111000", key1 = "10100100", key2 = "01000011"
  # Function call = func(key2, key1)
  # Output = ciphertext = "10010111"

def func(key1,key2):
  
    print("S-DES Encryption: \n")
    plaintext = input("Enter 8 bit Plain Text: ")
    ip = "15203746"   # Predefined permutation sequence
    
    print("I/P order sequence: 2 6 3 1 | 4 8 5 7")
    plaintext = permutate(plaintext, ip)
    print("After IP: ",plaintext)

    print("\nE/P order sequence: 4 1 2 3 | 2 3 4 1")
    ep = "30121230" # Predefined permutation sequence
    
    L = plaintext[:4]
    R = plaintext[4:]

    print("\nRight 4-bit is taken for Encryption first: ")
    print("After E/P: ",permutate(R,ep))

    print("\nNow we do XOR with Key 1: ")
    print(permutate(R,ep),"^ key 1")
    print(permutate(R,ep),"^",key1)
    print("After XOR: ",xor(permutate(R,ep),key1))

    eptext = xor(permutate(R,ep),key1)
    
    epL = eptext[:4]
    epR= eptext[4:]

    s0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]    # S-Box 0
    s1 = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]    # S-Box 1
    print("\nS-Boxes: ")
    print("S0: ",s0)
    print("S1: ",s1)

    print("\nFirst 4 bits we take: ")
    print("Row: ",epL[0]+epL[3])
    print("Column: ",epL[1]+epL[2])
    fk1L = s0[int(epL[0]+epL[3],2)][int(epL[1]+epL[2],2)]
    print("S0[",int(epL[0]+epL[3],2),"][",int(epL[1]+epL[2],2),"] = ",fk1L," -> ",bin(fk1L)[2:])

    print("\nNext 4 bits we take: ")
    print("Row: ",epR[0]+epR[3])
    print("Column: ",epR[1]+epR[2])
    fk1R = s1[int(epR[0]+epR[3],2)][int(epR[1]+epR[2],2)]
    print("S1[",int(epR[0]+epR[3],2),"][",int(epR[1]+epR[2],2),"] = ",fk1R," -> ",bin(fk1R)[2:])

    temp = str(bin(fk1L)[2:]+bin(fk1R)[2:])
    print("\nP4: 2 4 3 1")
    p4_pattern = "1320"   # Predefined permutation sequence
    p4 = permutate(temp,p4_pattern)
    print("After Permuting with P4: ",p4)

    fk1 = xor(L,p4)
    print("\nNow we do XOR with Left 4 bit: ")
    print(L,"^",p4)
    print("After XOR: ",fk1)
    print("First round of operation is completed")

    print("\nSwapping: ")
    print("Temporary text: ",R+fk1)
    temp_text = R+fk1

    print("\nNow we Repeat the process with key 2: \n")
    L = temp_text[:4]
    R = temp_text[4:]

    print("\nRight 4-bit is taken for Encryption first: ")
    print("After E/P: ",permutate(R,ep))

    print("\nNow we do XOR with Key 2: ")
    print(permutate(R,ep),"^ key 2")
    print(permutate(R,ep),"^",key2)
    print("After XOR: ",xor(permutate(R,ep),key2))

    eptext = xor(permutate(R,ep),key2)
    epL = eptext[:4]
    epR= eptext[4:]

    print("\nS-Boxes: ")
    print("S0: ",s0)
    print("S1: ",s1)

    print("\nFirst 4 bits we take: ")
    print("Row: ",epL[0]+epL[3])
    print("Column: ",epL[1]+epL[2])
    fk1L = s0[int(epL[0]+epL[3],2)][int(epL[1]+epL[2],2)]
    print("S0[",int(epL[0]+epL[3],2),"][",int(epL[1]+epL[2],2),"] = ",fk1L," -> ",bin(fk1L)[2:].zfill(2))

    print("\nNext 4 bits we take: ")
    print("Row: ",epR[0]+epR[3])
    print("Column: ",epR[1]+epR[2])
    fk1R = s1[int(epR[0]+epR[3],2)][int(epR[1]+epR[2],2)]
    print("S1[",int(epR[0]+epR[3],2),"][",int(epR[1]+epR[2],2),"] = ",fk1R," -> ",bin(fk1R)[2:].zfill(2))

    temp = str(bin(fk1L)[2:].zfill(2)+bin(fk1R)[2:].zfill(2))
    print("\nP4: 2 4 3 1")
    p4_pattern = "1320"   # Predefined permutation sequence
    p4 = permutate(temp,p4_pattern)
    print("After Permuting with P4: ",p4)

    fk1 = xor(L,p4)
    print("\nNow we do XOR with Left 4 bit: ")
    print(L,"^",p4)

    print("After XOR: ",fk1)
    print("\nSecond round of operation is completed")

    ipinv = "30246175"    # Predefined permutation sequence
    print("New Text: ",fk1+R)
    temp2 = fk1+R
    print("IP Inverse Sequence: 4 1 3 5 7 2 8 6")
    print("\nOn applying IP Inverse, CIPHER TEXT: ",permutate(temp2,ipinv))
