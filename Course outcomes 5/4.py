import csv
with open("dept.csv",newline='') as f:
    data=csv.DictReader(f)
    print("Name Department Age")
    print("----------------")
    for row in data:
        print(row['name'],row['dept'],row['age'])