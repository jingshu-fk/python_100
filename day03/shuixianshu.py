#!/bin/bash
##############################################################
# File Name: 
# Version: V1.0
# Author: shujingping
# Organization: https://www.cnblogs.com/jinggs/
# Created Time : 2020-05-21 10:58:13
# Description:
##############################################################
'''说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。
'''
list = []
for i in range(100, 1000):
    a = i // 100
    b = (i-a*100) // 10
    c = i % 10
    if a*100+b*10+c == a*a*a + b*b*b + c*c*c:
        list.append(i)
print(list)
    
