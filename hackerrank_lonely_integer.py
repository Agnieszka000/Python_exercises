# Hackerrank, challenge: Lonely Integer:
# Given an array of integers, where all elements but one occur twice, find the unique element. 
# -----------------------------------------
# Complete the 'lonelyinteger' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.

def lonelyinteger(a):
    # Write your code here
    sorted_list = sorted(a)

    while len(sorted_list) > 0:
        if len(sorted_list) == 1:
            return sorted_list[0]
            break
        elif sorted_list[0] != sorted_list[1]:
            return sorted_list[0]
            break
        elif sorted_list[0] == sorted_list[1]:
            sorted_list.remove(sorted_list[0])
            sorted_list.remove(sorted_list[0])
            continue
   
a = [59,88,14,8,85,1,94,74,57,96,39,2,47,43,35,17,53,52,92,31,99,48,94,30,92,60,32,45,88,13,39,50,22,65,89,46,65,76,57,67,99,35,76,46,85,82,45,62,53,80,74,22,31,52,82,13,41,96,2,1,80,62,4,20,50,89,59,67,60,8,41,14,47,48,17,4,43,30,32]
result = lonelyinteger(a)
print(result)