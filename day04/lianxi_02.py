#!/bin/bash
##############################################################
# File Name: 
# Version: V1.0
# Author: shujingping
# Organization: https://www.cnblogs.com/jinggs/
# Created Time : 2020-05-28 14:19:05
# Description:
##############################################################
'''
设计一个函数产生指定长度的验证码，验证码由大小写字母及数字构成
'''

import random
import sys

def generate(length):
	str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
	identify = ''
	for i in range(length):
	#	str_info = random.choice(str)
	#	identify += str_info
		index = random.randint(0,len(str)-1)
		identify += str[index]
	print(identify)
	return identify

if __name__ == '__main__':
	length = int(input('please input the length of identify:'))
	generate(length)
		
