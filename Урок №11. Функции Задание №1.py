def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
        
tmp = [6, 5, 4, 3, 2, 1]
final = [fact(num) for num in tmp]
print(final)