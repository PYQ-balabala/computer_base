"""
字符串：使用双引号或单引号括起来
字符串中使用变量: f字符串
制表符: \t 换行符 \n 制表符、换行符与普通的空格一样, 都被python视为空白, 都可以用下面的函数去掉, python中空白泛指任意非打印字符
strip(): 去除首尾空白 rstrip(): 去除尾部空白 lstrip(): 去除首部空白
f字符串: 花括号内部使用变量
删除前缀: removeprefix()方法
删除后缀: removesuffix()方法
大小写: title() -- 首字母大写, 其余全小写 upper() -- 全大写, lower() -- 全小写
上述的删除都是临时的, 不会改变变量本身指向的值, 如果要改变变量指向的值, 需要把处理后的字符串重新赋值给变量
"""
a = "hello"
b = 'Hello'
print(a, b)

c = f"{a}, python"
print(c)
a = "\nhello"
print(a)
print(a.strip())
url = 'https://www.baidu.com'
print(url.removeprefix('https://'))
print(url.removesuffix(".com"))

a = 'tOny'
print(a.title())
print(a.lower())
print(a.upper())