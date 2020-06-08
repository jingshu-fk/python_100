#!/bin/bash
##############################################################
# File Name: 
# Version: V1.0
# Author: shujingping
# Organization: https://www.cnblogs.com/jinggs/
# Created Time : 2020-06-04 09:53:20
# Description:
##############################################################


'''
排序列表，插入一个元素，在列表中找到目标值，返回其索引。
[1,3,5,6,9]
'''

def insert_index(list1, target):
	left = 0
	right = len(list1)-1
	while left < right:
		mid = (left + right) // 2
		if target == list1[mid]:
			return mid
		elif target < list1[mid]:
			right = mid - 1
		else:
			left = mid + 1
	return left
if __name__ == '__main__':
	print(insert_index([1,3,5,8,14], 14))
