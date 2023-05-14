myfile = open(r"C:/Users/PRATEEK/OneDrive/Desktop/school codes/textfilerandom.txt" , 'a')
# APPENDING-----------
    # it basically adds data in a file after the preexisting data.
'''   
for i in range(2):
    name = input("Enter your name please")
    des = input("Enter about your self")
    rec = name+des+"\n"
    myfile.write(rec)
'''
myfile.close()
