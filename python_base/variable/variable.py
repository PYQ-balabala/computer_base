"""
变量: 指向具体值的标签
可以包含数字、字母和下划线
不能以数字开头, 不能包含空格
变量命名要简洁明了、见名知意
如果存在变量修改, 则变量始终指向最新的值
注释: 以"#"开头， 三引号括起来的是docstring
"""
message = 'hello world'
print(message)
message = 'hello python'
print(message)
# 同时给多个变量赋值
a, b, c = 1, 2, 3
print(f"{a=} {b=} {c=}")
"""
常量: python没有内置常量, 通常全大写的变量视为常量, 在整个程序过程中不能修改
"""
MAX_CONN = 65535
print(f"{MAX_CONN=}")
name = 'tom'
str1 = f'{name} is my brother' # f字符串
str2 = "{} is my brother".format(name) # format方法
str3 = "%s is my brother" % (name) # %运算符
print(str1, str2, str3)
 