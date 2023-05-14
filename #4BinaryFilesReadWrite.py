# BINDARY FILES METHODS------
import pickle #module to read and write in binary files
record = []

def write():
    f = open('data.dat' , 'wb') # wb = write binary
    while True:
        name = input("enter name")
        clas = input("enter class")
        roll = int(input("enter roll no."))
        data = [name , clas , roll]
        record.append(data)
        ch = input("Y for yes \n N for no")
        if ch == "N":
            break;
    pickle.dump(record , f) # dump is basically used to write data
    f.close()
def read():
    f = open('data.dat' , 'rb') # rb = read binary
    r = pickle.load(f) # load is used to read data 
    for i in r:
        print(i)
    f.close()

write()
print("Data entered succesfully.....")
read()
print("Data read succesfully.......")

    
