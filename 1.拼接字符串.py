# 字符串拼接
# 1. 使用 + 拼接字符串
print(123456789 + 987654321)

print("你好" + "明天")
print("你好", "明天")
string = "刘备" + "皇叔"
print(string)
name = "羽生结弦"
project = "花滑"  # project：项目
say = name + "练" + project + "\n\t--" + "一生悬命"
print(say)
monkey = "孙悟空"
age = 88888
money = 3.21
# age是int 类型, 只能拼接字符串, 不能拼接数字型
# TypeError: can only concatenate str (not "int") to str
print(monkey + str(age) + str(money))

# 2. 使用占位符, %s, %d, %f
print("""
    姓名: %s
    年龄: %d
    盘缠: %f
""" % (monkey, age, money))

# 3. 使用format(), 函数拼接
hero = "戚继光"
# 海瑞: 海青天
shiji = "抗倭(小日本)"
# 1) .format()
print("{}  主要事迹: {}".format(hero, shiji))
# 2) 使用形参, 传入实参拼接
print("英雄: {hero}, 事迹: {sj}".format(sj=shiji, hero=hero))
# 3) 3.6版本后, 在字符串前使用f
print(f"{hero}, {shiji}")
