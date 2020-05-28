#!/bin/bash
##############################################################
# File Name: 
# Version: V1.0
# Author: shujingping
# Organization: https://www.cnblogs.com/jinggs/
# Created Time : 2020-05-28 14:12:18
# Description:
##############################################################
import os
import time
def main():
	content = "杭州欢迎你为你开天辟地......"
	while True:
		os.system('clear')
		print(content)
		time.sleep(1)
		content = content[1:] + content[0]
if __name__ == '__main__':
	main()



