import math

segs = ['PB2','PB1','PA','HA','NP','NA','MP','NS']
listNT = ['A','T','C','G']
STOPAA = ['TAG','TAA','TGA']
codonLigal = []
for a in listNT:
    for b in listNT:
        for c in listNT:
            codon = a + b + c
            codonLigal.append(codon)

for seg in segs:
    print('calculating ' + seg + ' segment...')
    fread = open(seg + '_Asia.fasta','r')
    lines = fread.readlines()
    fread.close()
    fwrite = open('DMk_'+seg+'_Asia.txt','w')

    dictCodonPosition = dict()
    for i in range(len(lines)):
        line = lines[i].rstrip()
        if line[0] == '>':
            isolateID = line[1:line.find('|')]
            fwrite.write(isolateID + '\t')
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
                fwrite.write(str(dictCodonShannonEntropy[codon]) + '\t')
            fwrite.write('\n')

    fwrite.close()
    print(seg + ' segment has been calculated!')



