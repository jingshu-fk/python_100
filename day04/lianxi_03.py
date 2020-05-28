#!/bin/bash
##############################################################
# File Name: 
# Version: V1.0
# Author: shujingping
# Organization: https://www.cnblogs.com/jinggs/
# Created Time : 2020-05-28 15:32:36
# Description:
##############################################################
'''
设计一个函数返回给定文件名的后缀名
'''

def get_suffix(filename):
	suffix = filename.split('.')[-1]
	print(suffix)
	return suffix

if __name__ == '__main__':
	filename = 'http_post.tmp'
	get_suffix(filename)
	
	
