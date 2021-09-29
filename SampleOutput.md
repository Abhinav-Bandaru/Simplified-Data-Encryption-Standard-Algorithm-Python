# KEY GENERATION

## Output: 

Enter 10-bit Key: 1010000010 <br><br>

Key Generation: 
P10: 3 5 2 7 4 10 1 9 8 6 

After Permutation using P10:  1000001100
After Left Shift-1 for both Halves:  0000111000

P8: 6 3 7 4 8 5 10 9
After Permutation using P8, Key 1:  10100100

After Left Shift-2 for both Halves:  0010000011
After Permutation using P8, Key 2:  01000011




# ENCRYPTION with above generated keys 
### function call = func(key1, key2), input = "10010111"

## Output:

S-DES Encryption: 

Enter 8 bit Plain Text: 10010111
I/P order sequence: 2 6 3 1 | 4 8 5 7
After IP:  01011101

E/P order sequence: 4 1 2 3 | 2 3 4 1

Right 4-bit is taken for Encryption first: 
After E/P:  11101011

Now we do XOR with Key 1: 
11101011 ^ key 1
11101011 ^ 10100100
After XOR:  01001111

S-Boxes: 
S0:  [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
S1:  [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

First 4 bits we take: 
Row:  00
Column:  10
S0[ 0 ][ 2 ] =  3  ->  11

Next 4 bits we take: 
Row:  11
Column:  11
S1[ 3 ][ 3 ] =  3  ->  11

P4: 2 4 3 1
After Permuting with P4:  1111

Now we do XOR with Left 4 bit: 
0101 ^ 1111
After XOR:  1010
First round of operation is completed

Swapping: 
Temporary text:  11011010

Now we Repeat the process with key 2: 


Right 4-bit is taken for Encryption first: 
After E/P:  01010101

Now we do XOR with Key 2: 
01010101 ^ key 2
01010101 ^ 01000011
After XOR:  00010110

S-Boxes: 
S0:  [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
S1:  [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

First 4 bits we take: 
Row:  01
Column:  00
S0[ 1 ][ 0 ] =  3  ->  11

Next 4 bits we take: 
Row:  00
Column:  11
S1[ 0 ][ 3 ] =  3  ->  11

P4: 2 4 3 1
After Permuting with P4:  1111

Now we do XOR with Left 4 bit: 
1101 ^ 1111
After XOR:  0010

Second round of operation is completed
New Text:  00101010
IP Inverse Sequence: 4 1 3 5 7 2 8 6

On applying IP Inverse, CIPHER TEXT:  00111000









# DECRYPTION with above generated keys
### function call = func(key2, key1), input = "00111000" (Cipher text generated in encryption)

## Output:

S-DES Encryption: 

Enter 8 bit Plain Text: 00111000
I/P order sequence: 2 6 3 1 | 4 8 5 7
After IP:  00101010

E/P order sequence: 4 1 2 3 | 2 3 4 1

Right 4-bit is taken for Encryption first: 
After E/P:  01010101

Now we do XOR with Key 1: 
01010101 ^ key 1
01010101 ^ 01000011
After XOR:  00010110

S-Boxes: 
S0:  [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
S1:  [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

First 4 bits we take: 
Row:  01
Column:  00
S0[ 1 ][ 0 ] =  3  ->  11

Next 4 bits we take: 
Row:  00
Column:  11
S1[ 0 ][ 3 ] =  3  ->  11

P4: 2 4 3 1
After Permuting with P4:  1111

Now we do XOR with Left 4 bit: 
0010 ^ 1111
After XOR:  1101
First round of operation is completed

Swapping: 
Temporary text:  10101101

Now we Repeat the process with key 2: 


Right 4-bit is taken for Encryption first: 
After E/P:  11101011

Now we do XOR with Key 2: 
11101011 ^ key 2
11101011 ^ 10100100
After XOR:  01001111

S-Boxes: 
S0:  [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
S1:  [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

First 4 bits we take: 
Row:  00
Column:  10
S0[ 0 ][ 2 ] =  3  ->  11

Next 4 bits we take: 
Row:  11
Column:  11
S1[ 3 ][ 3 ] =  3  ->  11

P4: 2 4 3 1
After Permuting with P4:  1111

Now we do XOR with Left 4 bit: 
1010 ^ 1111
After XOR:  0101

Second round of operation is completed
New Text:  01011101
IP Inverse Sequence: 4 1 3 5 7 2 8 6

On applying IP Inverse, CIPHER TEXT:  10010111   (original plaintext)
