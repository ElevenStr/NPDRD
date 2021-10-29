subtypeList = ['H1N1','H9N2','H3N2','H7N9','H5N1','H6N6','H5N6','H6N2']

fread = open('isolateHostClassLocationRankedByTimeHostDetail-6ForAsia.txt','r')
lines = fread.readlines()
fread.close()
dictSubtypeHostNum = dict()
for i in range(len(lines)):
    if i > 0:
        line = lines[i].rstrip()
        info = line.split('\t')
        host = info[1]
        subtype = info[3]
        if subtype in subtypeList:
            if subtype in dictSubtypeHostNum:
                if host in dictSubtypeHostNum[subtype]:
                    dictSubtypeHostNum[subtype][host] = dictSubtypeHostNum[subtype][host] + 1
                else:
                    dictSubtypeHostNum[subtype][host] = 1
            else:
                dictSubtypeHostNum[subtype] = dict()
                dictSubtypeHostNum[subtype][host] = 1

for subtype in subtypeList:
    fwrite = open('HostNumFor'+subtype+'.txt','w')
    fwrite.write('host\tnum\n')
    for host in dictSubtypeHostNum[subtype]:
        fwrite.write(host + '\t' + str(dictSubtypeHostNum[subtype][host]) + '\n')
    fwrite.close()

