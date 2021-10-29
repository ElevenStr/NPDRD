# fread = open('typeIndexInfoAvianDetailHostDetailForAsia.txt','r')
fread = open('isolateHostClassLocationRankedByTimeHostDetail-6ForAsia.txt','r')
lines = fread.readlines()
fread.close()
dictHostNum = dict()
for i in range(len(lines)):
    if i > 0:
        line = lines[i].rstrip()
        info = line.split('\t')
        host = info[1]
        if host in dictHostNum:
            dictHostNum[host] = dictHostNum[host] + 1
        else:
            dictHostNum[host] = 1

f = zip(dictHostNum.values(),dictHostNum.keys())
c = sorted(f,reverse=1)
# print(c)
fwrite = open('HostNumForAsiaIsolate.txt','w')
for item in c:
    fwrite.write(item[1] + '\t' + str(item[0]) + '\n')
fwrite.close()

