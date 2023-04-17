# 程序结构:
# 1. 顺序结构: 一个py文件中的代码, 从上向下执行
# 2. 选择结构: 使用if判断, 后边需要跟表达式, 表达式结果: True, False, 根据结果执行不同代码块
# 3. 循环结构: 根据条件进行循环, 当条件成立时进行循环, 不成立结束, 可以指定循环次数, 达到这个次数就结束
"""
判断语句-单分支判断:
if 表达式:
    代码块
if后边跟表达式, 后边有个  :  下边代码块需要缩进(一个tab键, 相当于四个空格)
当表达式成立, 下边的代码块执行, 如果不成立直接结束
"""
# 判断成绩及格
score = 50      # 定义成绩变量
if score >= 60:     # 判断成绩是否 大于等于60
    # 当成绩大于等于60, 表达式成立, 结果是True, 下边代码块执行
    print("恭喜你及格了!")
# 上边条件无论如何, 都会接着往下执行程序
print(f"你的成绩是: {score}")
# 例: 判断天气
weather = "晴"
# 判断
if weather == "晴":
    print("咱们打球吧!")

"""
双分支语句: 
if 表达式:
    代码块1
else:
    代码块2
当表达式成立执行代码块1, 不成立则执行代码块2
"""
# number = int(input("请输入您的彩票号码(六位数字): "))   # int类型
# if number == 321123:
#     print("恭喜, 恭喜, 您中了五百万")
# else:
#     print("很遗憾, 再接再厉!")
# 定义一个数, 当变量a 大于0 则赋值给变量b, 如果不是则 将-a赋值给变量b
a = 0
if a > 0:
    b = a
else:   # else后不跟条件表达式, 相当于 if表达式相反, not a > 0 就是 a <= 0
    b = -a
print("判断结果为: " + str(b))
# python语言以语法简洁出名, 比如说:
num = 10
res = a if num > 0 else -a
"""
练习1: 变量phone=12345678901 , 判断如果电话号码相同, 输出: 就是他, 不是输出: 下一位
练习2: 定义一个变量  var 随便一个类型的值, 判断是不是int数据类型
"""
phone = 15136282191
if phone == 15136282191:
    print("就是他")
else:
    print("下一位")
# 可以使用type()来判断是否为int类型
var = 123
if type(var) == int:
    print("是int类型")
else:
    print("不是int类型")
