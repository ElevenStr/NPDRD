segs = ['PB2','PB1','PA','HA','NP','NA','MP','NS']

dictSegIsolateCluster = dict()

for seg in segs:
	print(seg)
	fread = open('ClusterResultForAsia_'+seg+'.txt', 'r')

	dictIsolateCluster = dict()
	clusterNo = 0
	for rline in fread:
		info = rline.rstrip().split('\t')
		clusterNo = info[1]
		for i in range(len(info)):
			if i > 1:
				isolateID = info[i]
				# print(isolateID)
				dictIsolateCluster[isolateID] = clusterNo

	dictSegIsolateCluster[seg] = dictIsolateCluster
	fread.close()

fwrite = open('isolatesCombinationsHostDetailForAsia.txt', 'w')
fread = open('isolateHostClassLocationRankedByTimeHostDetail-6ForAsia.txt', 'r')
lineNo = 0
dictIsolateCombination = dict()

for rline in fread:
	lineNo += 1
	#isolateID	host_Classification	Continet_detail	subtype	year
	if lineNo > 1:
		lrline = rline.strip().split('\t')
		isolateID = lrline[0]
		fwrite.write(rline.strip()+'\t')
		combination = []
		for seg in segs:
			clusterNo = dictSegIsolateCluster[seg][isolateID]
			clusterName = seg+'_'+str(clusterNo)
			fwrite.write(clusterName+'\t')
			combination.append(clusterName)
		fwrite.write('\n')
		dictIsolateCombination[isolateID] = tuple(combination)
	else:
		fwrite.write(rline.strip()+'\t'+'PB2\tPB1\tPA\tHA\tNP\tNA\tM1\tNS1\n')

fread.close()
fwrite.close()

s = set(dictIsolateCombination.values())
print(len(s), 'combinations for ', len(dictIsolateCombination), 'strians...' )


