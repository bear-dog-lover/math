import math
import matplotlib.pyplot as plt
import numpy as np
import random

def dist_for_origin (x, y):
	return math.sqrt(x**2 + y**2)

circle_x = np.arange(0, 1, 0.001)
# mathパッケージのsqrtを用いるとエラー
circle_y = np.sqrt(1 - circle_x**2)
plt.plot(circle_x, circle_y)

n = int(input("精度を入力: "))

cnt_in = 0
cnt_out = 0

for i in range(n):
	x = random.uniform(0.0, 1.0)
	y = random.uniform(0.0, 1.0)
	if dist_for_origin(x, y) < 1:
		cnt_in += 1
	else:
		cnt_out += 1
	plt.plot(x, y, "ko")

print("πの近似値: " + str(cnt_in / (n / 4)))
plt.show()