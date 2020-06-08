#!/bin/bash
##############################################################
# File Name: 
# Version: V1.0
# Author: shujingping
# Organization: https://www.cnblogs.com/jinggs/
# Created Time : 2020-06-08 10:43:38
# Description:
##############################################################


import json

def main():
	data = {'name':'舒景平',
		'age':25,
		'num':17,
		'forhphy':77}
	try:
		with open('data.json', 'w', encoding='UTF-8') as f:
			#json.dump()是将内容序列化，并写入文件
			json.dump(data, f)
	except IOError as e:
		print(e)
	print('数据转换成json文件完成')

main()



def main_test():
	data = {"ID": "2", "IP":"12.12.12.12", "Port": "3000"}
	#json.dumps()是将内容序列化，转为json格式的字符串
	xu = json.dumps(data)
	print(xu, isinstance(xu, str))


main_test()
