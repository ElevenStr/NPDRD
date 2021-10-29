fread = open('typeIndexInfoAvianDetailHostDetailForAsia.txt','r')
# fread = open('isolateHostClassLocationRankedByTimeHostDetail-6ForAsia.txt','r')
lines = fread.readlines()
fread.close()
dictSubtypeNum = dict()
for i in range(len(lines)):
    if i > 0:
        line = lines[i].rstrip()
        info = line.split('\t')
        subtype = info[7]
        if subtype in dictSubtypeNum:
            dictSubtypeNum[subtype] = dictSubtypeNum[subtype] + 1
        else:
            dictSubtypeNum[subtype] = 1

f = zip(dictSubtypeNum.values(),dictSubtypeNum.keys())
c = sorted(f,reverse=1)
# print(c)
fwrite = open('SubtypeNumForAsiaGenotype.txt','w')
for item in c:
    fwrite.write(item[1] + '\t' + str(item[0]) + '\n')
fwrite.close()

