# 习题纠正
##### 2022-11-05
----

## 2-5

> 原本代码：

```python
 print('The Truman Show once said,"The world may be full of cheating, however wenever lack friends with a warm heart."')

correcting: wenever to whenever
```


## 2-6
> 原本代码：

```python
famous_person = "The Truman Show"
quote = "The world may be full of cheating, however wenever lack friends with a warm heart."
print(famous_person + "once said," + quote)

```
```python
运行结果：
The Truman Showonce said,The world may be full of cheating, however wenever lack friends with a warm heart.

correcting: 1.wenever to whenever  
            2. quote里面的最好这么写(加 \" , 详情搜索转义字符)：
quote = "\"The world may be full of cheating, however wenever lack friends with a warm heart.\""
            3. 逗号之后要空格，写英文要养成习惯
```

## 2-10

> 原本代码：

```python
#你最喜欢的数字是6
num = input("my favorite number is: ")
print('你将会获得%s个苹果'%(num))

```
```python

这个问题倒不大，就是要搞明白注释到底是用来干什么的： 一般是用来给别人看你的代码提供方便，说明每一步你都在干什么；或者作为title 标明代码的时间，作者，作用等信息
```
>例：

```python
# Mia 2022-11-05  number
num = input("my favorite number is: ") # input number
print('你将会获得%s个苹果'%(num)) # print number

```
## 习题2

>最后是最让宝头疼的练习题2：
>我把标准的代码敲在下面了，不能看懂来问我

> 在这里大致讲一下：map函数是独立的，这里map的作用是将float映射到input里面让输入的数字是一个浮点形式，如果不想用，可以用下面的注释替代
> math.pi 是说把 math库里的pi这个数引入
> '%.4f'% 这个应该不陌生，以前宝学过
```python

import math 

r,h = map(float,input().split(","))
#r,h=input().split(",")
#r = float(r)
#h = float(h)
area = r * r * math.pi
volume = area * h
print('%.4f'%area)
print('%.4f'%volume)


```