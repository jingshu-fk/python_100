#!/bin/bash
##############################################################
# File Name: 
# Version: V1.0
# Author: shujingping
# Organization: https://www.cnblogs.com/jinggs/
# Created Time : 2020-06-04 10:37:08
# Description:
##############################################################


def get_index(list1, target):
	entry = True
	if target == None:
		entry = False
		print('目标值不能为空')
	if entry == True:
		list1.append(target)
		print(list1)
		list1.sort()
		return list1.index(target)


print(get_index([1,3,7,10,21],None))

			
