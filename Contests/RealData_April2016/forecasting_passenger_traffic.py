import matplotlib.pyplot as plt

def test():
    f = open(u'D:/PythonProjects/HackerRank/Contests/RealData_April2016/traffic.txt', 'rb')
    raw = f.read().splitlines()
    n_cases = int(raw[0])
    targets = []
    for i in range(n_cases):
        case = raw[i+1].split()
        val = float(case[1])
        targets.append(val)
    mn = sum(targets) / len(targets)
    for i in range(12):
        print(int(mn))

def hacker_rank():
    n_cases = int(input())
    targets = []
    for i in range(n_cases):
        case = input().split()
        val = float(case[1])
        targets.append(val)
    mn = sum(targets) / len(targets)
    for i in range(12):
        print(int(mn))

if __name__ == "__main__":
    hacker_rank()