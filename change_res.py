import csv

path = 'E:/Projects/benchmarks/res2/rrpc/wd/'
file_name = "qa_test-1523114067"
res_path = path + file_name + "summary.csv"
res_file = open(res_path, "w", newline="")
writer = csv.writer(res_file)
p = path + file_name + ".csv"

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
        if "-" in fn or "_" in fn:
            writer.writerow([float(t)/1000])
            writer.writerow([str(float(n)/1000000)+"M"])
            print(t)
            print(n)
f.close()
res_file.close()

# if(row[filename])

# with open(filename) as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row, reader.line_num)
# print(row, reader.line_num)
# print(list(reader))
