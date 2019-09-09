import csv

# newline = "" writes the data in next line, otherwise one blank line, will be created
with open('nan.csv','w',newline='') as emp:
    w = csv.writer(emp)
    w.writerow(["Eno","Ename"])
    w.writerow(["123","manish"])
    