# The function must return an array of integers representing the frequency of occurrence of each query string in strings.

queries = ["ab", "abc", "bc"]
strings = ["ab", "ab", "abc"]

results = []

for query in queries:
    x = 0
    for string in strings:
        if query == string:
            x += 1
    results.append(x)
        
print(results)