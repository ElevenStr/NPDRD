# segs = ['HA','NA']
segs = ['HA']

fread = open('isolateHostClassLocationRankedByTimeHostDetail-6ForAsia.txt','r')
lines = fread.readlines()
fread.close()
dictIDtoSubtype = dict()
for i in range(len(lines)):
    line = lines[i].strip()
    info = line.split('\t')
    if i > 0:
        isolateID = info[0]
        subtype = info[3]
        dictIDtoSubtype[isolateID] = subtype


for seg in segs:
    print(seg)
    fread = open('ClusterResultForAsia_' + seg + 'Size10.txt', 'r')
    dictIDtoCluster = dict()
    subtypeWrongNumCluster = 0
    for rline in fread:
        info = rline.rstrip().split('\t')
        clusterNo = info[1]
        subtypeSet = set()
        for i in range(len(info)):
            if i > 1:
                isolateID = info[i]
                subtype = dictIDtoSubtype[isolateID]
                if seg == 'HA':
                    subtypeDetailed = subtype[:subtype.find('N')]
                else:
                    subtypeDetailed = subtype[subtype.find('N'):]
                subtypeSet.add(subtypeDetailed)
                if len(subtypeSet) > 1:
                    print(subtypeSet,clusterNo,isolateID,subtypeDetailed)
                dictIDtoCluster[isolateID] = clusterNo
        if len(subtypeSet) > 1:
            subtypeWrongNumCluster = subtypeWrongNumCluster + 1
            print(clusterNo)
            print(subtypeSet)
    fread.close()

