#!/bin/bash
##############################################################
# File Name: 
# Version: V1.0
# Author: shujingping
# Organization: https://www.cnblogs.com/jinggs/
# Created Time : 2020-05-28 11:27:24
# Description:
##############################################################
'''
元组：一种容器数据类型，存储多个数据，元素不能修改。
'''
import sys

t = ('舒景平', 25, True, '浙江杭州')
print(sys.getsizeof(t))
print(t)
#也可以通过下标获取元素
print(t[2])

#可以遍历for循环
for num in t:
	print(num)


person = list(t)
print(sys.getsizeof(person))



















