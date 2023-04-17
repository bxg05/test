"""
多分支判断语句结构
if 表达式1:
    代码块1
elif 表达式2:
    代码块2
elif 表达式3:
    代码块3
...
else:
    代码块
"""
# 例如: 判断成绩的分段, 0-59不及格, 60-79 良好, 80-99 优秀, 100 太棒了
score = 70
if 0 <= score <= 59:
    print("同学, 考的不好")
elif score >= 60 and score <= 79:   #  或者  elif 60 <= score <= 79:
    print("同学, 挺好的")
elif 80 <= score <= 99:
    print("同学, 太优秀了")
elif score == 100:
    print("哇!, 你太棒了")
else:
    print("你是不是输入错误了")
