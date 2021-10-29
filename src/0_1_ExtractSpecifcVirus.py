fread = open('isolateHostClassLocationRankedByTimeHostDetail-6ForAll.txt','r')
lines = fread.readlines()
fread.close()
dictIDLocation = dict()
fwrite = open('isolateHostClassLocationRankedByTimeHostDetail-6ForAsia.txt','w')
for i in range(len(lines)):
    if i > 0:
        line = lines[i].rstrip()
        info = line.split('\t')
        isolateID = info[0]
        location  = info[2]
        dictIDLocation[isolateID] = location
        if 'Asia' in location and isolateID != '29819':
            fwrite.write(lines[i])
    else:
        fwrite.write(lines[i])


segs = ['PB2','PB1','PA','HA','NP','NA','MP','NS']
for seg in segs:
    fread = open('../' + seg + '.fasta','r')
    lines = fread.readlines()
    fread.close()
    fwrite = open(seg + '_' + 'Asia.fasta', 'w')
    for i in range(len(lines)):
        line = lines[i].rstrip()
        if line[0] == '>':
            isolateID = line[1:line.find('|')]
            if 'Asia' in dictIDLocation[isolateID] and isolateID !='29819':
                fwrite.write(lines[i])
                fwrite.write(lines[i+1])
    fwrite.close()
