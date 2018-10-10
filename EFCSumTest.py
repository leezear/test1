import pandas as pd
import os

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

rss = {'Instances': '0',
       '#=': save['cpu'].count(),
       'cpu': round((save['cpu'].mean() / 1000), 3),
       '#node': str(round((save['#nodes'].mean() / 1000000), 3)) + 'M',
       '#to': (save['cpu'] >= to).sum()
       }

rsl = ['0',
       save['cpu'].count(),
       round((save['cpu'].mean() / 1000), 3),
       str(round((save['#nodes'].mean() / 1000000), 3)) + 'M',
       (save['cpu'] >= to).sum()
       ]

print(rss)
print(rsl)

res = pd.DataFrame(columns=('Instances', '#=', 'cpu', '#nodes', '#to'))
# print(res)
print(res)
# res.loc[res['Instances'] == '0'] = rss
# res.append(rss, ignore_index=True)
# res.append(rss, ignore_index=True)
# # print(res.loc[0])

# res.loc[res.shape[0] + 1] = {rss}
# res = pd.concat(rsl, ignore_index=True)
# res.loc[res['Instances'] == '0'] = rss
# res.loc[res.shape[0]] = rss
# res.loc[res.shape[0]] = rss
# res.loc[res['Instances'] == rss['Instances'].index] = rss
# rss['Instances'].isin(res['Instances'])
# print((res['Instances'] == rss['Instances']).index.tolist()[0])
idxs = res[res['Instances'] == rss['Instances']].index.tolist()
# (res['Instances'] == rss['Instances']).index.tolist()

print(idxs)
res.loc[res.shape[0]] = rss
print(res)

idxs = res[res['Instances'] == "0"].index.tolist()

print(idxs)

# if len(idxs) == 0:
#     print('empty')
#     res.loc[res.shape[0]] = rss
# else:
#     print(idxs[0])
#     idx = idxs[0]
#     res.loc[idx] = rss
#
# # idxs = (res['Instances'] == '1').index.tolist()
# idxs = res['Instances'].index('1')
# print(idxs)
#
# if len(idxs) == 0:
#     print('empty')
#     res.loc[res.shape[0]] = rss
# else:
#     print(idxs[0])
#     idx = idxs[0]
#     res.loc[idx] = rss

# res.loc[res['Instances'] == rss['Instances']] = rss
# print(res.loc[res['Instances'] == rss['Instances']])
# print((res['Instances'] == rss['Instances']).index.tolist()[0])
# for i in range(5):
#     df.loc[i] = [randint(-1, 1) for n in range(3)]
