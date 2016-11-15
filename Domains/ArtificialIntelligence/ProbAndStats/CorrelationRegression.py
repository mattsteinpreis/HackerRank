import math
import scipy.stats as st

# 1
myx = -4/3
mxy = -3/4
sgn = myx / abs(myx)
angle_yx = math.atan(myx)
angle_xy = math.atan(mxy)
phi = abs(angle_yx - angle_xy)
r = (1 / math.cos(phi) - math.tan(phi))
print(str.format('{0:.2f}', r*sgn))


# 2
mean_P = 100
sd_P = 8
mean_X = 103
sd_S = 4
r2 = 0.4

slope_P_S = math.sqrt(r2) * sd_P / sd_S
print(str.format('{0:.2f}', slope_P_S))

# 3
'''
4x - 5y + 33 = 0
20x - 9y - 107 = 0

16y - 272 = 0
'''

y = 272/16
x = y * 5/4 - 33 / 4
print(x)
print(y)
