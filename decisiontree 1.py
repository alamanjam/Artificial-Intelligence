import math, csv, random
from collections import deque
answers = []
alldata = []
tree = []
right = 0
wrong = 0
class Node:
    def __init__(self, val):
        self.value = val
        self.type = type
        self.freqs = dict()
        self.children = {}
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


def inputdata(file, size):
    datacols = []
    datarows = []
    data = []
    with open(file, 'r') as f:
        datareader = csv.reader(f, delimiter=',')
        data = list(datareader)
    tempdata = data
    global colnames
    colnames = []
    colnames = data[0]
    data.pop(0)
    data = [x for x in data if "?" not in x]
    random.shuffle(data)
    datarows = data[0:size]
    global alldata
    alldata = data[size:]
    for i in tempdata:
        if "?" in i:
            alldata.append(i)
    colnames.pop(0)
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
    index = 0
    bestentropylist = []
    bestfreqs = dict()
    bestcolname = ""
    bestindex = 0
    for i in datacols:
        freqs = dict()
        entropylist = []
        colname = colnames[index]
        index +=1
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
                freqs[x] = optionfreqs
            for k in columnfreqs:
                if len(k) != len(answers):
                    for j in answers:
                        if j in k:
                            pass
                        else:
                            k[j] = 0
            for op in columnfreqs:
                freq = list(op.values())
                entropylist.append(freq)
            entropy = avgentropy(entropylist)
            if entropy < lowestentropy:
                lowestentropy = entropy
                bestcol = i
                bestentropylist = entropylist
                bestfreqs = freqs
                bestcolname = colname
                bestindex = index-1
    return bestcol, bestfreqs, bestindex, bestcolname

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

def readTree(tree, row):
    global right, wrong
    questions = dict()
    if len(tree.children) is 0:
        return tree.value
    else:
        i = colnames.index(tree.value)+1
        response = alldata[row][i]
        if response == "?":
            for i in tree.children:
                value = readTree(tree.children[i], row)
                if value in questions:
                    questions[value] += 1
                else:
                    questions[value] = 1

            answer = max(questions, key=lambda key:questions[key])
            return answer
        if response in tree.children.keys():
            tree = tree.children[response]
            x = readTree(tree, row)
            return x
def make_tree(ds, level, node):
    global count
    datacols = ds[1]
    best = bestcolumn(ds)
    bestcol = best[0]
    freqs = best[1]
    index = best[2]
    colname = best[3]
    node.value = colname
    #print("---"*level, colname, "?")
    for val in list(set(bestcol)):
        newds = extract(ds, val, index+1)
        answertemp = newds[1][-1]
        if(len(set(answertemp))) == 1:
            node.children[val] = Node(answertemp[0])
           # print("---" * level + ">", val, answertemp[0])
        else:
            temp = Node("")
            node.children[val] = temp
            node.children[val].freqs = freqs[val]
            #count += 1
            #print("---" * level + ">" + val + str(node.children[val].freqs))
            make_tree(newds, level+1, temp)
    return node
def majorfreq(node):
    sum = 0
    t = 0
    sum = 0
    for j in node.freqs.values():
        sum += j
    for k in node.freqs.keys():
        t = node.freqs[k]/sum
        if  t >= 0.95:
            return k
    return None

def prune_tree(tree):
    global count
    queue = deque()
    queue.append(tree)
    while len(queue) is not 0:
        curr = queue.popleft()
        if len(curr.freqs.keys()) > 1:
            major = majorfreq(curr)
            if major is not None:
                curr.children = {}
                curr.value = major
                #curr.children.append(Node(major))
        else:
            count += 1
            for i in curr.children:
                queue.append(curr.children[i])

for k in range(5, 105, 5):
    count = 1
    right = 0
    wrong = 0
    for i in range(0, 100):
        ds = None, None
        tree = Node(None)
        ds = inputdata('perceptron.csv', k)
        tree = make_tree(ds, 1, tree)
        #prune_tree(tree)
        for i in range(0, len(alldata)):
            answer = readTree(tree, i)
            if answer == alldata[i][len(alldata[i]) - 1]:
                right += 1
            else:
                wrong += 1
    alldata = []
    datacols = []
    #print(str(k) + "\t" + str((count)))
    print(str(k) + "\t" + str(right/(wrong+right)))
