"""
if 表达式:
    if 表达式:
        代码块
    else:
        代码块
else：
    if 表达式:
        代码块
    else:
        代码块
"""
#  例： 0-59 D, 60-79 C, 80-99 B, 100 A, 手动输入成绩
score = input("请输入你的成绩: ")
score = int(score)
if 0 <= score <= 100:
    if 0 <= score <= 59:
        print("你的成绩是D")
    elif 60 <= score <= 79:
        print("你的成绩是C")
    elif 80 <= score <= 99:
        print("你的成绩是B")
    else:
       print("你的成绩是A")
"""
运算符优先级:
    1. () 有括号先算括号里面的
    2. ** 先算指数
    3. 符号: - 负,  + 正, ~ 安位取反
    4. * / % //
    5. +加  -减
    6. <  >  <= >= 
    7. ==判断相等 !=判断不相等
    8. = 赋值, +=, -=, *=, /=, %=, **=, //=
    9. is   is not 
    10. in   not in
    11. not
    12. and
    13. or
"""
# 判断不周日的上班时间
weekday = "星期五"
if "日" not in weekday:
    print("上六休一, 今天上班")
else:
    print("今天休息")
