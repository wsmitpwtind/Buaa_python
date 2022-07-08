from decimal import Decimal


def fun(x):
    if x == 0:
        return 1
    elif x == 1:
        return 3
    else:
        return (fun(x-2) + fun(x-1))/(1.01**fun(x-1))


n = int(input())
print(Decimal(fun(n)).quantize(Decimal("0.00")))