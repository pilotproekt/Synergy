x = int(input())
namber = 0
i = 1
while i * i <= x:
    if x % i == 0:
        if i * i == x:
            namber += 1
        else:
            namber += 2
    i += 1
print(namber)

