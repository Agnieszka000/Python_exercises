# Hackerrank - Diagional Difference
# Given a square matrix, calculate the absolute difference between the sums of its diagonals (pl. przekątne). 

# It is expected to obtain an INTEGER.
# It accepts 2D_INTEGER_ARRAY arr as parameter.
# 2D array (list) contains sublist as rows.

n = 3 # the number of rows and column in the array

arr = [
    [11,2,4],   # 1st row
    [4,5,6],    # 2nd row
    [10,8,-12]  # 3rd row
] 

list_left = []
list_right = []
digit_from_left = n - n - 1

for row in range(n):
    list_left.append((arr[row])[row])
    
    list_right.append((arr[row])[digit_from_left])
    digit_from_left -= 1

# To sum up all integers in a list we can use sum()
sum1 = sum(list_left)
sum2 = sum(list_right)

# To obtain the absolute number we can use abs()
absolute_difference = abs(sum1 - sum2)


print(absolute_difference)