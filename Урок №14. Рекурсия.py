def tmp(x, ind=0):
    if ind >= len(x):
        print("Конец списка")
        return
    print(x[ind])
    tmp(x, ind + 1)


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
tmp(my_list)

