#!/bin/bash
##############################################################
# File Name: 
# Version: V1.0
# Author: shujingping
# Organization: https://www.cnblogs.com/jinggs/
# Created Time : 2020-06-08 10:24:49
# Description:
##############################################################
'''
w——会覆盖掉文件已有内容
'''

def main():
	filenames = 'made.txt'
	with open(filenames, 'w', encoding='utf-8') as f:
		f.write('舒景平真是个大帅哥')
		#f.close()

		

main()
