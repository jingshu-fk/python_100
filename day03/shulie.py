#!/bin/bash
##############################################################
# File Name: 
# Version: V1.0
# Author: shujingping
# Organization: https://www.cnblogs.com/jinggs/
# Created Time : 2020-05-22 09:23:00
# Description:
##############################################################
'''
斐波那契数列：
1,1,2,3,5,8,13,21...

an+2 =an +an+1
输出前20个数
'''

list = [1, 1]
for i in range(18):
	a = list[i] + list[i+1]
	list.append(a)
print(len(list))
print(list)

