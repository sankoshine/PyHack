'''
杨辉三角，使用generator
'''

__author__ = 'sankoshine'

def triangles():
	l = [1]
	while True:
		g = [1,1]
		for i in range(len(l)-1):
			g.insert(-1,l[i]+l[i+1])
		yield(g)
		l = g


n = 0
for t in triangles():
	print(t)
	n = n + 1
	if n == 10:
		break
