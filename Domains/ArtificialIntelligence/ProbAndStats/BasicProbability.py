from fractions import Fraction

def FindFraction(x):
    exp = 1000
    while exp < 1e10:
        f = Fraction(x).limit_denominator(exp)
        n = f._denominator
        d = f._denominator
        if x == n/d:
            return f
        exp *= 10
    return f

# 1
'''
In a single toss of 2 fair (evenly-weighted) 6-sided dice, find the
probability of that their sum will be at most 9.
'''

def prob_two_dice(n):
    diff = abs(n - 7)
    return (6 - diff) / 36

print(1 - (prob_two_dice(10) + prob_two_dice(11) + prob_two_dice(12)))


# 2
'''
In a single toss of 2 fair (evenly-weighted) 6-sided dice, find the
probability of that their sum will be at most 9.
'''
prob_unequal_6 = 0.8  # 1,5; 2,4; !3,3; 4,2; 5,1;
print(prob_unequal_6 * prob_two_dice(6))

# 3
'''
X: 4 red, 3 black
Y: 5 red, 4 black
Z: 4 red, 4 black

One ball is drawn from each urn. What is the probability that the 3 balls
drawn consist of 2 red balls and 1 black ball?
'''
def px(x, y):
    return x / (x+y)

t = 7*9*8
f = (4*5*4) + (4*4*4) + (3*5*4)
print(f/t)
print('{}/{}'.format(f,t))


# 4
'''
X: 4 red, 5 black
Y: 3 red, 7 black
Draw one from X, two from Y. Find Prob(2 black and 1 red).
'''

tot = 9 * 10 * 9
f  = 5*7*3  # BBR
f += 5*3*7  # BRB
f += 4*7*6
prob = f/tot
print(FindFraction(prob))



# 5
'''
10 people sit in a circle; 2 specific people X, Y.
Prob(X and Y sat next to each other).

Prob(X) sits somewhere is 1.
Find Prob(Y sits next to X) = 1 - Prob(Y sits in one of 7 other seats)
                            = 1 - 7/9
                            = 2/9
'''

# 6
'''
X: 5 W, 4 B
Y: 7 W, 6 B

Draw 1 from X (don't look); put in Y. Draw 1 from Y.
Find Prob(B).
'''

prob = 5/9 * 6/14 + 4/9*7/14
print(FindFraction(prob)) # 29/63


# 7
'''
A: 500 units/day, 0.005 defective output
B: 1000 units/day, 0.008 defective output
C: 2000 units/day, 0.010 defective output
Find Prob(pipe from A | pipe is defective)
'''

prob_x_A = 0.005
prob_A = 500 / 3500
prob_x = (500*0.005 + 1000*0.008 + 2000*0.010) / 3500

prob_A_x = prob_x_A * prob_A / prob_x
print(FindFraction(prob_A_x))

# 8
p_notM = 0.5
p_notE = 0.4
p_ME = 0.2

p_E = 1 - p_notE
p_M = 1 - p_notM
p_MorE = p_E + p_M - p_ME
print(p_MorE)
print(FindFraction(p_MorE))


# 9
'''
A: 12 candidates
B: 15 candidates
C: 10 candidates
Prob(at least 1)
'''

prob_A = 1/12
prob_B = 1/15
prob_C = 1/10

prob_none = (1-1/12)*(1-1/15)*(1-1/10)
prob_atleast1 = 1 - prob_none
print(prob_atleast1)
print(FindFraction(prob_atleast1))


# 10
'''
Two vacancies.
Find prob only one.
'''
p_bill = 1/3
p_nina = 1/5

#independent since two vacancies
prob_both = p_bill*p_nina
prob_neither = (1-p_bill)*(1-p_nina)
prob_only1 = 1 - prob_neither - prob_both
print(prob_only1)
print(FindFraction(prob_only1))