# Hackerrank.com - "XOR strings 2"

# Given two strings consisting of digits 0 and 1 only, find the XOR of the two strings.
# Debug the given function strings_xor to find the XOR of the two given strings appropriately. 

def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0';
        else:
            res += '1';

    return res

s = "10101"
t = "00101"
print(strings_xor(s, t))