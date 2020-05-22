#!/bin/bash
##############################################################
# File Name: 
# Version: V1.0
# Author: shujingping
# Organization: https://www.cnblogs.com/jinggs/
# Created Time : 2020-05-21 17:24:33
# Description:
##############################################################
'''
玩家摇两个骰子，点数和为7和11，玩家胜；点数和为2、3、11，庄家胜；其他继续
点数和为第一次的点数，玩家胜；点数和为7，庄家胜；其他继续，知道钱输光
'''

import random

money = 100
count = 0
# 产生随机数
ran_num = random.randint(1,6) + random.randint(1,6)
if ran_num == 7 or ran_num == 11:
	money += 10
	count += 1
	print('本轮玩家胜，加10')
elif ran_num ==2 or ran_num == 3 or ran_num == 12:
	money -= 10
	count += 1
	print('本轮庄家胜，减10')
else:
	print('go on')
	while money > 0:
		ran_num2 = random.randint(1,6) + random.randint(1,6)
		if ran_num2 == ran_num:
			money += 10
			count += 1
			print('第二轮玩家胜，加10')
		elif ran_num2 == 7:
			money -= 10
			count += 1
			print('第二轮庄家胜，减10')
		else:
			print(money)
	print('你已经输光了')
	print('总共猜了{}'.format(count))

