#!/bin/bash
##############################################################
# File Name: 
# Version: V1.0
# Author: shujingping
# Organization: https://www.cnblogs.com/jinggs/
# Created Time : 2020-05-19 20:20:13
# Description:
##############################################################
row = int(input('please input a number:'))
for i in range(row):
    for _ in range(i+1):
        print('*', end='')
    print(end='\n')
