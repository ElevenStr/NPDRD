import numpy as np
import matplotlib.pyplot as plt

fread = open('TypeMatrix.txt', 'r')
lines = fread.readlines()
fread.close()
# dictIJSimilarity = {}
InterTypeSimilarity = []
for i in range(len(lines)):
    line = lines[i].rstrip()
    info = line.split('\t')
    # dictIJSimilarity[i] = {}
    for j in range(i):
        InterTypeSimilarity.append(float(info[j]))
        # dictIJSimilarity[i][j] = info[j]

fread = open('IntraTypeSimilarity.txt','r')
lines = fread.readlines()
fread.close()
# dictTypeIntratypesimilarity = {}
IntraTypeSimilarity = []
for i in range(len(lines)):
    line = lines[i].rstrip()
    # dictTypeIntratypesimilarity[i] = line
    IntraTypeSimilarity.append(float(line))

IntraTypeSimilarity_mean = np.mean(IntraTypeSimilarity)
InterTypeSimilarity_mean = np.mean(InterTypeSimilarity)
IntraTypeSimilarity_std = np.std(IntraTypeSimilarity)
InterTypeSimilarity_std = np.std(InterTypeSimilarity)

print(IntraTypeSimilarity_mean,InterTypeSimilarity_mean)
print(IntraTypeSimilarity_std,InterTypeSimilarity_std)

fig = plt.figure(figsize=(10,10))

x = [0.5,0.6]
y = [IntraTypeSimilarity_mean,InterTypeSimilarity_mean]
std_err = [IntraTypeSimilarity_std,InterTypeSimilarity_std]

error_params = dict(ecolor = '0.2', capsize = 12)
plt.bar(x, y, width=0.03, color = ['blue'], yerr = std_err, error_kw = error_params, tick_label = ['IntraTypeSimilarity','InterTypeSimilarity'], alpha=0.7)
plt.ylim(0.5,)

plt.savefig('IntraInterSimilarity.pdf')