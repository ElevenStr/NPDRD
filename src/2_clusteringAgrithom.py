from minisom import MiniSom
from sklearn.metrics import silhouette_score
import numpy as np
import math

segs = ['PB2','PB1','PA','HA','NP','NA','MP','NS']
# segs = ['HA','NA']

isolateIDlist = []
fread = open('DMk_MP_Asia.txt','r')
lines = fread.readlines()
fread.close()
for i in range(len(lines)):
    line = lines[i].rstrip()
    isolateID = line.split('\t')[0]
    isolateIDlist.append(isolateID)

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
    # size = math.ceil(np.sqrt(5 * np.sqrt(N)))
    size = 10
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
                        print('the maxscore has been updated to:',score)
                        print('now the best parameters are:',best_parameter)
                        fwrite = open('ClusterResultForAsia_'+seg+'Size10.txt','w')
                        for cluster in dictTypeToIsolateID:
                            fwrite.write(str(cluster) + '\t' + str(dictClusterToNum[cluster]) + '\t')
                            for id in dictTypeToIsolateID[cluster]:
                                fwrite.write(id + '\t')
                            fwrite.write('\n')
                        fwrite.close()

    print('the max silhouette_score for ' + seg + ' segment is:',maxscore)
    print('the best parameters for ' + seg + ' segment are:', best_parameter)




