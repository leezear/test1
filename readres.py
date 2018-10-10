import csv
import os

path = 'E:/Projects/benchmarks/res2/lmx/d/'
files = os.listdir(path)
res_path = path + "summary.csv"
res_file = open(res_path, "w", newline="")
writer = csv.writer(res_file)
time_limit = 1800000
for file in files:
    p = path + file
    bm_name = file[0: file.rfind("-")]
    if "summary.csv" not in file and "-" in file:
        with open(p) as f:
            # print(p)
            reader = csv.DictReader(f)
            ts = 0
            ns = 0
            i = 0
            to = 0
            for row in reader:
                fn = row['files']
                t = row["cpu"]
                n = row["#nodes"]
                if n is not None and n != '':
                    # print(fn, t, n)
                    if float(t) > time_limit:
                        to += 1
                    ts += float(t) / 1000
                    ns += float(n) / 1000000
                    i += 1
            print(bm_name)
            print(i, ts / i, ns / i)
            writer.writerow([bm_name, "cpu", str(round(ts / i, 4))])
            writer.writerow(["#=" + str(i), "#asgs", str(round(ns / i, 6)) + "M"])
            writer.writerow(["", "#out", str(to)])
        f.close()
res_file.close()

# if(row[filename])

# with open(filename) as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row, reader.line_num)
# print(row, reader.line_num)
# print(list(reader))
