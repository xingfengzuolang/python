import os
import multiprocessing


# 打开计算器
# os.system("C:\\Windows\\System32\\calc.exe")

# 打开一张图片
# os.system("C:\\Windows\\System32\\mspaint.exe C:\\Users\\Administrator\\Desktop\\851cde34e8dd70c4cc2a31c322171ce3.png")


cpu_num = '1'

if 'NUMBER_OF_PROCESSORS' in os.environ:
    cpu_num = os.environ['NUMBER_OF_PROCESSORS']

print ('cpu_num: %s' % cpu_num)
print ( multiprocessing.cpu_count())
print(os.cpu_count())
print(os.getcwd())
print(os.getlogin())
print(os.urandom(4))