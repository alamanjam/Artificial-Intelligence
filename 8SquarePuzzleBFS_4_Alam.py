class Queue():
	def __init__(self):
		self.list = []
	def add(self,object):
		self.list.append(object)
	def remove(self):
		if len(self.list) == 0:
			return False
		else:
			return self.list.pop(0)
	def size(self):
		return len(self.list)
	def isEmpty(self):
		return self.size()==0 

class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
    def getValue(self):
        return self.value
def fillArray(file):
    dictionary = set()
    with open(file,'r') as wfile:
        for line in wfile:  
            dictionary.add(line)
def expand(node):

    states = [stateU,stateL,stateD,stateR]
    while False in states:
    	states.remove(False)
    return states 

def bfs(node, goal):
    Q = Queue()   
    Q.add(node)
    visited = set()
    while Q.isEmpty()==False:
        current = Q.remove()
            for node in expand(current):    
            visited.add(node.state)
            print(node.state)
            if node.state == goal.state:
            	return(node)
            Q.add(node)

def path(node):
    n = node
    l = []
    while n.action!=None:
        l.append(n.action)
        n = n.parent
    return l
filename = "words.txt"  
dict = fillArray(filename)
start =  "toeshal"
n = Node(' ')
n.state = start
n.parent = None
n.action = None
n.depth = 0
goal = "nigger"
p = Node(' ')
p.state = goal
p.parent = None
p.action = None
p.depth = 0
solution = bfs(n,p)
solutionpath = path(solution)
print("Path: " + str(solutionpath[::-1]))