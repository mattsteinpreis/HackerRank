#!/bin/python3

s, t = [int(i) for i in input().split()]
a, b = [int(i) for i in input().split()]
m, n = [int(i) for i in input().split()]
a_on_house = sum([1 for i in input().split()
                  if s <= a + int(i) <= t])
b_on_house = sum([1 for i in input().split()
                  if s <= b + int(i) <= t])

print(a_on_house)
print(b_on_house)
