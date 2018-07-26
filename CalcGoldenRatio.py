import sys
from decimal import *

try:
	scale = int(input("精度を入力: "))
	if scale < 1:
		print("1以上の整数を入力してください")
		sys.exit()
	
except ValueError:
	print("整数を入力してください")
	sys.exit()

getcontext().prec = scale + 3
x = Decimal("1")
memo = Decimal("0")

while x != memo:
	memo = x
	x = (x + Decimal("1")).sqrt()

print("1.")
disp = str(x)[2:]
cnt_char = 0
cnt_space = 0
for i in range(scale):
	
	if cnt_char == 10:
		cnt_char = 1
		if cnt_space == 9:
			cnt_space = 0
			print()
		else:
			cnt_space += 1
			sys.stdout.write(" ")
	else:
		cnt_char += 1
	
	sys.stdout.write(disp[i])