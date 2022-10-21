import csv
with open('sample.xlxs','w',newline="") as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['F_name','L_name', 'Email'])
    thewriter.writerow(['John', 'Doe', 'john-doe@bogusemail.com'])
    thewriter.writerow(['marry','john','profof@gmail.com'])
    print("write the information to the sample.csv")
with open('sample.csv','r') as f1:
    theread = csv.reader(f1)
    for line in theread:
        print(line)
