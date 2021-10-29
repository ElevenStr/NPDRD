from minisom import MiniSom
from sklearn.metrics import silhouette_score
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import sys

# segs = ['PB2','PB1','PA','HA','NP','NA','MP','NS']
segs = ['HA','NA']
# segs = ['HA']

isolateIDlist = []
fread = open('DMk_MP_Asia.txt','r')
lines = fread.readlines()
fread.close()
for i in range(len(lines)):
    line = lines[i].rstrip()
    isolateID = line.split('\t')[0]
    isolateIDlist.append(isolateID)

fread = open('isolateHostClassLocationRankedByTimeHostDetail-6ForAsia.txt','r')
lines = fread.readlines()
fread.close()
dictIsolateSubtype = dict()
for i in range(len(lines)):
    line = lines[i].rstrip()
    if i > 0:
        info = line.split('\t')
        isolateID = info[0]
        subtype = info[3]
        dictIsolateSubtype[isolateID] = subtype

colorJetList = ['#00008F','#00009F','#0000AF','#0000BF','#0000CF','#0000DF','#0000EF','#0000FF','#000FFF','#001FFF','#002FFF','#003FFF','#004FFF','#005FFF','#006FFF','#007FFF','#008FFF','#009FFF','#00AFFF','#00BFFF','#00CFFF','#00DFFF','#00EFFF','#00FFFF','#0FFFEF','#1FFFDF','#2FFFCF','#3FFFBF','#4FFFAF','#5FFF9F','#6FFF8F','#7FFF7F','#8FFF6F','#9FFF5F','#AFFF4F','#BFFF3F','#CFFF2F','#DFFF1F','#EFFF0F','#FFFF00','#FFEF00','#FFDF00','#FFCF00','#FFBF00','#FFAF00','#FF9F00','#FF8F00','#FF7F00','#FF6F00','#FF5F00','#FF4F00','#FF3F00','#FF2F00','#FF1F00','#FF0F00','#FF0000','#EF0000','#DF0000','#CF0000','#BF0000','#AF0000','#9F0000','#8F0000','#7F0000']
dictHtypeColor = {}
fwrite = open('HtypeColor.txt','w')
for i in range(16):
    Htype = 'H' + str(i+1)
    colorIndex = int(64/16*i)%64
    colorHere = colorJetList[colorIndex]
    dictHtypeColor[Htype] = colorHere
    fwrite.write(Htype + '\t' + colorHere + '\n')
fwrite.close()

dictNtypeColor = {}
fwrite = open('NtypeColor.txt','w')
for i in range(10):
    Ntype = 'N' + str(i+1)
    colorIndex = int(64/10*i)%64
    colorHere = colorJetList[colorIndex]
    dictNtypeColor[Ntype] = colorHere
    fwrite.write(Ntype + '\t' + colorHere + '\n')
fwrite.close()

for seg in segs:
    print('clustering for ' + seg + ' segment...')
    fread = open('DMk_' + seg + '_Asia.txt','r')
    # fread = open('Vector_' + seg + '.txt', 'r')
    lines = fread.readlines()
    fread.close()
    Eigenvector = []
    isolateIDlist = []
    for i in range(len(lines)):
        line = lines[i].rstrip()
        info = line.split('\t')
        isolateIDlist.append(info[0])
        vector = []
        for j in range(len(info)-1):
            vector.append(float(info[j+1]))
        Eigenvector.append(vector)

    X = np.array(Eigenvector)
    N = X.shape[0]
    M = X.shape[1]
    print('Eigenvector size:',N,M)
    size = math.ceil(np.sqrt(5 * np.sqrt(N)))
    print('cluster size:',size)

    sigmalist = [2,3]
    learning_rate_list = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
    neighborhood_function_list = ['bubble','triangle']
    best_parameter = (0,0,'',0)
    maxscore = 0

    for s in sigmalist:
        for l in learning_rate_list:
            for n in neighborhood_function_list:
                if s!=2 or l!=1.0 or n!='triangle':
                    continue
                # if s == 1 and (n == 'bubble' or n == 'triangle'):
                #     continue
                # print('sigma=' + str(s) + ',learning_rate=' + str(l) + ',neighborhood_function=' + n)

                for k in range(30):
                # k = 3
                    som = MiniSom(size, size, M, sigma=s, learning_rate=l,neighborhood_function=n)
                    som.pca_weights_init(X)
                    # random_data = X.copy()
                    # np.random.shuffle(random_data)
                    som.train_batch(X, N*(k+1))

                    dictTypeToIsolateID = dict()
                    dictClusterToNum = dict()
                    num = 0
                    PreLabels = list()
                    for i in range(X.shape[0]):
                        cluster = som.winner(X[i])
                        if cluster not in dictTypeToIsolateID:
                            dictTypeToIsolateID[cluster] = []
                            dictTypeToIsolateID[cluster].append(isolateIDlist[i])
                            num = num + 1
                            dictClusterToNum[cluster] = num
                            PreLabels.append(num)
                        else:
                            dictTypeToIsolateID[cluster].append(isolateIDlist[i])
                            PreLabels.append(dictClusterToNum[cluster])
                    # print(len(dictTypeToIsolateID.keys()))
                    # print(len(dictClusterToNum.keys()))
                    # print(num)
                    # print(len(PreLabels))

                    score = silhouette_score(X, PreLabels, metric='euclidean')
                    # print('the' + k + ' th clustering score:',score)

                    if score > maxscore:
                        best_parameter = (s,l,n,k+1)
                        maxscore = score
                        print('the maxscore has been updated to:', score)
                        print('now the best parameters are:', best_parameter)
                        fwrite = open('ClusterResultForAsia_'+seg+'999.txt','w')
                        for cluster in dictTypeToIsolateID:
                            fwrite.write(str(cluster) + '\t' + str(dictClusterToNum[cluster]) + '\t')
                            for id in dictTypeToIsolateID[cluster]:
                                fwrite.write(id + '\t')
                            fwrite.write('\n')
                        fwrite.close()
    print('the max silhouette_score for ' + seg + ' segment is:', maxscore)
    print('the best parameters for ' + seg + ' segment are:', best_parameter)

    plt.figure(figsize=(size, size))
    the_grid = GridSpec(size, size)
    for position in dictTypeToIsolateID:
        dictSubSubtypeNum = dict()
        num = 0
        for id in dictTypeToIsolateID[position]:
            num = num + 1
            subtype = dictIsolateSubtype[id]
            if seg == 'HA':
                SubSubtype = subtype[0:subtype.find('N')]
            else:
                SubSubtype = subtype[subtype.find('N'):]
            if SubSubtype in dictSubSubtypeNum:
                dictSubSubtypeNum[SubSubtype] = dictSubSubtypeNum[SubSubtype] + 1
            else:
                dictSubSubtypeNum[SubSubtype] = 1
        label_fracs = []
        colorslist = []
        for SubSubtype in dictSubSubtypeNum:
            label_fracs.append(dictSubSubtypeNum[SubSubtype]/num)
            if seg == 'HA':
                colorslist.append(dictHtypeColor[SubSubtype])
            else:
                colorslist.append(dictNtypeColor[SubSubtype])
        if len(label_fracs) > 1:
            print(position,'cluster wrong!')
            # sys.exit(0)
        plt.subplot(the_grid[position[1], position[0]], aspect=1)
        patches, texts = plt.pie(label_fracs,colors=colorslist)
        plt.text(position[0] / 100, position[1] / 100, str(len(dictTypeToIsolateID[position])),
                    color='black', fontdict={'weight': 'bold', 'size': 15},va='center', ha='center')
    # plt.legend(patches, dictHtypeColor.keys(), loc='upper left', bbox_to_anchor=(-9, 18), ncol=3)
    if seg == 'HA':
        plt.savefig('HAClusterResult.pdf')
    else:
        plt.savefig('NAClusterResult.pdf')
    plt.show()

