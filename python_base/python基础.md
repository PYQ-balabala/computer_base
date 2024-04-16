# 变量
变量理解为指向特定的值<br>
**变量命名规则**
* 变量名只能采用字母、数字以及下划线组成
* 只能以字母、下划线开头
* 变量名一般采用小写，单词之间用下划线隔开，应当见名知意
* 慎用小写l和大写O
* 不要将python关键字和函数名作为变量名
# 数据类型
## 字符串
在python中用引号（单引号'' 或 双引号""）括起来的都是字符串
```python
str1 = 'hello world'
str2 = "hello world"
```
这样的灵活组合是为了方便能够在字符串中组合引号和撇号<br>
**字符串常用方法**<br>
```python
str = 'test'
str = str.title() # 首字母大写，其余小写
str = str.upper() # 全大写
str = str.lower() # 全小写
```
>上述方法都是临时修改，如果要永久修改则需要将变量指向改变后的字符串<br>

**空白字符**<br>
```python
# python中空白字符包括一切控制台不直接打印的字符，包括制表符（\t）换行符（\n）
str1 = 'hello '
str2 = '\thello\t'
str3 = '\nhello\n'
# 删除空白字符方法：rstrip() 删掉右侧空白字符，strip() 删掉首尾空白字符, lstrip() 删掉左侧空白字符
str1.rstrip()
str2.strip()
str3.lstrip()
```
>上述方法用于删除右侧、首尾、左侧的空白字符，空白字符不仅是空格，还包括换行符、制表符等控制台不直接显示的字符<br>

**字符串引用变量**
```python
name = 'tom'
str1 = f'{name} is my brother' # f字符串
str2 = "{} is my brother".format(name) # format方法
str3 = "%s is my brother" % (name) # %运算符
```

上述这种方式分别称为:
* “f字符串”，用于在字符串中引用已有变量，用花括号将变量括起来；此方法适用于python 3.6及以上版本
* format方法，空的花括号表示变量要插入的位置
* %运算符, %s表示变量位置以及变量类型

## 数
**整数运算**<br>
```python
# 整数运算主要有：+、-、*、/、//、%
# 位运算主要有：&、|、!、~、>>、<<、^
a, b = 2, 3 # 一次性赋值多个变量
c = 10_000_000 # 下划线分割较大数字，python会忽略下划线
COUNT = 20 # 常量，python并未内置常量，一半将全大写变量认为是常量
print(c)
print(a * b) # 乘法运算
print(a ** b) # 幂运算
print(a / b) # 除法运算
print(a - b) # 减法运算
print(a + b) # 加法运算
print(b // a) # 整除
print(b % a) # 取模
# 位运算
print(a >> 2) # 右移2位
print(a << 2) # 左移2位
print(a & b) # 与运算
print(a | b) # 或运算
print(a ^ b) # 异或运算
print(~ a) # 按位取反
```
浮点数与整数运算一样，值得注意的是：*除法的结果总为浮点数*，有浮点数参与的运算，结果总为浮点数<br>
## 列表
**列表**由一系列按特定顺序排列的元素组成，这里的元素可以是任意元素类型和内容；由方括号括起来<br>
```python
lists = [1, 2, 3,, 4, 5] #列表定义
len(lists) # 获取列表长度
```
访问列表元素可以直接通过索引(index)访问，注意，*索引从0开始*
```python
print(lists[0])
print(lists[1])
print(lists[-1]) # 对于列表末尾元素，python提供了页数访问方法，索引-1表示最后一个元素，-2.-3依次表示倒数第二个、倒数第三个
```
**列表元素的增、删、改**
```python
lists.append(1) # 在列表末尾增加元素0
lists.insert(1, 10) # 在列表索引1处插入元素10

del lists[0] # 删除列表索引0的元素
lists.remove[1] # 删除列表中第一个元素为1的元素
a = lists.pop() # 删除列表末尾元素并将该元素作为返回值返回
b = lists.pop(1) # 删除列表中索引为1的元素，并将该元素作为返回值返回

lists[1] = 20 # 修改列表中索引1处的元素值为20
```

**列表切片**<br>
*列表切片*是将列表的的一部分作为一个新的列表，视为原列表的子集
```python
lists_1 = lists[:3] # 列表索引从0到2的切片
lists_2 = lists[1:] # 列表索引从1到列表末尾的切片
lists_3 = lists[:] # 整个列表的完整切片，可以作为列表拷贝的一种方式
lists_4 = lists[1:3] #列表索引从1~2的切片
```
**列表排序**
```python
lists.sort() # 列表排序，原列表被排序
lists.sort(reverse=True)  # 反向排序

sorted(lists) # 临时排序，原列表不变
sorted(lists, reverse=True) # 临时反向排序，原列表不变

lists.reverse() # 反转列表，原列表改变
```
**数值列表**<br>
通常需要数值列表（元素都为数字），可以通过list和range()快速产生数值列表
```python
lists = list(range(1, 5)) # range产生1~5之间的整数（不包括5）
print(lists)
lists = list(range(1, 10, 2)) # range产生1~10之间的整数，整数之间间隔为2（1、3、4、7）
```

**列表推导式**<br>
利用for循环语句快速创建列表
```python
lists = [ value ** 2 for value in range(1, 5)] # 产生列表为[1, 4, 9, 16]
```

**元组**<br>
列表是可变的，在程序执行过程中会对列表进行增、删、改等操作对原列表进行改变，但我们有时对于某些数据不希望在程序执行过程中进行修改，这是，就可以采用**元组**<br>
**元组**是不可变的，不能对声明后的元组进行修改，如果要修改只能重新定义变量
```python
a = (2, 3)
a[0] = 1 # 会报错
a = (1, 3) # 只能重新声明变量进行改变
```
## 字典
字典是由一系列*键值对*组成的动态结构，字典的值可以是任意python对象<br>
**定义字典**
```python
dict0 = {} # 定义一个空字典
dict0 =  {
    'name': 'Bob',
    'age': 0,
    } # 定义一个有元素的字典，键-值之间用冒号分割，键值对之间用逗号分隔
```
**字典增、删、改**
```python
dict0['name'] = 'Tom' # 新增一个键值对：'name': 'Tom'
dict0['name'] = 'Alice' # 修改'name'对应的值为'Alice'
del dict0['name'] # 删除name键值对
```

**遍历字典**
```python
print(dict0['name']) # 访问字典中name这个键对应的值
var = dict0.get('name', None) # 获取字典中name这个键的值，键不存在则返回None
# 遍历字典所有的键值对
for key, value in dict0.items():
    print(key, value)
# 遍历字典所有的键
for key in dict0.keys():
    print(key)
# 遍历字典中所有的值
for value in dict0.values():
    print(value)
```
**嵌套**<br>
嵌套一般是指列表和字典相互嵌套，列表字典、字典列表、字典嵌套字典、列表嵌套列表四种
```python
list_dict = [{'name': 'Tom', 'age': 18}, {'name': 'Alice', 'age': 16}] # 字典列表
dict_list = {
    'user': ['Alice', 'Bob', 'Tom'],
    'age': [61, 18, 24],
} # 列表字典
lists = [[1, 2, 3, 5,], [3, 6, 7, 8, 10]] # 列表中嵌套列表
dicts = {
    'Alice':{
       'name': 'Alice',
       'age': 16, 
    },
    'Tom':{
        'name': 'Tom',
        'age': 16,
    },
} # 字典中嵌套字典
```
# 流程控制
## if语句
**if语句**<br>
用于判断后面的的布尔表达式（紧跟在判断之后的表达式，计算结果为True或False），为True时执行冒号后缩进内容，否则不执行
```python
a = 10
if a > 0:
    print('{a} is greater than zero')
```
**if-else语句**<br>
当布尔表达式为True时执行if后跟着的缩进代码，为False时执行else后跟着的缩进代码
```python
a = -1
if a > 0:
    print('{a} is greater than zero')
else:
    print('{a} is less than zero')
```
**if-elif-else**<br>
此语句支持多个条件判定，根据需要，elif可以有很多个，if和elif中当布尔表达式为True时，则会执行对应的语句后缩进的代码，都不满足时则会执行else中的代码，注意：**else不是必要的**
```python
a = 0
if a > 0:
    print('{a} is greater than zero')
elif a == 0:
    print('{a} is equal to zero')
else:
    print('{a} is less than zero')
```
**逻辑运算符**<br>
逻辑运算符：与（and）、或（or）、非（not）<br>
逻辑运算符用于组合多个条件的结果<br>
算数比较：大于(>)，小于(<)，**等于(==)**，大于等于(>=)，小于等于(<=), 不等于(!=)<br>
算数比较符号用于比较数字的大小
```python
score = int(input("input students's score: "))
if a > 80:
    print("great")
elif a > 70 and a < 80:
    print("good")
elif a <= 70 and a >= 60:
    print('normal')
```
## 循环
### while循环
while循环是一种条件循环，当循环条件被满足时就会执行后续缩进的代码内容，当循环条件不满足时，就会退出循环<br>
特别需要注意循环体内一定要有促进循环结束的相关代码，否则就变成了死循环，大多数情况相爱，死循环不是一个好现象
```python
a = 0
while a < 10: # 只要a < 10成立就会进入循环
    print('loop, num is {a}')
    a += 1
```
### for循环
for循环常用于用于遍历一些元素，例如：列表，遍历结束时则循环结束
```python
a = [1, 2, 3, 4, 5]
for i in a: # 遍历a列表中的所有元素
    print(i)
```
### 循环控制
**braak与continue**<br>
break: 结束当前循环<br>
contiue: 结束当次循环，直接进入下一次循环
```python
for i in range(1, 100):
    if i > 50:
        print(i)
        break # 结束当前循环，执行循环体后面的语句
    elif i % 2 == 0:
        print('{i} is good num')
    else:
        continue # 进入下一次循环
print('done')
```
