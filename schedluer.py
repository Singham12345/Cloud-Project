import cloud_info                                  #  Ruhela's module  for clud information
import pickle as pk
from c_project import userInfo
from cloud_info import CloudInfo

class User_Process:
    User_ID=""
    Process_ID=0
    cloud=""
    instance=""
    number=0

def Save(object):
    file1=open("ProcessInfo","rb")
    data=pk.load(file1)
    file1.close()
    data.append(object)

    file2=open("ProcessInfo",'wb')
    pk.dump(data,file2)
    file2.close()

def Scheduling(uid,Pid,instance_type,num_instance, cloud):
    # cloud=CloudInfo(initialize=False, Cloud=cloud)                             #   calling for clouds information
    # print(cloud)
    process=User_Process()

    process.User_ID=uid
    process.Process_ID=Pid
    process.number=num_instance
    process.instance=instance_type

    cloud1=cloud["1"]
    cloud2=cloud["2"]
    cloud3=cloud["3"]
    # print("asmdfhgasdkh")
    # print(cloud1, cloud2, cloud3)
    # print(instance_type)
    if(cloud1[instance_type]>=cloud2[instance_type] and cloud1[instance_type] >= cloud3[instance_type]):
        cloud1[instance_type]=cloud1[instance_type]-num_instance
        cloud_new={"1":cloud1,"2":cloud2,"3":cloud3}
        process.cloud="1"
        # Save(process)
        return cloud_new

    elif(cloud2[instance_type]>=cloud1[instance_type] and cloud2[instance_type] >= cloud3[instance_type]):
        cloud2[instance_type]=cloud2[instance_type]-num_instance
        cloud_new={"1":cloud1,"2":cloud2,"3":cloud3}
        process.cloud = "2"
        # Save(process)
        return cloud_new

    elif(cloud3[instance_type]>=cloud1[instance_type] and cloud3[instance_type] >= cloud2[instance_type]):
        cloud3[instance_type]=cloud3[instance_type]-num_instance
        cloud_new={"1":cloud1,"2":cloud2,"3":cloud3}
        process.cloud = "3"
        # Save(process)
    # print(cloud_new)
        return cloud_new
