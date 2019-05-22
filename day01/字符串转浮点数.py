from functools import reduce

DIGITS = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
def str2float(s):
    s1,s2 = s.split('.')
    def char2num(s):
        return DIGITS[s]
    return reduce(lambda x,y : x*10+y, map(char2num,s1)) + reduce(lambda x,y : x*10+y, map(char2num,s2))/pow(10,len(s2))
print(isinstance(str2float('123.456'),float))
print(str2float('123.456'))