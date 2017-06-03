

class Node:
	def __init__(self,data=None,next=None):
		self.data = data
		self.next = next

class Stack:
	def __init__(self,top = None):
		self.top = top

	def push(self,data):
		newnode = Node()
		newnode.data = data
		newnode.next = self.top
		self.top = newnode

	def pop(self):
		if not self.isempty():
			self.top = self.top.next

	def peek(self):
		if not self.isempty():
			return self.top.data
		else:
			return -1			

	def isempty(self):
		if ( self.top == None ):
			return True 
		return False 			

	def print_stack(self):
		temp = self.top
		while ( temp != None ):
			print temp.data
			temp = temp.next			



class Queue:
	def __init__ ( self,front = None , rear = None):
		self.front = None
		self.rear = None

	def enque(self,data):
		newnode = Node()
		newnode.data = data
		newnode.next = None
		if ( self.isempty() ):
			self.rear = newnode
			self.front = newnode
			return
		self.rear.next = newnode		
		self.rear = newnode	

	
	def deque(self):
		if self.isempty():
			return
		else:
			self.front = self.front.next			

	def isempty(self):
		if self.rear == None or self.front == None :
			return True 
		else:
			return False 

	def print_queue(self):
		temp = self.front		
		while ( temp != None ):			
			print temp.data		
			temp = temp.next		

	def peek(self):
		if self.isempty():
			return None
		else:
			return self.front.data			

class BNode:
	def __init__(self,data=None,left=None,right=None):
		self.data = data
		self.left = left
		self.right = right				


class BinarySearchTree:
	def __init__(self,root = None):
		self.root = root	

	def insert(self,root,data):
		if root == None:
			newnode = BNode(data)
			self.root = newnode				
			return

		if ( root.data > data ):
			if ( root.left == None ):
				root.left = BNode(data)
				return
			self.insert(root.left,data)
			return				
		else:
			if ( root.right == None ):
				root.right = BNode(data)
				return
			self.insert(root.right,data)
			return												

	def findmin(self,root):		
		while root.left != None:			
			root = root.left 			
		return root			
		
	def findmax(self,root):
		while root.right != None:
			root = root.right
		return root			

	def delete(self,root,data):			
		if root == None:
			return
		elif root.data == data:
			if root.right == None and root.left == None:								
				return -1
			elif root.right != None and root.left == None:
				temp = root.right
				return temp
			elif root.right == None and root.left != None:
				temp = root.left
				return temp
			elif root.right != None and root.left != None:
				mi = self.findmin(root.right)
				root.data=mi.data				
				self.delete(root.right,root.data);																						
				return				
		elif data > root.data:
			temp  = self.delete(root.right,data)												
			if temp == -1:
				root.right = None			
			elif temp != None:
				root.right = temp				
		else:
			temp  = self.delete(root.left,data)												
			if temp == -1:
				root.left = None	
			elif temp != None:
				root.left = temp								


	def preorder(self,root):
		if ( root == None ):
				return
		print root.data
		self.preorder(root.left)			
		self.preorder(root.right)	
	
	def postorder(self,root):
		if ( root == None ):
				return		
		self.postorder(root.left)			
		self.postorder(root.right)							
		print root.data

	def inorder(self,root):
		if ( root == None ):
				return		
		self.inorder(root.left)			
		print root.data
		self.inorder(root.right)									

	def max(self,a,b):
		if a > b:
			return a 
		else:
			return b 							

	def findheight(self,root):
		if ( root == None ):
			return -1 		
		l = self.findheight(root.left)
		r = self.findheight(root.right)							
		return self.max(l,r) + 1  

	
	def bfsutil(self,root):
		obj = Queue()	
		print root.data	
		self.bfs(root,obj)

	def bfs(self,root,obj):	
		if ( root == None ):
				return		
		if ( obj.isempty() ):			
			obj.enque(root.left)					
			obj.enque(root.right)				
		else:				
			print obj.peek().data						
			if ( obj.peek().left != None ):
				obj.enque(obj.peek().left)
			if ( obj.peek().right != None ):
				obj.enque(obj.peek().right)
			obj.deque()
		self.bfs(obj.peek(),obj)			
			

	def isbstutil(self,root):
		min_ele = -10000
		max_ele = 10000
		if ( self.isbst(root,min_ele,max_ele) ):
			return True 
		else:
			return False			

	def isbst(self,root,min_ele,max_ele):
		if root == None:
			return 1
		elif root.data < min_ele or root.data > max_ele:			
				return 0
		else:			
			return self.isbst(root.left,min_ele,root.data) and self.isbst(root.right,root.data,max_ele)

class LinkedList:
	def __init__(self,head = None,tail=None): 
		self.head = head 
		self.tail = tail

	def append(self,data):	
		newnode = Node()		
		newnode.data = data				
		if ( self.head == None ):					
			newnode.next = self.head			
			self.head = newnode
			self.tail = self.head	
			return 			
		newnode.next = self.head										
		self.head = newnode		
		

	def preappend(self,data):
		newnode = Node()		
		newnode.data = data
		newnode.next = None
		self.tail.next = newnode
		self.tail = newnode					
		

	def delete(self,data):		
		if ( self.head.next == None ):
			self.head = None 					
		elif ( self.head.data == data ):
			self.head = self.head.next

		temp = 	self.head										
		while ( temp != None ):			
			if ( temp.data == data ):
				if ( temp.next == None ):
					prev.next = temp.next			
					self.tail = prev	
				
					return
				prev.next = temp.next							
				
				return temp.data 
			prev = temp			
			temp = temp.next		
		

	def delete_by_postion(self,position):
		i=0
		temp = self.head

		if ( position == 0 ):
			self.head = self.head.next			 			
			return

		while ( i < position and temp.next != None ):			
			prev=temp
			temp = temp.next
			i += 1
		prev.next = temp.next		

	def print_me(self):
		while ( self.head != None ):
			print self.head.data
			self.head = self.head.next




class HashTable:	
	# open addressing   ==> arrays  / list in python
		# linear probing 
		# quadratic probing 
		# double hashing 		
	
	# seprate chaining  ==>  linkedlist    

	class Node:
		def __init__(self,data = None ,next = None ):
			self.data = data
			self.next = None  		

	class Sepratechaining:

		def __init__(self,lis=None):		
			self.lis = [None] * 10 		

		def hash(self,data):
			return data % 10

		def insert(self,data):
			key = self.hash(data)			
			if self.lis[key] == None:
				self.lis[key] = Node(data)
				return		
			else:			
				x = self.lis[key]
				while x.next != None:
					x = x.next
				newnode = Node(data)
				x.next = newnode
				return			

		def print_table(self):						
			for i in range(len(self.lis)):
			 	if self.lis[i] != None:
			 		x = self.lis[i]
			 		print " lis[%d] = %d \t" %(i,x.data)
			 		while x.next != None:		
			 			x = x.next 		  			
			 			print " -> %d" % x.data			 							 	

		def lookup(self,data):
			key = self.hash(data)
			x = self.lis[key]
			while ( x != None ):
				if ( x.data	== data ):
					return key
				x = x.next

		def delete(self,data):		
			key = self.hash(data)
			x = self.lis[key]		
			if x.data == data :
				self.lis[key] = x.next
				return	
			p = x
			while (x != None):			
				if ( x.data == data ):				
					p.next = x.next
					return 
				p = x				
				x = x.next


	# ==> list 

	class LinearProbing:		
		def __init__(self,lis=None):
			self.lis = [None] * 10		
		
		def hash(self,data):
			return data % 10

		def insert(self,data):			
			k = self.hash(data)
			if self.lis[k] == None:
				self.lis[k] = data
				return
			else:
				while ( k < len(self.lis) and self.lis[k] != None  ):					
					k = k + 1 				
				if ( k == len(self.lis) ):
					k = k % len(self.lis) 				
				if ( self.lis[k] == None ):
					self.lis[k] = data					
				else:
					print "No More Space to Insert Data"					

		def delete(self,data):
			k = self.hash(data)
			if self.lis[k] == data:
				self.lis[k] = None
				return
			while k < len(self.lis) and self.lis[k] != data: 									
				k += 1
			if ( self.lis[k] == data):
				self.lis[k] = None
				return 

		def lookup(self,data):
			k = self.hash(data)
			if ( self.lis[k] == data ):
				return k
			else:
				while k < len(self.lis) and self.lis[k] != data:
					k += 1 		
				if ( k >= len(self.lis)):
					return "Not Found"											
				if ( self.lis[k] == data):					
					return k

	# ==> QuadraticProbing , list 

	class QuadraticProbing:

		def __init__(self,lis=None):			
			self.lis = [None] * 10

		def pow(self,a,b):
			return a ** b

		def hash(self,i,data):
			p = data ** i 
			return (data + p) % 10			

		def insert(self,i,data):			
			k = self.hash(i,data)
			if self.lis[k] == None:
				self.lis[k] = data
				return	
			if i < len(self.lis):							
				i += 1
				self.insert(i,data)	
				return			
			else:
				print "Cant Insert Value"				


		def delete(self,i,data):
			k = self.hash(i,data)
			if self.lis[k] == data:
				self.lis[k] = None
			else:
				if ( k < len(self.lis)):
					i += 1	
					self.delete(i,data)				

		def lookup(self,i,data):
			k = self.hash(i,data)
			if self.lis[k] == data:				
				return k 
			else:
				if ( i < len(self.lis)):
					i += 1	
					k = self.lookup(i,data)									
					return k 				
			return "Not Found"
	
	# ==> DoubleHashing , two hash functions 		

	class DoubleHashing:
		def __init__(self,lis=None):
			self.lis = [None] * 10

		def hash1(self,data):
			return data % 3 		
	
		def hash2(self,data):
			return (self.hash1(data) + (7 - data % 7) ) % 10

		def insert(self,data):		
			k = self.hash1(data)	
			if self.lis[k] == None:
				self.lis[k] = data
				return

			k1 = self.hash2(data)				
			if ( self.lis[k1] == None):
				self.lis[k1] = data 
				return

		def delete(self,data):
			k = self.hash1(data)
			if self.lis[k] == data:
				self.lis[k] = None
				return			
			else:
				k1 = self.hash2(data)				
				if self.lis[k1] == data:		
 					self.lis[k1] = None	
 					return			
					


class Sort:
	def __init__(self,lis=[]):
		self.lis=lis
		self.len = len(self.lis)

	def bubblesort(self):		
		i = self.len-1		
		while i >= 0: 
			j = i - 1								
			while j >= 0:
				if self.lis[i] < self.lis[j]:
					self.lis[i], self.lis[j] = self.lis[j],self.lis[i] # i = 0 , j = 1 1st pass 								
				j -= 1									
			i -= 1							
		return self.lis 					

	def insertionsort(self):						
		for i in range(1,self.len):
			hole = i - 1	
			value = self.lis[i]
			while hole >= 0 and self.lis[hole] > value:
				self.lis[hole+1] = self.lis[hole]
				hole = hole - 1 						
			self.lis[hole+1] = value					
		return self.lis 

	def selectionsort(self):		
		for i in range(self.len):
			m = i 
			for j in range(i+1,self.len):
				if self.lis[m] < self.lis[j]:
					m = j 
				self.lis[m],self.lis[j] = self.lis[j],self.lis[m]
		return self.lis 								

	def quicksort(self):		
		def swap(a,b):				
			self.lis[a],self.lis[b] = self.lis[b],self.lis[a]
		
		def partition(start,end):
			pivot = self.lis[start]
			right = end
			left = start+1
			done = False
			while not done:																						
				while left <= right and self.lis[left] <= pivot:
					left +=1 
				while right >= left and self.lis[right] >= pivot:
					right -= 1
				if right < left:
					done = True
				else:
					swap(left,right)
			swap(start,right)
			return right																												

		def sort(start,end):
			if start < end:
				piv = partition(start,end)				
				sort(start,piv-1)	
				sort(piv+1,end)	
				
		sort(0,self.len-1)									
		return self.lis

	
	
	def mergesort(self):
		def merge(lis,l,lsize,r,rsize):
			i=0
			j=0
			k=0
			while i < lsize and j < rsize:
				if l[i] < r[j]:					
					lis[k] = l[i]					
					k += 1
					i += 1
				else:
					lis[k] = r[j]
					j += 1
					k += 1					
			
			while i < lsize:
				lis[k] = l[i]
				i += 1
				k += 1 

			while j < rsize:
				lis[k] = r[j]
				j += 1
				k += 1
			return lis 				
			
		def sort(lis,size):
			if size < 2:
				return 
			mid = size / 2 
			l = lis[:mid]
			r = lis[mid:]												
			sort(l,len(l))			
			sort(r,len(r))					
			lis = merge(lis,l,len(l),r,len(r))						
			return lis 

		lis = sort(self.lis,self.len)		
		return lis 					


	def radixsort(self):				
		pass 


# ==> Like a Dictonary 	

class Tries:
	def __init__(self,value = None):
		self.root = None				
		self.bool = [0] * 26

	class List:
		def __init__(self,value=None):
			self.lis = [None] * 26
			self.value = value
			self.data = None

	def getindex(self,data):
		return ord(data) - 97

	def insert_util(self,data,key):
		if self.root == None:
			newnode = self.List()		
			self.root = newnode 
		size = len(data)				
		root = self.insert(self.root,data[0])
		self.bool[self.getindex(data[0])] = self.bool[self.getindex(data[0])] + 1 
		for i in range(1,size):							
			root = self.insert(root,data[i])				
		root.data = key

	def insert(self,root,data):
		indx = self.getindex(data)						
		if root.lis[indx] == None:						
			root.lis[indx] = self.List()		
			return root.lis[indx]
	 	else:
	 		return root.lis[indx] 

	def print_value(self,data):						
		root = self.root

		size = len(data)

		for i in range(size):
			indx = self.getindex(data[i])			
			if root.lis[indx] == None:
				print "Element Not Found"
				return
			root = root.lis[indx]
		
		if root.data != None:
			print root.data
			return 	
		else:
			print "Element not Found"
			return

	def delete(self,data):
		root = self.root
		indx = self.getindex(data[0])
		if self.bool[indx] == 1:
			self.root.lis[indx] = None 
			self.bool[indx] -= 1
			return 
		size = len(data)

		for i in range(size):
			indx = self.getindex(data[i])			
			if root.lis[indx] == None:
				print "Element Not Found to be Deleted"
				return
			root = root.lis[indx]

		root.data = None 
		return 			




class Heap:
	def __init__(self,lis=[],size=0):
		size += 1
		self.size = size - 1
		self.lis = [None] * size
		self.c = 1

	def print_heap(self):
		print self.lis[1:]

	def extract_min(self):
		if not self.isempty():
			mi = self.lis[1]
			self.lis[1] = self.lis[len(self.lis)-1]
			self.lis.pop()
			self.min_heap()
			return mi 	
		else:
			return 			

	def increase_key(self,data,indx):
		if self.lis[indx] < data:
			self.lis[indx] = data		
			return 							
		return 

	def decrease_key(self,data,indx):
		if self.lis[indx] > data:
			self.lis[indx] = data 
			self.min_heap()
			return 
		return 

	def extract_max(self):
		if self.lis[self.size] > self.lis[1]:
			return self.lis[self.size]
		return self.lis[1]				

	def insert_heap(self,data):
		if self.lis[self.c] == None:			
			self.lis[self.c] = data 
			return 
		if self.lis[self.c * 2] == None:			
			self.lis[self.c * 2] = data 
			return 
		if self.lis[self.c * 2 + 1] == None:			
			self.lis[self.c * 2 + 1] = data 
			return 			
		self.c = self.c + 1
		self.insert_heap(data)			

	def max_heap(self):	
		size = (len(self.lis) - 1 ) / 2		
		i=size
		while i >= 1:			
			self.max_heapify(i)
			i -= 1

	def max_heapify(self,i):
		root = i
		left = 2 * i 
		right = 2 * i + 1
		size = len(self.lis) - 1		
		if left > size or right > size:
			return 
		if self.lis[left] > self.lis[right]:
			largest = left
		else:
			largest = right 
		if self.lis[root] > self.lis[largest]:
			root = largest
		if root != largest:
			self.swap(i,largest)
			self.max_heapify(largest)			 								

	def heapsort(self):				
		i = len(self.lis) - 1
		lis = [None] * 12
		while i >= 1:
			self.max_heap()
			self.swap(1,i)
			lis[i] = self.lis[i]
			self.lis[i] = None							
			i -= 1
		self.lis = lis 			
		

	def swap(self,a,b):
		self.lis[a] ,self.lis[b] = self.lis[b] ,self.lis[a]

	def min_heap(self):		
		size = (len(self.lis) - 1 ) / 2
		i = size
		while i >= 1:
			self.min_heapify(i)
			i -= 1		

	def min_heapify(self,i):
		root = i 
		left = 2 * i 
		right = 2 * i + 1					
		if left > len(self.lis) or right >= len(self.lis):
			return  
		if self.lis[left] > self.lis[right]:
			minimum = right 
		else:
			minimum = left			
		if self.lis[root] < self.lis[minimum]:
			minimum = root
		if root != minimum:			
			self.swap(root,minimum)						
			self.min_heapify(minimum)		


	def isempty(self):
		if len(self.lis) == 1:
			return True 
		else:
			return False			

class Search:
	def __init__(self,lis):
		self.lis = lis

	def linearsearch(self,data):
		for i in range(len(self.lis)):
			if self.lis[i] == data:
				return i  
		return "Not Found"				

	def binarysearch(self,data):
		obj = Sort(self.lis)
		self.lis = obj.mergesort()		
		print self.lis 
		indx = self.binarysearch_util(self.lis,data,len(self.lis))
		return indx	

	def binarysearch_util(self,lis,data,size):				
		if size <= 1:
			return "Not Found"
		mid = size / 2	 	
		print lis 
		if data == lis[mid]:
			return data
		if data > lis[mid]:
			mid = self.binarysearch_util(lis[mid:],data,len(lis[mid:]))
			return mid 
		else:
			mid = self.binarysearch_util(lis[:mid],data,len(lis[:mid]))				
			return mid 				

class Graphs:
	def __init__(self,graph=None,size=0):
		self.size = size - 1
		self.graph = [None] * size		
		self.all_edges=[]
		self.c = 0
		self.map_heap = {}

	class Vertice:
		def __init__(self,data=None,next=None,flag=None):
			self.data = data			
			self.next = None
			self.flag = False
			

	class Edge:
		def __init__(self,vindex1=None,vindex2=None,weight=None,ptr=None):
			self.vindex1 = vindex1
			self.vindex2 = vindex2
			self.weight = weight 
			self.ptr = ptr
	
	def insert(self,data):
		self.graph[self.c] = self.Vertice(data)
		self.c += 1 
	
	def addedge_undirected(self,v1,v2,weight):
		p = self.graph[v1].next
		e1 = self.Edge(vindex1=v1,vindex2=v2,weight=weight)	
		self.all_edges.append(e1)	
		while p and p.ptr:
			p = p.ptr
		if ( p ):
			 p.ptr = e1			
		else:
			self.graph[v1].next = e1

		p = self.graph[v2].next
		e2 = self.Edge(vindex1=v2,vindex2=v1,weight=weight)
		#self.all_edges.append(e2)
		while p and p.ptr:
			p = p.ptr;
		if p:
			p.ptr = e2
		else:
			self.graph[v2].next = e2			



	def addedge_directed(self,v1,v2,weight=0):
		ed = self.Edge(vindex1=v1,vindex2=v2,weight=weight)
		self.all_edges.append(ed)
		p = self.graph[v1].next
		while p and p.ptr != None:
			p = p.ptr 
		if p :
			p.ptr = ed			
		else:
			self.graph[v1].next = ed
	

	def print_graph(self):
		i = 0
		while  i < self.c:
			print "graph[%d] = %d " % ( i,self.graph[i].data)
			e = self.graph[i].next			
			while ( e ):
				print " -> %d" %(e.vindex)
				e = e.ptr 
			i += 1				

	def displayvertex(self,i):
		print self.graph[i].data	

	def not_visited_all(self):
		for i in range(self.c):
			if self.graph[i].flag == False:
				return True
		return False

	def dfsutil(self):
		obj = Stack()
		print self.graph[0].data
		obj.push(0)
		self.graph[0].flag = True 
		self.dfs(obj,self.graph[0].next)

	def dfs(self,obj,p):			
		if ( obj.isempty() ):
			return			

		if  p and self.graph[p.vindex].flag == False:
			self.displayvertex(p.vindex)			
			self.graph[p.vindex].flag = True
			obj.push(p.vindex)

		if ( p ):
			p = self.graph[p.vindex].next
			while ( p ):
				if ( self.graph[p.vindex].flag == False):
					break
				p = p.ptr
		else:
			i = obj.peek()									
			p = self.graph[i].next
			while ( p ):
				if ( self.graph[p.vindex].flag == False):									
					break
				p = p.ptr							
			obj.pop()

		if ( self.not_visited_all() ):			
			self.dfs(obj,p)			
		else:
			self.reset_flags()

	def bfsutil(self):
		obj = Queue()
		self.displayvertex(0)
		obj.enque(0)
		self.graph[0].flag = True 
		self.bfs(obj,self.graph[0].next)
	
	def bfs(self,obj,p):
		if ( obj.isempty() ):
			return 
		while ( p ):
			if ( self.graph[p.vindex].flag == False):
				self.displayvertex(p.vindex)
				obj.enque(p.vindex)
				self.graph[p.vindex].flag = True
			p = p.ptr		
		p = self.graph[obj.peek()].next
		obj.deque()
		if ( self.not_visited_all()):
			self.bfs(obj,p)		
		else:
			self.reset_flags()					


	def reset_flags(self):
		for i in range(self.c):
			self.graph[i].flag = False


	def get_key(self,edge):
    		return edge.weight

	def kruskal_spanning_tree_algorithm(self): # for directed 		
			obj = DisjointSet()			# disjoint set object 
			for i in range(len(self.graph)): 
				if self.graph[i]:																			
					obj.insert(self.graph[i].data) #insert sets as datas 
			sort_lis = sorted(self.all_edges,key = self.get_key) # sort according to the weights 

			lis = []  #empty lis for each edge with minimum span 
			for i in sort_lis:
				root1 = obj.find(self.graph[i.vindex1].data) # vertex 1 
				root2 = obj.find(self.graph[i.vindex2].data) # vertex 2 
				if root1 != root2: # if vertex1.parent == vertex2.parent, then do nothing because already a set 
					lis.append(i) # append the edge to lis 
					obj.union(root1.data,root2.data) #if not connected  then merge sets 
			self.kruskal_print(lis) # print the set 					 
			#return lis 

	
	def kruskal_print(self,lis):
		for i in lis:
			print self.graph[i.vindex1].data,self.graph[i.vindex2].data,i.weight
	
	def get_weight(self,v1,v2):
		p = self.graph[v1].next
		p1 = self.graph[v2]
		while p:
			if self.graph[p.vindex2] == p1:
				break
			p = p.ptr		
		return p.weight 						

	def get_unvisited_vertex(self,visited_lis):
		for i in self.graph:
			if i not in visited_lis:
				return i

	def visited_all(self,visited_lis):
		for i in self.graph:
			if i in visited_lis:
				return False 
		return True 		

	def prims(self):			
		import sys 
		obj = PriorityQueue(True)
		for vertex in self.graph:
			obj.add_task(sys.maxint,vertex)
		obj.change_task_priority(0,self.graph[0])
		result = [] 
		v_e = {}

		while not obj.is_empty():
			current_node = obj.pop_task()

			if current_node in v_e:
				node = v_e[current_node]
				result.append(node)
			
			p = current_node.next
			edge_lis = [] 
			while p: 
				edge_lis.append(p)
				p = p.ptr				

			for edge in edge_lis:
				vertex = self.graph[edge.vindex2]
				if obj.contains_task(vertex):
					if obj.get_task_priority(vertex) > edge.weight:					
						obj.change_task_priority(edge.weight,vertex)	
						v_e[vertex] = edge

		for i in result:
			print self.graph[i.vindex1].data, self.graph[i.vindex2].data, i.weight

	def top_sort(self):
		stack = [] 
		visited = [] 
		for vertex in self.graph:
			if vertex in visited:
				continue 
			self.top_sort_util(vertex,visited,stack)	
		return stack 

	def top_sort_util(self,vertex,visited,stack):
		visited.append(vertex)
		edge_lis = [] 
		p = vertex.next
		while p:
			edge_lis.append(self.graph[p.vindex2])
			p = p.ptr
		for adjacent in edge_lis:
			if adjacent in visited:
				continue
			self.top_sort_util(adjacent,visited,stack)
		stack.append(vertex)											

	def get_all_vertices(self):
		import sys 
		map_ = {}
		infinity = sys.maxint 
		for i in self.graph:
			map_[i.data] = infinity
		return map_ 			

	def shortest_path(self,sourceVertex):    #dijstra's shortest path algo 
		obj = PriorityQueue(True)
		for vertex in self.graph:
			obj.add_task(sys.maxint,vertex)
		obj.change_task_priority(0,sourceVertex)			
		distance = {}
		parent = {}
		parent[sourceVertex] = None 
		while not obj.is_empty():
			vertex = obj.peek_task()
			weight = obj.get_task_priority(vertex)
			current_node = obj.pop_task()
			distance[current_node] = weight			

			edge_lis = [] 
			edge = current_node.next
			while edge:
				edge_lis.append(edge)
				edge = edge.ptr

			for edge in edge_lis:
				adjacent = self.graph[edge.vindex2]  
				if obj.contains_task(adjacent): 				
					new_weight = distance[current_node] + edge.weight 
					if new_weight < obj.get_task_priority(adjacent):
						obj.change_task_priority(new_weight,adjacent)
		self.print_dict(distance)

	def print_dict(self,distance):
		for x,y in dict.items(distance):
			print x.data, y

			
	def bellman_ford(self):
		dic,parent = {},{}	
		infinity = sys.maxint 
		for vertex in self.graph:
			dic[vertex] = infinity
		sourcevertex = self.graph[0]
		dic[sourcevertex] = 0
		parent[sourcevertex] = sourcevertex
		
		for _ in range(self.size-1):
			for vertex in self.graph:
				edge = vertex.next
				edge_lis=[]
				while edge:
					edge_lis.append(edge)
				 	edge = edge.ptr
				for edge in edge_lis:
					u = self.graph[edge.vindex1] # source 
					v = self.graph[edge.vindex2] # destination 
					if dic[v] >= dic[u] + edge.weight:
						dic[v] = dic[u] + edge.weight
						parent[v] = u

		for edge in self.all_edges:
			u = self.graph[edge.vindex1] # source 
			v = self.graph[edge.vindex2] # destination 
			if dic[v] > dic[u] + edge.weight:
				return "Graph has negative values"

		self.print_dict(dic)

	
	def bellman_ford_1(self):
		dic = {}
		infinity = sys.maxint		
		for vertex in self.graph:
			dic[vertex] = infinity
		sourcevertex = self.graph[0]
		dic[sourcevertex] = 0
		for _ in range(self.size):
			for edge in self.all_edges:
				u = self.graph[edge.vindex1]
				v = self.graph[edge.vindex2]
				if dic[v] > dic[u] + edge.weight:
					dic[v] = dic[u] + edge.weight
		self.print_dict(dic)

class DisjointSet:
	class Node:
		def __init__(self,data,parent=None,rank=0):
			self.data = data
			self.parent = parent
			self.rank = rank 

	def __init__(self):
		self.map = {}				

	def insert(self,data):
		node = self.Node(data)
		node.parent = node 
		self.map[data] = node

	def union(self,data1,data2):
		node1 = self.map[data1] 
		node2 = self.map[data2]
		parent1 = self.findset(node1)
		parent2 = self.findset(node2)
		if parent1.data == parent2.data:			
			return 
		if parent1.rank <= parent2.rank:
			if parent1.rank == parent2.rank:
				parent1.rank += 1
			parent2.parent = parent1	
		else:
			parent1.parent = parent2 						

	def find(self,data):
		return self.findset(self.map[data])


	def findset(self, node): 
	        parent = node.parent 
	        if parent == node: 
	            return parent  
	        node.parent = self.findset(node.parent)
	        return node.parent 



from heapq import *

class PriorityQueue(object):
    
    def __init__(self, is_min_heap):
        self.pq = []
        self.entry_finder = {}
        if(is_min_heap is True):
            self.mul = 1
        else :
            self.mul = -1
         
    def contains_task(self, task):
        if task in self.entry_finder:
            return True
        else:
            return False

    def get_task_priority(self, task):
        if task in self.entry_finder:
            return (self.entry_finder[task])[0]
        raise ValueError("task does not exist")
        
    def add_task(self, priority, task):
        if task in self.entry_finder:
            raise KeyError("Key already exists")
        entry = [self.mul*priority, False, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def change_task_priority(self, priority, task):
        if task not in self.entry_finder:
            raise KeyError("Task not found")
        self.remove_task(task)
        entry = [self.mul*priority, False, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)
 
    def remove_task(self, task):
        entry = self.entry_finder.pop(task)
        entry[1] = True

    def pop_task(self):
        while self.pq:
            priority, removed, task = heappop(self.pq)
            if removed is False:
                del self.entry_finder[task]
                return task
        raise KeyError("pop from an empty priority queue")

    def peek_task(self):
        while self.pq:
            priority, removed, task = tuple(heappop(self.pq))
            if removed is False:
                 heappush(self.pq, [priority, False, task])
                 return task
        raise KeyError("pop from an empty priority queue")

    def is_empty(self):
        try:
            self.peek_task()
            return False
        except KeyError:
            return True

    def __str__(self):
        return str(self.entry_finder) + " " + str(self.pq)



