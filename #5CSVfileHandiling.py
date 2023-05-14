# CSV FILE HANDLING--------------

import csv

def write():
    record = []
    with open('data.csv' , 'w' , newline='') as f:
        obj = csv.writer(f)
        obj.writerow(["Roll no." , "Name" , "Marks"]) # we enter data in  the form of lists
        while True:
            name = input("enter name")
            marks = int(input("enter marks"))
            roll = int(input("enter roll no."))
            data = [roll , name , marks]
            record.append(data)
            ch = input("Y for yes\n N for no")
            if ch == "N":
                break
        obj.writerows(record)  # multiple records at a time .. writerow adds one record at a time

def read():
    with open('data.csv' , 'r') as f:
        obj = csv.reader(f)
        for i in obj:
            print(i)

write()
read()
        
        
        
