def printStatus(cloud):
    '''
        This Functions prints the status of Different Clouds
    '''
    for i in range(3):
        print("Cloud {}".format(i+1))
        for instance, num in cloud[str(i+1)].items():
            print("Instance Type: {}, Instance Remainin: {}".format(instance, num))

def CloudInfo(initialize=True, Cloud=None):
    if initialize:
        cloud = {}
        for i in range(3):
            cloud[str(i+1)] = {}
            cloud[str(i+1)]['t2micro'] = 15
            cloud[str(i+1)]['t2nano'] = 17
            cloud[str(i+1)]['t2small'] = 12
            cloud[str(i+1)]['t2medium'] = 7
            cloud[str(i+1)]['t2large'] = 6
        # print(cloud)
        printStatus(cloud)
        return cloud
    else:
        printStatus(Cloud)
        return Cloud


# cloud = {}
# cloud = CloudInfo(initialize=True, Cloud=cloud)