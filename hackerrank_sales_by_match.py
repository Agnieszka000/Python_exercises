# Hackerrank.com - Challenge: "Sales by match"

# There is a large pile of socks that must be paired by color. 
# Given an array of integers representing the color of each sock, 
# determine how many pairs of socks with matching colors there are.

# number of socks
n = 9
# each digit represents a colour
ar = [10,20,20,10,10,30,50,10,20] 


def sockMerchant(n, ar):
    
    # Use set to find how many unique colours there are in ar:
    total_pairs_count = 0
    unique_colours = set(ar)
    
    # Check how many socks of a unique colour there are:
    for colour in unique_colours:
        # Use .count to count all the items of the same colour:
        same_colour_count = ar.count(colour)
        pairs = same_colour_count // 2 
        print(f"The colour {colour} appears {same_colour_count} times.")
        print(f"There is/are {pairs} pair(s) of socks in the colour {colour}.")
        total_pairs_count = total_pairs_count + int(pairs)
    print(f"\nTotal sum of pairs:{total_pairs_count}\n")
    
sockMerchant(n,ar)