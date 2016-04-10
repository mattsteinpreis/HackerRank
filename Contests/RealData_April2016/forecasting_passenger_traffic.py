import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
from scipy.optimize import brute


def auto_arima(ts):

    def objfunc(order, x):
        mod = ARIMA(x, order)
        try:
            mod = mod.fit(disp=0)
        except ValueError:
            return 1e6
        return mod.aic

    grid = (slice(0, 3, 1), slice(0, 3, 1), slice(0, 3, 1))
    res = brute(objfunc, grid, args=[ts], finish=None)
    best_order = [int(i) for i in res]
    best_model = ARIMA(ts, best_order).fit(disp=0)
    pred = best_model.predict(60, 71, typ='levels')
    return pred


def test():
    f = open(u'D:/PythonProjects/HackerRank/Contests/RealData_April2016/traffic.txt', 'rb')
    raw = f.read().splitlines()
    n_cases = int(raw[0])
    targets = []
    for i in range(n_cases):
        case = raw[i+1].split()
        val = float(case[1])
        targets.append(val)

    # # mean
    # mn = sum(targets) / len(targets)
    # for i in range(12):
    #     print(int(mn))

    predictions = auto_arima(targets)
    print(predictions)



def hacker_rank():
    n_cases = int(input())
    targets = []
    for i in range(n_cases):
        case = input().split()
        val = float(case[1])
        targets.append(val)
    predictions = auto_arima(targets)
    for pred in predictions:
        print(int(pred))

if __name__ == "__main__":
    hacker_rank()