#!/bin/bash
##############################################################
# File Name: 
# Version: V1.0
# Author: shujingping
# Organization: https://www.cnblogs.com/jinggs/
# Created Time : 2020-06-02 19:59:34
# Description:
##############################################################

'''
输入：[1,8,6,2,5,4,8,3,7]
输出：49


1、先两端是index值最大，m1
2、两端较小的数向中间移动，即下标索引向中间移动，要么是left+=1,要么是right-=1，获取m2
3、比较两次的m1,m2,得出max(m1,m2)
'''

'''

'''


def max_container(x):
	left = 0
	right = len(x)-1
	area = 0
	#不知道具体循环做几次，用while，用下标去做循环判定
	while left < right:
		#第一次左端和右端的area
		cur = min(x[left], x[right]) * (right - left)
		area = max(area, cur)
		if x[left] < x[right]:
			left += 1
		else:
			right -= 1

	return area

if __name__ == '__main__':
	x=[12,8,17,2,5,4,8,3,2]
	print(max_container(x))


