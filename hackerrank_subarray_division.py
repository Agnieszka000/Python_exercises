# Hackerrank.com - "Subarray division"

# Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.
# Lily decides to share a contiguous segment of the bar selected such that:
### The length of the segment matches Ron's birth month, and,
### The sum of the integers on the squares is equal to his birth day.
# Determine how many ways she can divide the chocolate.


# s = numbers on each of the squares of chocolate
# d = Ron's birth day = sum of the integers on the squares
# m = Ron's birth month = length of the segment


s = [2,2,1,3,2]
d = 4 # sum of the integers on the squares
m = 2 # length of the segment

# Let's start addition from the item with the index [0] from the list s:
index_of_item_from_array = 0
# Counter for sum of items that equals to d.
results_counter = 0

while index_of_item_from_array <= (len(s)):
    # Let's sum the integers from index 0 till index that equals to m:
    result = sum(s[index_of_item_from_array:m])
    # print(f"The result for index {index_of_item_from_array} is {result}.")
    index_of_item_from_array += 1
    m += 1
    # If the sum equals to d, add 1 to the results we're looking for counter.
    if result == d:
        results_counter += 1
print(f"The number of possibilities: {results_counter}.")
    
