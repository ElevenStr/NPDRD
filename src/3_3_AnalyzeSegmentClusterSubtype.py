# segs = ['PB2','PB1','PA','NP','MP','NS']
segs = ['HA','NA']

fread = open('isolateHostClassLocationRankedByTimeHostDetail-6ForAsia.txt','r')
lines = fread.readlines()
fread.close()
dictIsolateSubtype = dict()
for i in range(len(lines)):
    line = lines[i].rstrip()
    if i > 0:
        info = line.split('\t')
        isolateID = info[0]
        subtype = info[3]
        dictIsolateSubtype[isolateID] = subtype

for seg in segs:
    fread = open('ClusterResultForAsia_'+seg+'.txt','r')
    lines = fread.readlines()
    fread.close()
    # dictClusterSubtypeNum = dict()
    dictSubtypeClusternum = dict()
    for i in range(len(lines)):
        line = lines[i].rstrip()
        info = line.split('\t')
        # if len(info) > 10:
        type = seg + '_' + str(info[1])
            # dictClusterSubtypeNum[type] = dict()
            # for j in range(len(info)):
                # if j > 1:
        isolateID = info[2]
        subtype = dictIsolateSubtype[isolateID]
        if seg == 'HA':
            subtype = subtype[0:subtype.find('N')]
        else:
            subtype = subtype[subtype.find('N'):]
        if subtype in dictSubtypeClusternum:
            dictSubtypeClusternum[subtype] = dictSubtypeClusternum[subtype] + 1
        else:
            dictSubtypeClusternum[subtype] = 1
                    # if subtype in dictClusterSubtypeNum:
                    #     dictClusterSubtypeNum[type][subtype] = dictClusterSubtypeNum[type][subtype] + 1
                    # else:
                    #     dictClusterSubtypeNum[type][subtype] = 1
    # fwrite = open('ClusterSubtypeNumFor'+seg+'.txt','w')
    f = zip(dictSubtypeClusternum.keys(), dictSubtypeClusternum.values())
    c = sorted(f)
    # print(c)
    fwrite = open('SubtypeClusternumFor'+seg+'.txt','w')
    for item in c:
        fwrite.write(item[0] + '\t' + str(item[1]) + '\n')
    fwrite.close()
    # for type in dictClusterSubtypeNum:
    #     fwrite.write(type + '\n')
    #     for subtype in dictClusterSubtypeNum[type]:
    #         fwrite.write(subtype + '\t' + str(dictClusterSubtypeNum[type][subtype]) + '\n')
    #     fwrite.write('\n')
    # fwrite.close()



