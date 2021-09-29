# Given 2 strings text and pattern, the contents of the string text are re-arranged according to the indices order in the string pattern
# Example: 
# text = "101101", pattern = "210354"
# The function returns = "101110"

def permutate(text,pattern):
    permuted = ""
    for i in pattern:
        permuted+=text[int(i)]
    return permuted

  
# Given 2 binary strings, s1 and s2, an XOR value of the strings is returned as a string
# Example:
# s1 = "1010", s2 = "0010"
# The function returns = "1000"

def xor(s1,s2):
    s3 = ""
    for i in range(len(s1)):
        s3 += str(int(s1[i])^int(s2[i]))
    return s3
