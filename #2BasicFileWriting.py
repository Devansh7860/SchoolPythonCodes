myfile = open(r"C:/Users/PRATEEK/OneDrive/Desktop/school codes/textfilerandom2.txt" , 'w')
# WRITING METHODS-----------
   # if something is already there in the file .. it will get replaced.. 
   # if file doesn't exist new file by that name will be created and then data will be added.
'''
for i in range(2):
    name = input("enter name")
    myfile.write(name)  # writes a single string value at a time
    myfile.write('\n')  # if we don't give \n then all names will be added without any space between them
'''


'''
l = []
for i in range(2):
    name = input("enter name")
    l.append(name+"\n")
myfile.writelines(l)  # writes a list of value

'''

'''
for i in range(2):
    name = input("enter name")
    marks = input("enter marks")
    rec = marks+name+'\n'
    myfile.write(rec)
'''
myfile.close()























