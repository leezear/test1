import csv


def minL(a):
    min_d = 10000000
    for i in a:
        min_d = min(float(i), min_d)

    return min_d


path = 'E:/Projects/benchmarks/res2/'
file_name = "test2"
res_path = path + file_name + "-summary.csv"
res_file = open(res_path, "w", newline="")
writer = csv.writer(res_file)
p = path + file_name + ".csv"

with open(p) as f:
    print(p)
    reader = csv.reader(f)
    b = 0
    for row in reader:
        # print(row)
        min_int = 100000000

        a = minL(row)
        # print(a)

        c = ''
        for i in row:
            w = b % 2
            if w == 0:
                d = round(float(i), 3)
                if i == str(a):
                    c = c + '&\\textbf{' + i + '}'
                else:
                    c = c + '&' + i
            elif w == 1:
                d = round(float(i), 4)
                if i == str(a):
                    c = c + '&\\textbf{' + str(d) + 'M}'
                else:
                    c = c + '&' + str(d) + 'M'
        b = b + 1
        c = c[1:]
        c = c + '\\\\'
        # for i in row:
        # for i in row:
        #     a = float(i);
        #     if max(row):
        # fn = row['files']
        # t = row["cpu"]
        # n = row["#nodes"]
        # if "-" in fn or "_" in fn:
        #     writer.writerow([float(t)/1000])
        #     writer.writerow([str(float(n)/1000000)+"M"])
        #     print(t)
        #     print(n)
        print(c)
        print()
f.close()
res_file.close()

# if(row[filename])

# with open(filename) as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row, reader.line_num)
# print(row, reader.line_num)
# print(list(reader))
