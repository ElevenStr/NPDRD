# fread = open('typeIndexInfoAvianDetailHostDetailForAsia.txt','r')
fread = open('isolateHostClassLocationRankedByTimeHostDetail-6ForAsia.txt','r')
lines = fread.readlines()
fread.close()
dictlocNum = dict()
for i in range(len(lines)):
    if i > 0:
        line = lines[i].rstrip()
        info = line.split('\t')
        loc = info[2]
        if loc in dictlocNum:
            dictlocNum[loc] = dictlocNum[loc] + 1
        else:
            dictlocNum[loc] = 1

f = zip(dictlocNum.values(),dictlocNum.keys())
c = sorted(f,reverse=1)
# print(c)
fwrite = open('LocNumForAsiaIsolate.txt','w')
for item in c:
    fwrite.write(item[1] + '\t' + str(item[0]) + '\n')
fwrite.close()

