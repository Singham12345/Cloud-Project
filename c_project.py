import pandas as pd
import numpy as np

count = 0
def userInfo():
    global count
    print('Choose your type of process & number of procese')
    type = ['prs','type','CPUs','RAM(GB)']
    print(type[0],type[1],type[2],type[3])
    p1 = ['t2nano',1,0.5]
    p2 = ['t2macro',1,1]
    p3 = ['t2small',1,2]
    p4 = ['t2medium',2,4]
    p5 = ['t2large',2,8]
    print('t1',p1[0],p1[1],p1[2])
    print('t2',p2[0],p2[1],p2[2])
    print('t3',p3[0],p3[1],p3[2])
    print('t4',p4[0],p4[1],p4[2])
    print('t5',p5[0],p5[1],p5[2])

    dta = pd.read_csv('data.csv',header=None)

    print('log in Here')

    users = dta.iloc[:,0].values


    name = input('Enter your name ')
    flag=0
    for i in users:
        if name==i:
            flag=1
            break
    if flag==1:
        instance = input("Enter type of instance ")
        num_instance = int(input("Enter number of instance "))
        pid = count
        count+=1
        return name, pid, instance, num_instance
    else:
        print("Invalid User")

# count=0
# userInfo()
