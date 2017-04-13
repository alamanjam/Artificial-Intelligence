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
   def __init__(self,value, depth, parent):
      self.state = value
      self.depth = depth
      self.parent = parent
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
						newNode = Node(worder, node.depth + 1, node)
						haha.append(newNode)

	return haha
       



def bfs(node, solution):
	global repeats
	repeats = set()
	Q = Queue()   
	Q.add(node)
	visited = set()
	while Q.isEmpty()==False:
		current = Q.remove()
		for node in expand(current):
			if node.state == solution:
				return node
			if node.state not in visited:
				visited.add(node.state)
				Q.add(node)

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

toeshal = []
with open('karthik.txt', 'r') as searchFile:
    for line in searchFile:
            toeshal.append(line[:-1])
for dik in toeshal:
	faf = dik.split()
	start = faf[0].strip()
	print(start)
	n = Node(start, 1, None)
	goal = faf[1].strip()
	print(goal)

	solution = bfs(n, goal)
	if(solution!=None):
		print(solution.depth)
	else:
		print(solution)
	#solutionpath = path(solution)
	#print(solutionpath[::-1])