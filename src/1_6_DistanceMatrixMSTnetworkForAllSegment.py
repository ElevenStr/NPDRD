from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
import networkx as nx

# fread = open('DistanceMatrixForAllSegment.txt','r')
fread = open('DistanceMatrixForHANASegment.txt','r')
lines = fread.readlines()
fread.close()
isolateIDList = list()
dictTypeDist = {}
for i in range(len(lines)):
    line = lines[i].rstrip()
    if i > 0:
        info = line.split('\t')
        for j in range(len(info)):
            if j > 0:
                dictTypeDist[(info[0],isolateIDList[j-1])] = info[j]
    else:
        idlist = line.split('\t')
        for isolateID in idlist:
            isolateIDList.append(isolateID)

# matrixContent = []
g_data = []
for i in range(len(isolateIDList)):
    typeIndexI = isolateIDList[i]
    # arrContent = []
    for j in range(len(isolateIDList)):
        typeIndexJ = isolateIDList[j]
        if j > i:
            weight = float(dictTypeDist[(typeIndexI, typeIndexJ)])
            g_data.append((i,j,weight))
        #     arrContent.append(0)
        # elif (typeIndexI, typeIndexJ) in dictTypeDist:
        #     arrContent.append(float(dictTypeDist[(typeIndexI, typeIndexJ)]))
        # else:
        #     arrContent.append(0)
    # matrixContent.append(arrContent)

# X = csr_matrix(matrixContent)
# Tcsr = minimum_spanning_tree(X)
# MST_Array = Tcsr.toarray()
g = nx.Graph()
g.add_weighted_edges_from(g_data)
tree = nx.minimum_spanning_tree(g, algorithm='prim')
# print(tree.edges(data=True))
edges = tree.edges(data=True)

# fwrite = open('MST_IsolateIDForAsiaAllSegment.txt', 'w')
fwrite = open('MST_IsolateIDForAsiaHANASegment.txt', 'w')
fwrite.write('typeIndexI\ttypeIndexJ\tdist\n')
for edge in edges:
    i = edge[0]
    j = edge[1]
    typeIndexI = isolateIDList[i]
    typeIndexJ = isolateIDList[j]
    weight = edge[2]['weight']
    fwrite.write(typeIndexI + '\t' + typeIndexJ + '\t' + str(weight) + '\n')
# for i in range(len(isolateIDList)):
#     typeIndexI = isolateIDList[i]
#     for j in range(len(isolateIDList)):
#         if j > i:
#             typeIndexJ = isolateIDList[j]
#             if MST_Array[i][j] > 0:
#                 fwrite.write(typeIndexI+'\t'+typeIndexJ+'\t'+str(MST_Array[i][j])+'\n')
fwrite.close()
print('MSTnetwork completed...')

# print('prim to MST...')
#
# listV = isolateIDList
#
# dictMarkedV = {}
# for typeK in isolateIDList:
#     dictMarkedV[typeK] = 0
#
# def insertPriorityQueue(queueEdges, e):
#     if len(queueEdges) == 0:
#         queueEdges = [e]
#     else:
#         edgeDist = dictVertexEdgeDist[e[0]][e]
#         pos2Insert = 0
#         for eINQ in queueEdges:
#             if dictVertexEdgeDist[eINQ[0]][eINQ] < edgeDist:
#                 pos2Insert += 1
#         for eINQ in queueEdges[pos2Insert:]:
#             if dictVertexEdgeDist[eINQ[0]][eINQ] == edgeDist:
#                 pos2Insert += 1
#         queueEdges.insert(pos2Insert, e)
#
#     return queueEdges
#
# edges = dictTypeDist
# mst = []
# queueEdges = []
#
# typeIndex0 = isolateIDList[0]
#
# dictMarkedV[typeIndex0] = 1
# for (typeIndexI,typeIndexJ) in dictVertexEdgeDist[typeIndex0]:
#     if typeIndexI != typeIndex0:
#         print('Wrong dictVertexEdge...')
#         sys.exit()
#     else:
#         pass
#     queueEdges = insertPriorityQueue(queueEdges, (typeIndexI,typeIndexJ))
#
# while True:
#     print('mstLength length...', len(mst))
#     print('queueEdges length...', len(queueEdges))
#     (typeIndexI,typeIndexJ) = queueEdges[0]
#     queueEdges.remove((typeIndexI,typeIndexJ))
#
#     if dictMarkedV[typeIndexJ] == 0:
#         mst.append((typeIndexI,typeIndexJ))
#         print('J:',typeIndexI,typeIndexJ,dictVertexEdgeDist[typeIndexI][(typeIndexI,typeIndexJ)])
#         dictMarkedV[typeIndexJ] = 1
#         for eINQ in queueEdges:
#             if dictMarkedV[eINQ[1]] == 1:
#                 queueEdges.remove(eINQ)
#
#         for (typeIndexJ,typeIndexJJ) in dictVertexEdgeDist[typeIndexJ]:
#             if dictMarkedV[typeIndexJJ] == 0:
#                 #queueEdges = insertPriorityQueue(queueEdges, (typeIndexJ,typeIndexJJ))
#                 e = (typeIndexJ,typeIndexJJ)
#                 edgeDist = dictVertexEdgeDist[e[0]][e]
#                 pos2Insert = 0
#                 for eINQ in queueEdges:
#                     if dictVertexEdgeDist[eINQ[0]][eINQ] < edgeDist:
#                         pos2Insert += 1
#                 for eINQ in queueEdges[pos2Insert:]:
#                     if dictVertexEdgeDist[eINQ[0]][eINQ] == edgeDist:
#                         pos2Insert += 1
#                 queueEdges.insert(pos2Insert, e)
#
#     if len(queueEdges) == 0:
#         break
#
# fwrite = open('mst_prime_withDistForAsiaIsolateSome.txt', 'w')
# for (a,b) in mst:
#     fwrite.write(a+'\t'+b+'\t'+str(dictVertexEdgeDist[a][(a,b)])+'\n')
# fwrite.close()

