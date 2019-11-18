#！/usr/bin/env python3

num1 = 1
while num1 <= 9:
    num2 = 1
    while num2 <= 10 - num1:
        print("%d * %d = %d" % (num2,num1,num1*num2), end="\t")
        num2 = num2 + 1
    print()
    num1 = num1 + 1