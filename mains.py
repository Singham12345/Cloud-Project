from cloud_info import CloudInfo
from c_project import userInfo
import schedluer

count = 0

cloud=CloudInfo(initialize=True)
for i in range(4,5):
    name, pid, instance_type, num_instance = userInfo()
    # print(name,pid,instance_type,num_instance)
    cloud = schedluer.Scheduling(name, pid, instance_type, num_instance, cloud)
    # print(cloud)
    cloud = CloudInfo(initialize=False, Cloud=cloud)
    count+=1    



