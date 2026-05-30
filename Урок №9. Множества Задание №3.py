n = list(map(int, input().split()))
num = set()
for i in n:
    if i in num:
        print("YES")
    else:
        print("NO")
        num.add(i)