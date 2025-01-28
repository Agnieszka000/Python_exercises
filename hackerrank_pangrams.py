# Hackerrank
# Challenge: Pangrams

# A pangram is a string that contains every letter of the alphabet. 
# Given a sentence determine whether it is a pangram in the English alphabet. 
# Ignore case. Return either pangram or not pangram as appropriate.


def pangrams(s):
    # Write your code here
    s = set(s.lower().replace(" ",""))
    if len(s) == 26:
        print("pangram")
    else:
        print("not pangram")



s = "The quick lazy brown fox jumps over the lazy dog"
pangrams(s)