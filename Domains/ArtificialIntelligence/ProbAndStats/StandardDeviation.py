import math
import numpy as np

# 1
l = [1,2,3]
sd = np.std(l)

low = 0
high = 10
guess = 5
while abs(low - high) > 0.0001:
    s = np.std(l+[guess])
    if s == sd:
        break
    if s > sd:
        high = guess
        guess = low + 0.5*(guess-low)
    else:
        low = guess
        guess = high - 0.5*(high-guess)
print('{0:.2f}'.format(low))


# 2
mu = 0.675
sigma = 0.065
x = 90.25 / 100
ans = (x - mu) / sigma
print('{0:.2f}'.format(ans))


# 3
mu1 = 10
sigma1 = 3
mu2 = 20
sigma2 = 4

mu = mu1 + mu2
sigma = math.sqrt(sigma1*sigma1 + sigma2*sigma2)
print('{0:.1f}'.format(sigma))


# 4
mu = mu1 - mu2
sigma = sigma
print('{0:.1f}'.format(sigma))


# 5
# sigma doesn't change

# 6
# var' = 4*var  => sigma' = 2*sigma


