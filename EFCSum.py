import numpy as np
import pandas as pd
import os

mil = 1000000
thd = 1000
to = 1800000

path = R'E:\result\EFC_exp'
res_path = R'E:\result\EFC_summary'
algs = os.listdir(path)
summary = R'summary.csv'

dit = {'ac': 'AC3^{bit}', 'efc': 'EFC^{bit}',
       'fc': 'FC^{bit}', 'lmx': 'lMaxRPC^{bit}',
       'rpc': "rRPC3", 'd': 'dom', 'wd': "dom/wdeg"}

dit_idx = {'ac': 2, 'efc': 0,
           'fc': 1, 'lmx': 3,
           'rpc': 4, 'd': 'dom', 'wd': "dom/wdeg"}

for alg in algs:
    heus_path = os.path.join(path, alg)
    if os.path.isdir(heus_path):
        print(dit[alg])
        heus = os.listdir(heus_path)
        print(heus_path)

        for heu in heus:
            print(dit[heu])
            heu_path = os.path.join(heus_path, heu)
            print(heu_path)
            files = os.listdir(heu_path)
            sum_path = os.path.join(res_path, alg + '-' + heu + '-summary.csv')
            res = pd.DataFrame(columns=('Instances', '#=', 'cpu', '#nodes', '#to'))
            print(sum_path)

            # 查找所有的csv文件
            for f in files:
                # print(f)
                # 获取类名
                file_class = f[0:f.rfind('-')]
                f_path = os.path.join(heu_path, f)
                print(file_class, f_path)
                csv_bm = pd.read_csv(f_path)
                save = pd.DataFrame(csv_bm)

                rss = {'Instances': file_class,
                       '#=': save['cpu'].count(),
                       'cpu': save['cpu'].mean(),
                       '#nodes': save['#nodes'].mean(),
                       '#to': (save['cpu'] >= to).sum()}
                print(rss)
                idxs = res[res['Instances'] == rss['Instances']].index.tolist()

                if len(idxs) == 0:
                    # 不在
                    res.loc[res.shape[0]] = rss
                else:
                    # 在
                    idx = idxs[0]
                    res.loc[idx] = rss

            res.to_csv(sum_path, index=False)
