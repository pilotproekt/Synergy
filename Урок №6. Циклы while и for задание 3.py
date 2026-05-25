a = int(input())
b = int(input())
if a % 2 == 0:
    num = a
else:
    num = a + 1
while num <= b:
    print(num, end=' ')
    num += 2

