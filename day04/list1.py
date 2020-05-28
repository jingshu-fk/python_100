#!/bin/bash
##############################################################
# File Name: 
# Version: V1.0
# Author: shujingping
# Organization: https://www.cnblogs.com/jinggs/
# Created Time : 2020-05-28 10:02:54
# Description:
##############################################################
'''
列表：结构化的、非标量类型，它的值得有序序列
支持索引，可以for循环，可以[]或[:]切片
'''
list1 = [1, 3, 300, 5, 939]
#可以通过enumerate函数处理列表之后遍历同时获得元素的索引和值
for index,elem in enumerate(list1):
	print(index,elem)
#添加元素：append、insert
list1.insert(2,13)
print(list1)

#删除元素
if 3 in list1:
	list1.remove(3)

#从指定位置删除元素
list1.pop(4)
print(list1)

#清空列表元素
list1.clear()
print(list1)

#------------------------
#反向切片复制列表

fruits = ['apple', 'ipad', 'ipad pro', 'macbook air', 'macbook pro']
fruits2 = fruits[::-1]
print(fruits2)

#排序
#sorted不会修改原来的列表，没有副作用
fruits3 = sorted(fruits)
print(fruits3)

fruits4 = sorted(fruits, key=len, reverse=True)
print(fruits4)








