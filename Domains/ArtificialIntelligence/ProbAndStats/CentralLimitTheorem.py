import math
import scipy.stats as st

def Z_sum(val, m, s, n):
    return (val - n*m) / math.sqrt(n) / s

def Z_mean(val, m, s, n):
    return (val - m) * math.sqrt(n) / s

def mean_from_Z(Z, m, s, n):
    return m + Z * s / math.sqrt(n)

def sum_from_Z(Z, m, s, n):
    return n*m + Z * s * math.sqrt(n)

# 1
maxW = 9800
n_box = 49
mean_box = 205
sd_box = 15

Z = Z_sum(maxW, mean_box, sd_box, n_box)
prob = st.norm.cdf(Z)
print('{0:.4f}'.format(prob))


# 2
mu = 2.4
sd = 2.0
n = 100
maxZ = 250

Z = Z_sum(maxZ, mu, sd, n)
prob = st.norm.cdf(Z)
print('{0:.4f}'.format(prob))


# 3
mu = 500
sd = 80
n = 100
min_mean = 490
max_mean = 510

Z_min = Z_mean(min_mean, mu, sd, n)
Z_max = Z_mean(max_mean, mu, sd, n)
prob = st.norm.cdf(Z_max) - st.norm.cdf(Z_min)
print('{0:.4f}'.format(prob))


# 4
n = 100
mu = 500
sd = 80

Z_low = st.norm.ppf(0.025)
Z_high = st.norm.ppf(0.975)
mean_low = mean_from_Z(Z_low, mu, sd, n)
mean_high = mean_from_Z(Z_high, mu, sd, n)
print('{0:.2f}'.format(prob_low))
print('{0:.2f}'.format(prob_high))


# 5
mu = 50000
sd = 10000
start = 74000
deliver = 47000
n = 11
finish = start + n*deliver
bought = finish - 20000

Z = Z_sum(bought, mu, sd, n)
prob = 1 - st.norm.cdf(Z) # want prob that Z is higher
print('{0:.4f}'.format(prob))


# 6
mu = 50000
sd = 10000
n = 11
start = 74000
deliver = ???
finish = start + weekly*11

Z = st.norm.ppf(0.995)
bought = sum_from_Z(Z, mu, sd, n)
finish = bought + 20000
deliver = (finish - start)/n
print('{0:.1f}'.format(deliver))