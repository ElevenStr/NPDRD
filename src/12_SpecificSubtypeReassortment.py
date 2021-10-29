'''
fread = open('ExtReassortModeForH6N6.txt','r')
lines = fread.readlines()
fread.close()
dictSegmentNum = dict()
num = 0
for i in range(len(lines)):
    line = lines[i].rstrip()
    if line[0] == '>':
        reassortNum = line.split('|')[1]
        targetInfo = lines[i+1].rstrip().split('\t')
        targetSubtype = targetInfo[4]
        targetCombination = list()
        for k in range(len(targetInfo)):
            if k > 6:
                targetCombination.append(targetInfo[k])
        subtypeSet = set()
        for j in range(int(reassortNum)+1):
            info = lines[i+j+1].rstrip().split('\t')
            subtype = info[4]
            subtypeSet.add(subtype)
        if targetSubtype == 'H6N2' and len(subtypeSet) == 2 and 'H6N6' in subtypeSet:
        # if targetSubtype == 'H6N2':
            num = num + 1
            GetInnerSegment = set()
            for j in range(int(reassortNum)):
                infoj = lines[i+j+2].rstrip().split('\t')
                subtypej = infoj[4]
                if subtypej == 'H6N6':
                    for k in range(len(infoj)):
                        if k > 6:
                            if infoj[k] in targetCombination:
                                segment = infoj[k].split('_')[0]
                                GetInnerSegment.add(segment)
            for segment in GetInnerSegment:
                if segment in dictSegmentNum:
                    dictSegmentNum[segment] = dictSegmentNum[segment] + 1
                else:
                    dictSegmentNum[segment] = 1
print(num)
print(dictSegmentNum)
                # fwrite.write(lines[i+j+1])
'''

'''
# subtypeList = ['H1N1','H9N2','H3N2','H7N9','H5N1','H6N6','H5N6','H6N2','H4N6']
subtypeList = ['H5N8']
# subtypeToAnalyze = 'H1N1'
fread = open('reassortmentHistroy3HostDetailForAsia.txt','r')
lines = fread.readlines()
fread.close()
for subtypeToAnalyze in subtypeList:
    fwrite = open('ExtReassortModeFor'+subtypeToAnalyze+'.txt', 'w')
    for i in range(len(lines)):
        line = lines[i].rstrip()
        if line[0] == '>':
            reassortNum = line.split('|')[1]
            subtypeSet = set()
            selfReassortment = False
            for j in range(int(reassortNum)+1):
                info = lines[i+j+1].rstrip().split('\t')
                subtype = info[4]
                subtypeSet.add(subtype)
            if subtypeToAnalyze in subtypeSet and len(subtypeSet) != 1:
                fwrite.write(lines[i]+lines[i+1])
                infoi = lines[i+1].rstrip().split('\t')
                targetCombination = list()
                for k in range(len(infoi)):
                    if k > 6:
                        targetCombination.append(infoi[k])
                for j in range(int(reassortNum)):
                    infoj = lines[i+j+2].rstrip().split('\t')
                    for k in range(len(infoj)):
                        if k < 7:
                            fwrite.write(infoj[k] + '\t')
                        else:
                            if infoj[k] in targetCombination:
                                fwrite.write(infoj[k] + '\t')
                    fwrite.write('\n')

                    # fwrite.write(lines[i+j+1])
    fwrite.close()
'''

'''
subtypeList = ['H1N1','H3N2','H4N6','H5N1','H6N6','H5N6','H5N8','H6N2','H7N9','H9N2']
# subtypeList = ['H5N8']
for subtypeToAnalyze in subtypeList:
    print('For ' + subtypeToAnalyze + ':')
    fread = open('reassortmentHistroy3HostDetailForAsia.txt','r')
    lines = fread.readlines()
    fread.close()
    dictSubtypeNum = dict()
    selfReassortNum = 0
    ReassortNumForSubtype = 0
    ReassortNumForTarget = 0
    for i in range(len(lines)):
        line = lines[i].rstrip()
        if line[0] == '>':
            reassortNum = line.split('|')[1]
            subtypeSet = set()
            TargetInfo = lines[i+1].rstrip().split('\t')
            TargetSubtype = TargetInfo[4]
            if TargetSubtype == subtypeToAnalyze:
                ReassortNumForTarget = ReassortNumForTarget + 1
            for j in range(int(reassortNum)):
                info = lines[i+j+2].rstrip().split('\t')
                subtype = info[4]
                subtypeSet.add(subtype)
            if subtypeToAnalyze in subtypeSet and len(subtypeSet) == 1:
                selfReassortNum = selfReassortNum + 1
            if subtypeToAnalyze in subtypeSet or TargetSubtype == subtypeToAnalyze:
                ReassortNumForSubtype = ReassortNumForSubtype + 1
                if TargetSubtype != subtypeToAnalyze:
                    subtypeSet.add(TargetSubtype)
                if subtypeToAnalyze in subtypeSet:
                    subtypeSet.remove(subtypeToAnalyze)
                for s in subtypeSet:
                    if s in dictSubtypeNum:
                        dictSubtypeNum[s] = dictSubtypeNum[s] + 1
                    else:
                        dictSubtypeNum[s] = 1

    f = zip(dictSubtypeNum.values(),dictSubtypeNum.keys())
    c = sorted(f,reverse=1)
    fwrite = open('reassortNumFor'+subtypeToAnalyze+'.txt','w')
    fwrite.write('reassortNum\t' + str(ReassortNumForSubtype) + '\n' + 'selfReassortNum\t' + str(selfReassortNum) + '\n' + 'reassortTarget\t' + str(ReassortNumForTarget) + '\n')
    for item in c:
        fwrite.write(item[1] + '\t' + str(item[0]) + '\n')
    fwrite.close()
    # print(c)
    print(ReassortNumForSubtype,selfReassortNum)
'''



fread = open('reassortmentHistroy3HostDetailForAsia.txt','r')
lines = fread.readlines()
fread.close()
selfReassortNum = 0
for i in range(len(lines)):
    line = lines[i].rstrip()
    if line[0] == '>':
        reassortNum = line.split('|')[1]
        subtypeSet = set()
        for j in range(int(reassortNum)):
            info = lines[i+j+2].rstrip().split('\t')
            subtype = info[4]
            subtypeSet.add(subtype)
        if len(subtypeSet) == 1:
            selfReassortNum = selfReassortNum + 1
print(selfReassortNum)


