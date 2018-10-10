import csv
import os

path = 'E:/Projects/benchmarks/res2/cfc/d/'
files = os.listdir(path)
res_path = path + "statistic-summary.csv"
res_file = open(res_path, "w", newline="")
writer = csv.writer(res_file)
time_limit = 1800000
i = 0
for file in files:
    p = path + file
    bm_name = file[0: file.rfind("-")]
    if "summary.csv" not in file and "-" in file:
        with open(p) as f:
            # print(p)
            reader = csv.DictReader(f)
            ts = 0
            ns = 0
            to = 0
            print(bm_name)
            for row in reader:
                fn = row['files']
                t = row["cpu"]
                n = row["#nodes"]
                if n is not None and n != '':
                    writer.writerow([t])
                    i = i + 1
        f.close()
        print(bm_name+"--subtotal = ", i)
res_file.close()
print("total = ", i)
