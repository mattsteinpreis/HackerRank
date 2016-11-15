import scipy.stats as st

# 1
mu = 2.5
X = 5

prob_X = st.poisson.pmf(k=5, mu=2.5)
print('{0:.3f}'.format(prob_X))


# 2

def cost(coef, x):
    return coef[0]+coef[1]*x*x

mu_X = 0.88
mu_Y = 1.55

# E[x] = var[x] = mean[x]
# E[C(x)] = E(160 + 40*x^2) = 160 + 40 * E[x^2]
#                           = 160 + 40 * (Var(x) + E[x]^2)
#                           = 160 + 40 * (Var(x) + Var(x) ^ 2)

E_cost_X = 160 + 40 * (mu_X + mu_X*mu_X)
E_cost_Y = 128 + 40 * (mu_Y + mu_Y*mu_Y)
print('{0:.3f}'.format(E_cost_X))
print('{0:.3f}'.format(E_cost_Y))


# 3
mu = 3

prob_1 = st.poisson.pmf(k=0, mu = mu)

prob_gt2 = 1
prob_gt2 -= st.poisson.pmf(k=0, mu = mu) * st.poisson.pmf(k=0, mu=mu)
prob_gt2 -= st.poisson.pmf(k=0, mu=mu) * st.poisson.pmf(k=1, mu=mu) * 2
print('{0:.3f}'.format(prob_1))
print('{0:.3f}'.format(prob_gt2))


# NO 4


# 5
mu = 1.2
# (1)
prob = st.poisson.pmf(k=2, mu=mu)
print('{0:.3f}'.format(prob))
#(2)
prob = 1 - st.poisson.cdf(k=2, mu=mu)
print('{0:.3f}'.format(prob))
#(3)
mu_10 = 10*mu
prob = st.poisson.pmf(k=5, mu=mu_10)
print('{0:.3f}'.format(prob))
#(4)
mu_40 = 40*mu
prob = 1 - st.poisson.cdf(k=2, mu=mu_40)
print('{0:.3f}'.format(prob))

