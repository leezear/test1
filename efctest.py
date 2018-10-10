import pandas as pd
import os

if __name__ == '__main__':
    res_path = R'E:\result\EFC_exp\summary.csv'
    path = R'E:\result\EFC_exp\ac\d\BH-4-4-1537012907.csv'
    csv_data = pd.read_csv(path)
    save = pd.DataFrame(csv_data)
    # print(csv_data.shape)
    # print(save)
    # print(csv_data.columns)

    # for item in save:
    #     print(item)
    mil = 1000000
    thd = 1000
    to = 1800000
    # print(round((save['cpu'].mean() / 1000), 3))
    # print(round((save['#nodes'].mean() / 1000000), 3))
    # print(save['cpu'].count())
    # print((save['cpu'] >= to).sum())

    rss = ['0',
           round((save['cpu'].mean() / 1000), 3),
           save['cpu'].count(),
           round((save['#nodes'].mean() / 1000000), 3),
           (save['cpu'] >= to).sum()
           ]

    print(rss)

    res = pd.DataFrame()
    print(res)
    res['Instances'] = []
    res['#='] = []
    res['cpu'] = []
    res['#nodes'] = []
    res['#to'] = []

    print(res)
    # res.loc[res['Instances'] == '0'] = rss
    res.append(rss)
    # print(res.loc[0])
    print(res)