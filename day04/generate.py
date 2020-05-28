#!/bin/bash
##############################################################
# File Name: 
# Version: V1.0
# Author: shujingping
# Organization: https://www.cnblogs.com/jinggs/
# Created Time : 2020-05-28 11:16:00
# Description:
##############################################################
'''
生成式和生成器
'''
import sys
f = [x + y for x in 'ABDE' for y in '1234567']
print(f)

f1 = [x ** 2 for x in range(1,10)]
print(f1)

#查看对象占用内存的字节数
print(sys.getsizeof(f1))


'''
下面代码创建的不是一个列表而是一个生成器对象
通过生成器可以获取到数据但它不占用额外的空间存储数据
每次需要数据的时候就通过内部的运算得到数据（需要花费额外的时间）
'''

f2 = (x ** 2 for x in range(1,10))
print(sys.getsizeof(f2)) #生成器节省了空间存储，相比生成式
print(f2)
for val in f2:
	print(val) # 但是获取里面的数据需要再运算，花费额外的时间


