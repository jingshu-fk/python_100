#!/bin/bash
##############################################################
# File Name: 
# Version: V1.0
# Author: shujingping
# Organization: https://www.cnblogs.com/jinggs/
# Created Time : 2020-05-26 18:53:58
# Description:
##############################################################
str1 = "hello"
str2 = "world"
str3 = "python"
print('{}\n{}\n{}'.format(str1, str2, str3))

'''
字符串
'''

str4 = "hello, world!"
#查找子串的位置
print(str4.find('or'))
print(str4.find('shit'))

#判断字符串以指定字符串开头或结尾
print(str4.startswith('He'))
print(str4.endswith('d!'))

#判断字符串是否由数字构成
print(str4.isdigit())
#判断字符串是否由字母构成
print(str4.isalpha())

#判断字符串是否由数字和字母构成
print(str4.isalnum())

str5 = " fke @3i4   "
#获得字符串去掉左右两侧的空格之后
print(str5.strip())


'''
格式化输出字符串
'''

a, b = 5,10
print('%d * %d = %d' % (a,b,a*b))

print('{0} * {1} = {2}'.format(a,b,a*b))

print(f'{a} * {b} = {a*b}')


