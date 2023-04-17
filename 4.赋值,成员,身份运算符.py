"""
1. 赋值运算符
    = 赋值, -= , +=, *=, /= , **=, //=, %=
"""
abc = "abc" # 一般的赋值
x = 8051005
x = x + 95
print(x)
# +=: 符号左边先加上右边再赋值给左边的变量
i = 85
i += 10
print(i)
s = "hello"
s += " Yuzu"
print(s)
# -=: 符号左边先减去右边再赋值给左边的变量
y = 127
y -= 10
print(y)
# name = "jack"
# name -= "j"   字符串可以使用 + 拼接, 但是不能使用 - 减去
# print(name)
# *=: 符号左边先乘以右边再赋值给左边的变量
a = 777
a *= 2  # 相当于 a = a * 2
print(a)
n = "888"
n *= 10     # * 计算的是字符串, 就会让字符串重复拼接
print(n)
# /=: 符号左边先除以右边再赋值给左边的变量
w = 100
w /= 10     # / : 计算结果为浮点数
print(w)
# **=: 符号的左边的多少次(右边值)幂赋值给左边
m = 2
m **= 10
print(m)
# //=: 符号的左边整除右边赋值给左边
z = 9
z //= 3
print(z)
# %=: 符号的左边对右边取余赋值给左边
q = 8
q %= 3
print(q)
"""
2. 成员运算符
    in 在里面, not in 不在里面
"""
string = "volunteer"
if "v" in string:
    print("v在里面")
if "a" not in string:
    print("a不在里面")
# 列表(list): 跟字符串都是容器类型数据, 就是中括号(方括号) [] 放入数据
list001 = []    # 空列表, 什么都没有, 长度为0, False
str001 = ""     # 空字符串, 长度为0, False
print(type(list001))    # < class 'list'>
list002 = ["字符串", True, 3.123, 100]
print(list002)
if True in list002 or False in list002:
    print("列表中有布尔值")
if 100 not in list002:
    print("100不在列表中")
else:
    print("列表中有100")
"""
3.身份运算符
    is 是, is not 不是; 判断变量
    is: 不只会判断变量在数值上大小相等, 还会判断类型相同, id相同
    ==: 只判断数值和类型相同
"""
f = "fula"
n = "not"
if f is n:
    print("f和n是一样的")
else:
    print("f和n不一样")
number = 999
number_str = "999"
number2 = 999
print(f"number的地址是{id(number)}")
print(f"number2的地址是{id(number2)}")
print(number is number2)
print(f"字符串number_str地址是{id(number_str)}")
str_int = int(number_str)
print(number, str_int)  # 这两个变量数值相等但是id不一样, 并不是同一个常量
print(number is str_int)
print(number == str_int)
# 从键盘输入一个名字给变量,判断是否与字符串 "王一博" 是否为同一个使用is
str_name = input("请输入一个你喜欢的明星: ")
name_str = "王一博"   # 真的
print(id(name_str))
if str_name is name_str:
    print(f"是同一个人, id: {id(name_str)}")
else:
    print(" 不是我喜欢的那个, 假的id: {}".format(id(str_name)))
