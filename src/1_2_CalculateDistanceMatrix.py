import math
# import sys
segs = ['PB2','PB1','PA','HA','NP','NA','MP','NS']
# segs = ['PB2']
for seg in segs:
    print(seg + '...')
    fread = open('DMk_'+seg+'_Asia.txt','r')
    lines = fread.readlines()
    fread.close()
    dictDistanceMatrix = dict()
    IDlist = list()
    for i in range(len(lines)):
        line1 = lines[i].rstrip()
        info1 = line1.split('\t')
        isolateID1 = info1[0]
        IDlist.append(isolateID1)
        if isolateID1 not in dictDistanceMatrix:
            dictDistanceMatrix[isolateID1] = dict()
        for j in range(i):
            line2 = lines[j].rstrip()
            info2 = line2.split('\t')
            isolateID2 = info2[0]
            if isolateID2 not in dictDistanceMatrix:
                dictDistanceMatrix[isolateID2] = dict()
            distance = 0
            for k in range(61):
                distance = distance + math.pow(float(info1[k+1]) - float(info2[k+1]), 2)
            distance = math.sqrt(distance)
            if distance == 0.0 and isolateID1 != isolateID2:
                distance = 1e-6
            dictDistanceMatrix[isolateID1][isolateID2] = distance
            dictDistanceMatrix[isolateID2][isolateID1] = distance
        if i%100 == 0:
            print('calculated in :', i)

    fwrite = open('DistanceMatrixFor'+seg+'.txt','w')
    for isolateID in IDlist:
        fwrite.write(isolateID + '\t')
    fwrite.write('\n')
    for isolateID1 in IDlist:
        fwrite.write(isolateID1 + '\t')
        for isolateID2 in IDlist:
            if isolateID1 == isolateID2:
                fwrite.write('0' + '\t')
            else:
                fwrite.write(str(dictDistanceMatrix[isolateID1][isolateID2]) + '\t')
        fwrite.write('\n')
    fwrite.close()


