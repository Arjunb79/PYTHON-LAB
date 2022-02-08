import csv

# with open("dept.csv","w",newline='')as w:
#     csv_writer=csv.writer(w)
#     csv_writer.writerow(["amal","MCOM","alam@gmail.com"])


with open("dept.csv","r") as f:
    csv_reader=csv.DictReader(f)
    for l in csv_reader:
        print(dict(l))
