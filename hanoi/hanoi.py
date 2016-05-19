'''
递归实现汉诺塔
'''

__author__ = 'sankoshine'

def move(n,a,c,b):
	if n < 1:
		return
	move(n-1,a,b,c)
	print(a,c)
	move(n-1,b,c,a)

move(3,"A","C","B")