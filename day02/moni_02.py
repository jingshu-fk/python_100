#!/bin/bash
##############################################################
# File Name: 
# Version: V1.0
# Author: shujingping
# Organization: https://www.cnblogs.com/jinggs/
# Created Time : 2020-05-19 20:05:16
# Description:最大公约数和最小公倍数
##############################################################
a = int(input('请输入一个正整数：'))
b = int(input('请输入第二个正整数：'))

if a > b:
    a, b = b, a

for i in range(a, 2, -1):
    if a % i == 0 and b % i == 0:
        print('最大公约数为{}'.format(i))
        print('最小公倍数为{}'.format(a // i * i * (b // i)))
        break
