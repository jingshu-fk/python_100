#!/bin/bash
##############################################################
# File Name: 
# Version: V1.0
# Author: shujingping
# Organization: https://www.cnblogs.com/jinggs/
# Created Time : 2020-06-03 14:47:39
# Description:
##############################################################

'''
买卖股票的最佳时机
给定一个数组，它的第i个元素是一支给定股票第i天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），来计算你能获取的最大利润。
注意：你不能在买入股票前卖出股票。

[7,1,5,3,6,1,4]
max(price(j)-price(i))

1、遍历一次列表，记录每次的最低值
2、如果当天卖掉，利润profit是不是最大的
'''


def get_maxprofit(prices):
	minprice = int(1e9)	
	maxprofit = 0
	for price in prices:
		maxprofit = max(price - minprice, maxprofit)
		minprice = min(price, minprice)
	return maxprofit

if __name__ == '__main__':
	prices = [7,1,5,3,6,1,4]
	s = get_maxprofit(prices)
	print(s)	
