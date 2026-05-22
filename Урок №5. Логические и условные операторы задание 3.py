mike = int(input())
ivan = int(input())
cashinvest = int(input())
if (mike >= cashinvest) and (ivan >= cashinvest):
    print(2)
else:
    if (mike >= cashinvest):
        print("Mike")
    else:
        if (ivan >= cashinvest):
            print("Ivan")
        else:
            if (ivan + mike) >= cashinvest:
                print(1)
            else:
                if (ivan + mike) < cashinvest:
                    print(0)