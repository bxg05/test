# 算术运算符, 比较运算符, 逻辑运算符
"""
算术运算符: + 加  - 减     *乘      / 除
    ** 幂    // 整除   % 取余
"""
print(999 + 432)
print(88888 - 66666)
print(98 * 109)
# / 除以符号, 所得结果是浮点数
print(4 / 2)
# 2 ** 10: 就是2的十次方
print(2 ** 10)
# // : 整除符号, 取整数位
print(5 // 2)
# % : 取整除后的余数
print(5 % 2)
print(10 % 4)
"""
比较运算符(关系运算符):
    > 大于    < 小于    == 等于   <= 小于   >= 大于等于    != 不等于
    表达式的结果为布尔值: True, False
"""
print(10 > 1)
print(2 <= 2)
print(False == 1)
print(4 + 5 != 7 + 2)
"""
逻辑运算符: 
    逻辑与: and    逻辑或: or     逻辑非: not
"""
# and: 并列多个条件, 当条件同时成立结果为True, 否则为False
result = 1 < 2 and 2 > 0
print(f"结果是: {result}")
result2 = True and False
print(result2)
# or: 并列多个条件, 当其中一个条件为True结果为True, 否则为False
result3 = 4 == 3 or 4 == 4
print("判断结果: %s" % result3)
# not: 不是什么条件, 与原来条件全反; 如: a < 10, not a < 10 相当于a >= 10
print(not 8 > 9)
print(not True == 0)
print(not True, not False)
