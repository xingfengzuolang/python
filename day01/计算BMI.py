# -*- coding: utf-8 -*-

height = 1.75
weight = 80.5
bmi = weight/(height*height)
if bmi < 18.5:
    print(1)
elif 18.5 <= bmi < 25:
    print(2)
elif 25 <= bmi < 28:
    print(3)
elif 28 <=  bmi < 32:
    print(4)
else:
    print(5)
    pass