import pandas as pd
from sklearn.linear_model import LinearRegression


def load_data(path):
    df = pd.read_csv(path, header=None)
    df.columns = ['charge_time', 'battery_time']
    return df


def fit_model(df):
    df1 = df[df['charge_time'] < 4.0].copy()
    mod = LinearRegression()
    mod.fit(df1.charge_time.reshape(-1, 1), df1.battery_time.reshape(-1, 1))
    return mod


def my_predict(val):
    if val < 4.0:
        return 2*val
    return 8.0


def explore():
    import matplotlib.pyplot as plt

    path = 'D:/PythonProjects/HackerRank/'
    path += 'Domains/ArtificialIntelligence/StatisticsAndMachineLearning/'
    path += 'trainingdata_laptop.txt'
    df = load_data(path)
    plt.scatter(df.charge_time, df.battery_time)
    plt.show()
    mod = fit_model(df)
    print(mod.coef_)

    test_values = [1.50, 5.7]
    test_answers = [3.00, 8.00]
    for value, answer in zip(test_values, test_answers):
        assert my_predict(value) == answer


def main():
    value = float(input())
    print(my_predict(value))


if __name__ == '__main__':
    main()
