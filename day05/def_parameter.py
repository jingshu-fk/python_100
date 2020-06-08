#!/bin/bash
##############################################################
# File Name: 
# Version: V1.0
# Author: shujingping
# Organization: https://www.cnblogs.com/jinggs/
# Created Time : 2020-06-02 16:11:59
# Description:
##############################################################

from random import randint


# 可以给函数有个默认参数值
def roll_dice(n=2):
	'''摇色子'''
	total = 0
	for _ in range(n):
		total += randint(1, 6)
	return total


#print(roll_dice())

print(roll_dice(5))

#不知道具体多少参数化，可以用*args
def add(*args):
	total = 0
	for val in args:
		total += val
	return total

print(add(1,34,5))




