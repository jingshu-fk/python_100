'''
for-in循环
'''

# 如果明确的知道循环执行的次数或者对一个容器进行迭代。


# sum = 0
# for i in range(1, 101, 2):
# 	sum += i
# 	print(sum)
	


'''
while循环
'''

# 如果要构造不知道具体循环次数的循环结构



# 有个条件达到了就停止循环
import random

answer = random.randint(1, 100)
count = 0
while True:
	count += 1
	number = int(input('请输入一个数字：'))
	if number > answer:
		print('大了一些')
	elif number < answer:
		print('小了一些')
	else:
		print('bingo')
		break
print('你猜了%s次' % count)
if count > 5:
	print('你的智商税交多了')


