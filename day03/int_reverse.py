#!/bin/bash
##############################################################
# File Name: 
# Version: V1.0
# Author: shujingping
# Organization: https://www.cnblogs.com/jinggs/
# Created Time : 2020-05-21 13:45:20
# Description:
##############################################################
'''
正整数反转
'''

num = input('please input a number:')
list=[]
for x in range(len(num)):
    list.append(num[x])
# 2, 4, 7,8,1 ---->> 1,8,7,4,2
for i in range(0, (len(list)//2+len(list)%2)):
    list[i], list[len(list)-i-1] = list[len(list)-i-1], list[i]
print(str(list))


'''
字符串是不可变的，可以通过下标获取值但无法改变。可以重新赋值
'''


'''
解法2：24781
num > 0
1、获取到最后一位L1
2、剔除掉最后一位的剩余M1继续获取最后一位L2，第一步的L1加上L2组合
3、重复进行




