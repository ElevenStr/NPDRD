import math

# segs = ['PB2','PB1','PA','HA','NP','NA','MP','NS']
# segs = ['PB2','PB1','PA','NP','MP','NS']
segs = ['HA','NA']
listNT = ['A','T','C','G']
STOPAA = ['TAG','TAA','TGA']
codonLigal = []
for a in listNT:
    for b in listNT:
        for c in listNT:
            codon = a + b + c
            codonLigal.append(codon)

dictIsolateVector = dict()
for seg in segs:
    print('calculating ' + seg + ' segment...')
    fread = open(seg + '_Asia.fasta','r')
    lines = fread.readlines()
    fread.close()

    dictCodonPosition = dict()
    for i in range(len(lines)):
        line = lines[i].rstrip()
        if line[0] == '>':
            isolateID = line[1:line.find('|')]
        else:
            for a in listNT:
                for b in listNT:
                    for c in listNT:
                        codon = a + b + c
                        if codon not in STOPAA:
                            dictCodonPosition[codon] = list()
                            dictCodonPosition[codon].append(0)
            # print(dictCodonPosition)
            #计算每个三元组出现的位置
            for j in range(len(line)-2):
                if j%3 == 0:
                    codon = line[j:j+3]
                    if codon not in codonLigal or codon in STOPAA:
                        break
                    else:
                        dictCodonPosition[codon].append(j+1)

            #计算间隔和部分和
            dictCodonGap = dict()
            dictCodonPartialSum = dict()
            for codon in dictCodonPosition:
                poslist = dictCodonPosition[codon]
                dictCodonGap[codon] = list()
                dictCodonPartialSum[codon] = list()
                for k in range(len(poslist)-1):
                    alpha = 1 / (poslist[k+1] - poslist[k])
                    dictCodonGap[codon].append(alpha)
                    partialSum = 0
                    for gap in dictCodonGap[codon]:
                        partialSum = partialSum + gap
                    dictCodonPartialSum[codon].append(partialSum)

            #计算香农熵
            dictCodonShannonEntropy = dict()
            for codon in dictCodonPartialSum:
                partialSumlist = dictCodonPartialSum[codon]
                sum = 0
                for partialSum in partialSumlist:
                    sum = sum + partialSum
                ShannonEntropy = 0
                for partialSum in partialSumlist:
                    probability = partialSum / sum
                    ShannonEntropy = ShannonEntropy - probability * math.log2(probability)
                dictCodonShannonEntropy[codon] = ShannonEntropy

            for codon in dictCodonShannonEntropy:
                if isolateID in dictIsolateVector:
                    dictIsolateVector[isolateID].append(dictCodonShannonEntropy[codon])
                else:
                    dictIsolateVector[isolateID] = list()
                    dictIsolateVector[isolateID].append(dictCodonShannonEntropy[codon])
    print(seg + ' segment has been calculated!')

print(len(dictIsolateVector['22355']))

# fwrite = open('DMk_Asia.txt','w')
fwrite = open('DMk_AsiaForHANASegment.txt','w')
for isolateID in dictIsolateVector:
    fwrite.write(isolateID + '\t')
    for feature in dictIsolateVector[isolateID]:
        fwrite.write(str(feature) + '\t')
    fwrite.write('\n')
fwrite.close()


