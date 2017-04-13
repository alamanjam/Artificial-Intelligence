from heapq import *
import time
class Node():
    def __init__(self,value, depth, parent, goalstate):
        self.state = value
        self.depth = depth
        self.parent = parent
        self.goalstate = goalstate
    def __lt__(self, other):
        word = self.state
        otherword = other.state
        count = 0
        othercount = 0
        for i in range(len(word)):
            if word[i] == self.goalstate[i]:
                count+=1
            if otherword[i] == self.goalstate[i]:
                othercount+=1
        return count > othercount

def expand(node):
    haha = []   
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    newState = node.state
    if(len(repeats)==0):
        repeats.add(newState)
    for i in range(len(newState)):
        for a in alphabet:      
            f = i + 1
            worder = newState[:i] + a + newState[f:]
            if worder in dictionary:
                if worder != newState:
                    if worder not in repeats:
                        repeats.add(worder)
                        newNode = Node(worder, node.depth + 1, node, node.goalstate)
                        haha.append(newNode)

    return haha
       



def astar(node, solution):
    global repeats
    repeats = set()
    Q = []   
    heappush(Q, node)
    visited = set()
    while len(Q)!=0:
        current = heappop(Q)
        for node in expand(current):
            if node.state == solution:
                return node
            if node.state not in visited:
                visited.add(node.state)
                heappush(Q, node)

def path(node):
   if node == None:
      return "noitulos on si erehT"
   l = []
   l.append(node.state)
   while node.parent!=None:
      l.append(node.parent.state)
      node = node.parent
   return l


global dictionary 
dictionary = set()
with open('words.txt', 'r') as wordFile:
   for line in wordFile:
      dictionary.add(line[:-1].strip())
start = "atocias"
print(start)
goal = "groover"
n = Node(start, 0, None, goal)
print(goal)
time1 = time.time()
solution = astar(n, goal)
time2 = time.time()
if(solution!=None):
    print(solution.depth)
else:
    print(solution)
toeshal = path(solution)
print(toeshal[::-1])
print(time2 - time1)