a = int(input())
b = list(map(int, input().split()))
res = []
res.append(b[-1])
for i in range(len(b) - 1):
    res.append(b[i])
print(res)

