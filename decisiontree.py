import math, csv, random
colnames = []
answers = []
tree = []
datarows = []
def entropy(l):
    e1 = 0
    e = []
    total = sum(l)
    totale = 0
    for i in l:
        if(i == 0):
            e1 = 0
        else:
            e1 = i/total * math.log(i/total, 2)
        totale += e1
    return -(totale)


def avgentropy(freqs):
    total = 0
    for i in freqs:
        total += sum(i)
    avg = 0
    for i in freqs:
        avg += sum(i)/total * entropy(i)
    return avg


def inputdata(file):
    datacols = []
    with open(file, 'r') as f:
        datareader = csv.reader(f, delimiter=',')
        data = list(datareader)
    for i in data:
        if "?" not in i :
            datarows.append(i)
    global colnames
    colnames = datarows[0]
    colnames.pop(0)
    datarows.pop(0)
    print(datarows[4])
    #datarows = random.sample(datarows, size)
    temp = []
    for i in range(0, len(colnames)+1):
        for j in range(0, len(datarows)):
            temp.append(datarows[j][i])
        datacols.append(temp)
        temp = []
    datacols.pop(0)
    global answers
    answers = list(set(datacols[len(datacols)-1]))
    return datarows, datacols


def bestcolumn(ds):
    datacols = ds[1]
    finalstates = datacols[len(datacols) - 1]
    datacols.pop(len(datacols)-1)
    lowestentropy = 100
    bestcol = []
    for i in datacols:
        if len(i) != 0:
            columnfreqs = []
            options = set(i)
            for x in options:
                optionfreqs = dict()
                for j in range(0, len(i)):
                    if i[j] == x:
                        answer = finalstates[j]
                        if answer not in optionfreqs.keys():
                            optionfreqs[answer] = 1
                        else:
                            optionfreqs[answer] += 1
                columnfreqs.append(optionfreqs)
            for k in columnfreqs:
                if len(k) != len(answers):
                    for j in answers:
                        if j in k:
                            pass
                        else:
                            k[j] = 0
            entropylist = []
            for op in columnfreqs:
                freq = list(op.values())
                entropylist.append(freq)
            entropy = avgentropy(entropylist)
            if entropy < lowestentropy:
                lowestentropy = entropy
                bestcol = i
    return bestcol


def extract(ds, val, index):
    newdsrows = []
    newdscols = []
    for i in ds[0]:
        if val == i[index]:
            newdsrows.append(i)
    temp = []
    for i in range(1, len(colnames)+1):
        for j in range(0, len(newdsrows)):
            if i != index:
                temp.append(newdsrows[j][i])
        newdscols.append(temp)
        temp = []
    return newdsrows, newdscols

def readTree(input):
    input.pop(0)
    answer = input[len(input)-1]
    currentlevel =[]
    currindex = ""
    col = ""
    for i in range(1, len(tree)):
        index = -1
        for j in tree:
            if j[0] == str(i):
                if "?" in j:
                    currentlevel.append([j])
                    index+=1
                else:
                    currentlevel[index].append(j)
        for k in currentlevel:
            leaf = currindex[3:]
            if leaf in answers:
                if leaf == answer:
                    return True
                else:
                    return False
            if i == 1:
                col = k[0][3:-1]
                index = colnames.index(col)
                ans = input[index]
                for x in range(1, len(k)):
                    if k[x][3] == ans:
                        currindex = tree[tree.index(k[x]) + 1]
            else:
                if currindex in k:
                    col = currindex[3:-1]
                    index = colnames.index(col)
                    ans = input[index]
                    for x in range(1, len(k)):
                        if k[x][3] == ans:
                            currindex = tree[tree.index(k[x]) + 1]
                else:
                    pass
        currentlevel = []

def make_tree(ds, level, node):
    datacols = ds[1]
    bestcol = bestcolumn(ds)
    index = datacols.index(bestcol)
    colname = colnames[index]
    tree.append(str(level) + ": " + colname + "?")
    print("---"*level, colname, "?")
    for val in list(set(bestcol)):
        newds = extract(ds, val, index+1)
        answertemp = newds[1][-1]
        if(len(set(answertemp))) == 1:
            tree.append(str(level) + ": " + val)
            tree.append(str(level + 1) + ": " + answertemp[0])
            print("---" * level + ">", val, answertemp[0])
        else:
            tree.append(str(level) + ": " + val)
            print("---" * level + ">" + val)
            make_tree(newds, level+1, tree)

ds = inputdata('house-votes-84.csv')
make_tree(ds, 1, tree)
print(tree)
trues = 0
falses = 0
for i in range(0, len(datarows)):
    if readTree(datarows[i]) == True:
        trues +=1
    else:
        falses +=1
print(trues)
print(falses)
tree = []

