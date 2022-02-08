import csv
field_name=['No','name','age']
fields=[{"No":"1","name":"Arjun","age":"21"},
        {"No":"2","name":"Arun","age":"20"},
        {"No":"3","name":"thomas","age":"41"},]


with open("5-csv.csv","w",newline='') as f:
    w=csv.DictWriter(f,fieldnames=field_name)
    w.writeheader()
    w.writerows(fields)