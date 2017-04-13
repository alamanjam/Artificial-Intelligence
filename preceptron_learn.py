import numpy as np
from numpy import *
import itertools
import random
import time
global count
count = 0
def genFuncs(inputs):
    all_data = []
    curr_data = []
    boshal = (["".join(seq) for seq in itertools.product("01", repeat=inputs)])
    snowshal = (["".join(seq) for seq in itertools.product("01", repeat=2**inputs)])
    for i in snowshal:
        for j in range(0, len(boshal)):
            temp = []
            for k in boshal[j]:
                temp.append(k)
            temp.append(1)
            row = (array(temp, dtype = 'int')), int(i[j])
            curr_data.append(row)
        all_data.append(curr_data)
        curr_data = []
    return all_data, snowshal
def makeTrainingSet(size):
    all_data = []
    curr_data = []
    boshal = (["".join(seq) for seq in itertools.product("01", repeat=10)])
    for i in range(0, len(boshal)):
        temp = []
        for j in boshal[i]:
            temp.append(j)
        temp.append("1")
        row = array(temp, dtype= "int"), majority(temp)
        curr_data.append(row)
        all_data.append(curr_data)
        curr_data = []
    random.shuffle(all_data)
    return all_data[size:], all_data[0:size]
def majority(input):
   ones = input.count('1')-1
   zeros = len(input) - (ones+1)
   if ones > zeros:
       return 1
   else:
       return 0
def test(inputs, size):
    global right
    test_data = makeTrainingSet(size)
    training_set = test_data[1]
    test_data = test_data[0]
    right = 0
    weights = array([0 for i in range(0, inputs + 1)], dtype='int')
    for x in range(0, 100):
        for i in training_set:
            for j in i:
                result = function(dot(weights, j[0]))
                if result != j[1]:
                    weights += j[0] * (j[1] - result)
    wrong = 0
    #print(len(test_data))
    for x in test_data:
        for y in x:
            result = function(dot(weights, y[0]))
            if result == y[1]:
                right+=1
            else:
                wrong+=1
    return right, len(test_data)
def function(x):
    if x > 0:
        return 1
    else:
        return 0
for i in range(5, 105, 5):
    right = 0
    sum1 = 0
    sum2 = 0
    for x in range(0, 100):
        result = test(10, i)
        r = result[0]
        a = result[1]
        sum1 = sum1 + int(r)
        sum2 = sum2 + int(a)
    print(str(i) + "\t" + str(sum1/sum2))
#functions = makeTrainingSet(10)
#print(functions)
# print("Label,V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,Majority")
# counter = 0
# for i in range(len(functions)):
#     counter = i + 1
#     print("P" + str(counter) + ",", end="")
#     for j in range(len(functions[i][0][0])):
#         if j != len(functions[i][0][0]) - 1:
#             print(str(functions[i][0][0][j]) + ",", end="")
#     print(str(functions[i][0][1]), end="")
#     print("")