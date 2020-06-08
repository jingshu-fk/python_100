#!/bin/bash
##############################################################
# File Name: 
# Version: V1.0
# Author: shujingping
# Organization: https://www.cnblogs.com/jinggs/
# Created Time : 2020-06-08 09:58:08
# Description:
##############################################################


'''
文件操作
'''

import time

def main():
	#一次性读取全部文件内容
	#with open('def_parameter.py', 'r', encoding='utf-8') as f:
		#f.read()是str
	#	print(f.read())

	#通过for-in循环遍历读取每一行
	#with open('made.txt', 'r', encoding='UTF-8') as f:
	#	for line in f:
	#		print(line, end='')
	
	#读取文件按行读取到列表中
	with open('made.txt', 'r', encoding='UTF-8') as f:
		#f.readlines是list
		f.readlines()
		print(type(f.readlines()))	

#直接执行该py才会运行的模块名字是__main__
if __name__ == '__main__':
	main()
