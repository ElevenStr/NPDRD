import sys
import time

begin = time.time()

def calNucleotideSimilarity(seqi, seqj):
	if len(seqi) != len(seqj):
		sys.exit('Not equal seq lengths!')
	else:
		same = 0
		l = len(seqi)
		for k in range(len(seqi)):
			nti = seqi[k]
			ntj = seqj[k]
			if nti == ntj:
				if nti != '-':
					same = same + 1
				else:
					l = l -1
		return float(same/l)

fread = open('../ClusterResultForAsia_MP.txt','r')
lines = fread.readlines()
fread.close()
dictTypeIsolate = {}
dictIsolateType = {}
for i in range(len(lines)):
    line = lines[i].rstrip()
    info = line.split('\t')
    type = info[1]
    if type not in dictTypeIsolate:
        dictTypeIsolate[type] = []
    for j in range(len(info)-2):
        isolateID = info[j+2]
        dictTypeIsolate[type].append(isolateID)
        dictIsolateType[isolateID] = type

print(len(dictIsolateType.keys()))

fread = open('MP_Asia.mafft.fasta','r')
dictIsolateSeq = dict()
lineNo = 0
seq = ''
for rline in fread:
    lineNo = lineNo + 1
    if rline[0] == '>':
        if lineNo > 1:
            dictIsolateSeq[isolateID] = seq
            seq = ''
        isolateID = rline[1:rline.find('|')]
    else:
        seq = seq + rline.strip()
dictIsolateSeq[isolateID] = seq
fread.close()

# print(len(dictIsolateSeq.keys()))

dictIsolateIJdistance = {}
for isolateIDi in dictIsolateType:
    # print(isolateIDi)
    if isolateIDi not in dictIsolateIJdistance:
        dictIsolateIJdistance[isolateIDi] = {}
    for isolateIDj in dictIsolateType:
        if isolateIDj not in dictIsolateIJdistance:
            dictIsolateIJdistance[isolateIDj] = {}
        if isolateIDj not in dictIsolateIJdistance[isolateIDi]:
            dictIsolateIJdistance[isolateIDi][isolateIDj] = calNucleotideSimilarity(dictIsolateSeq[isolateIDi],dictIsolateSeq[isolateIDj])
            dictIsolateIJdistance[isolateIDj][isolateIDi] = dictIsolateIJdistance[isolateIDi][isolateIDj]


dictypeMeansimilarity = {}
fwrite = open('IntraTypeSimilarity.txt','w')
for type in dictTypeIsolate:
    # print(type)
    similarity = 0
    num = 0
    for i in range(len(dictTypeIsolate[type])):
        isolateIDi = dictTypeIsolate[type][i]
        for j in range(i):
            isolateIDj = dictTypeIsolate[type][j]
            # print(isolateIDj,isolateIDj)
            similarity = similarity + dictIsolateIJdistance[isolateIDi][isolateIDj]
            num = num + 1
    if num == 0 :
        mean_similarity = 1
    else:
        mean_similarity = similarity/num
    # print(type,mean_similarity)
    dictypeMeansimilarity[type] = mean_similarity
    fwrite.write(str(mean_similarity)+'\n')

dictTypeIJdistance = {}
for typei in dictTypeIsolate:
    if typei not in dictTypeIJdistance:
        dictTypeIJdistance[typei] = {}
    for typej in dictTypeIsolate:
        if typej not in dictTypeIJdistance:
            dictTypeIJdistance[typej] = {}
        if typei != typej:
            similarity = 0
            num = 0
            for isolateIDi in dictTypeIsolate[typei]:
                for isolateIDj in dictTypeIsolate[typej]:
                    similarity = similarity + dictIsolateIJdistance[isolateIDi][isolateIDj]
                    num = num + 1
            dictTypeIJdistance[typei][typej] = similarity / num
            dictTypeIJdistance[typej][typei] = dictTypeIJdistance[typei][typej]
        else:
            dictTypeIJdistance[typei][typej] = 1

# print(dictTypeIJdistance)

fwrite = open('TypeMatrix.txt', 'w')
for typei in dictTypeIsolate:
    for typej in dictTypeIsolate:
        if typei == typej:
            fwrite.write('1' + '\t')
        else:
            fwrite.write(str(dictTypeIJdistance[typei][typej]) + '\t')
    fwrite.write('\n')
fwrite.close()

# fwrite = open('TypeSimilarity.txt','w')
# fwrite.write('cluster_type\tintra_type_similarity\tinter_type_minSimilarity\tinter_type_maxSimilarity\tinter_type_meanSimilarity\tif_inter>intra+0.01\n')
# for typei in dictTypeIsolate:
#     fwrite.write(str(typei)+'\t')
#     minsimilarity = 1
#     maxsimialrtiy = 0
#     similarity = 0
#     num = 0
#     for typej in dictTypeIsolate:
#         if typei != typej:
#             if dictTypeIJdistance[typei][typej] > maxsimialrtiy:
#                 maxsimialrtiy = dictTypeIJdistance[typei][typej]
#             if dictTypeIJdistance[typei][typej] < minsimilarity:
#                 minsimilarity = dictTypeIJdistance[typei][typej]
#             similarity = similarity + dictTypeIJdistance[typei][typej]
#             num = num + 1
#     similarity = similarity / num
#     # print(dictypeMeansimilarity[typei],minsimilarity,maxsimialrtiy)
#     fwrite.write(str(dictypeMeansimilarity[typei])+'\t'+str(minsimilarity)+'\t'+str(maxsimialrtiy)+'\t'+str(similarity)+'\t')
#     # print(dictypeMeansimilarity[type],min(dictTypeIJdistance[type].values()),max(dictTypeIJdistance[type].values()))
#     if maxsimialrtiy > dictypeMeansimilarity[typei] + 0.01:
#         fwrite.write('True\n')
#     else:
#         fwrite.write('False\n')
#
# end = time.time()
# print(end - begin)
#
# print(min(dictypeMeansimilarity.values()),max(dictypeMeansimilarity.values()))