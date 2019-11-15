score = int(input("输入一个分数:"))

if score < 0 or score > 100:
    grade = "输入的分数超出范围"
elif score >= 90:
    grade = "A"
elif score >= 60:
    grade = "B"
else:
    grade = "C"

print('%d 属于 %s' % (score,grade))
