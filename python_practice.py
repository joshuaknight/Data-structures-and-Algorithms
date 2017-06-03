
from datastructure import *


obj = LinkedList()
obj.append(5)
obj.preappend(15)
#obj.print_me()


obj = Stack()
obj.push(5)
obj.push(10)
obj.push(15)
obj.push(25)
obj.push(35)
obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.push(45)
obj.push(35)
obj.push(25)
obj.push(15)
obj.push(5)
obj.pop()
obj.pop()
obj.pop()
obj.pop()
#obj.peek()
#obj.print_stack()






obj = Queue()
obj.enque(10)
obj.enque(20)
obj.enque(30)
obj.enque(40)
obj.enque(50)
obj.deque()
obj.deque()


#obj.print_queue()






obj = BinarySearchTree()
obj.insert(obj.root,10)
obj.insert(obj.root,5)
obj.insert(obj.root,3)
obj.insert(obj.root,7)
obj.insert(obj.root,6)
obj.insert(obj.root,15)
obj.insert(obj.root,17)
obj.insert(obj.root,16)
obj.insert(obj.root,20)
obj.insert(obj.root,18)
obj.insert(obj.root,25)
#obj.delete(obj.root,20)
#obj.preorder(obj.root)


#if obj.isbstutil(obj.root):
#	print "Its a BST"
#else:
#	print "Not a BST"	


#obj.bfsutil(obj.root)

#print obj.findheight(obj.root)





ob = HashTable()
obj = ob.Sepratechaining()
obj.insert(5)
obj.insert(20)
obj.insert(25)
obj.insert(55)
#obj.insert(20)
obj.insert(15)
obj.insert(14)
obj.insert(19)
obj.insert(29)
obj.insert(45)
obj.insert(30)
obj.delete(14)
obj.delete(5)
#obj.print_table()
#print obj.lookup(29)


obj = ob.LinearProbing()
obj.insert(10)
obj.insert(20)
obj.insert(40)
obj.insert(50)
obj.insert(60)
obj.insert(70)
obj.insert(80)
obj.insert(90)
obj.insert(100)
obj.insert(40)
obj.delete(50)
obj.insert(90)
obj.delete(70)
obj.insert(71)
#print obj.lis
#print obj.lookup(40)
#print obj.lookup(42)
#print obj.lookup(90)

obj = ob.QuadraticProbing()
obj.insert(0,2)
obj.insert(0,4)
obj.insert(0,6)
obj.insert(0,8)
obj.insert(0,10)
obj.insert(0,12)
obj.insert(0,14)
obj.delete(0,4)
#print obj.lookup(0,14)
#print obj.lis 


obj = ob.DoubleHashing()
obj.insert(229)
obj.insert(144)
obj.insert(332)
obj.insert(334)
obj.insert(554)
obj.insert(854)
obj.insert(1854)
obj.insert(4854)
obj.insert(5854)
obj.insert(565111)
obj.delete(554)
obj.delete(332)
obj.delete(334)
obj.delete(854)
#print obj.delete(8534)
#print obj.lis


obj = Graphs(size=7)
obj.insert('A')  # 0 
obj.insert('B') # 1 
obj.insert('C') # 2 
obj.insert('E') # 3 
obj.insert('D') # 4
obj.insert('F') # 5
obj.insert('G') # 6

#obj.addedge_directed(0,2)
#obj.addedge_directed(1,2)
#obj.addedge_directed(1,4)
#obj.addedge_directed(2,3)
#obj.addedge_directed(3,5)
#obj.addedge_directed(4,5)
#obj.addedge_directed(5,6)
obj.addedge_undirected(0,1,3)
obj.addedge_undirected(0,3,1) 
obj.addedge_undirected(1,2,1) 
obj.addedge_undirected(1,3,3) 
obj.addedge_undirected(2,5,4) 
obj.addedge_undirected(2,3,1) 
obj.addedge_undirected(2,4,5) 
obj.addedge_undirected(3,4,6)
obj.addedge_undirected(4,5,2)
obj.addedge_undirected(5,6,2)




#print "bellman_ford shortest path "
#if obj.bellman_ford():
#	print obj.bellman_ford()

#print " "
#print " "
#print "kruskal min span"
#o#bj.kruskal_spanning_tree_algorithm()
#lis = obj.top_sort()



#print " "
#print " "
#print "Topological sort"
#for i in lis:#
#	print i.data 
#print " "
#print " "
#print "dijstra's"
#obj.shortest_path(obj.graph[0])

#print " "
#print " "
#print "Prims min span"
#print " "
#print " "	
#obj.prims()




#obj.print_graph()#
#obj.dfsutil()
#obj.bfsutil()
#obj.shortest_path_algorithim()
#lis=[25,30,17,20,13,7,9]


#obj = Sort(lis)
#print 
#obj.insertionsort()
#print obj.quicksort()
#print obj.mergesort()
#obj = Search(lis)
#print obj.binarysearch(14)
#obj.radixsort()

#obj = Heap()
#obj.insert_heap(25)
#obj.insert_heap(30)
#obj.insert_heap(17)
#obj.insert_heap(20)
#obj.insert_heap(13)
#obj.insert_heap(7)
#obj.insert_heap(9)
#obj.insert_heap(45)
#obj.insert_heap(15)
#obj.insert_heap(11)
#obj.insert_heap(14)
#print obj.lis
#obj.heapsort()
#print obj.lis 

	

#obj = Tries()
#obj.insert_util("arun",55525252525)  
#obj.insert_util("arul",55525444252525)  
#obj.insert_util("joshua",7598465371)
#obj.insert_util("jackup",9759877532)  
#obj.insert_util("jackffup",1759877532)  
#obj.insert_util("pa",9789726030)  
#obj.insert_util("a",9434343789726030)
#obj.insert_util("joshuaiii",9434330) 
#obj.insert_util("zebra",7598)

#obj.print_value("arun")
#obj.print_value("joshua")
#obj.print_value("joshuaiii")
#obj.print_value("jackup")
#obj.print_value("arul")
#obj.print_value("jackffup")
#obj.print_value("pa")	
#obj.print_value("a")	
#obj.print_value("zebra")

#obj.delete("p")


#obj=RedBlackTree()
#obj.insert_red_black_tree_util(1)
#obj.insert_red_black_tree_util(2)
#obj.insert_red_black_tree_util(3)
#obj.insert_red_black_tree_util(4)
#obj.insert_red_black_tree_util(5)
#obj.insert_red_black_tree_util(6)
#obj.inorder(obj.root)
#obj = DisjointSet()
#obj.insert(13) #0
#obj.insert(15) #1
#obj.insert(20) #2
#obj.insert(25) #3 
#obj.insert(35) #4
#obj.insert(30) #5
#obj.print_set()
#obj.merge_set(0,1)
#bj.merge_set(2,3)
#obj.merge_set(4,5)


#o#bj.merge_set(0,2)
#o3#bj.merge_set(2,4)


##print " "
#print " "
#print obj.lis[0].data
#print obj.lis[0].child[0].data
#print obj.lis[0].child[1].data
#print obj.lis[2].child[1].data
#obj	 =  Heap(size=9)
#obj.insert_heap(5)
#obj.insert_heap(10)
#obj.insert_heap(13)
#obj.insert_heap(4)
#obj.insert_heap(7)
#obj.insert_heap(9)
#obj.insert_heap(3)
#obj.insert_heap(2)
#obj.insert_heap(1)
#obj.min_heap()
#obj.print_heap()
#obj.increase_key(indx = 1,data=10)
#obj.min_heap()
#obj.print_heap()


#obj = DisjointSet()
#obj.insert(15)
#obj.insert(25)
#obj.insert(35)
#obj.insert(30)
#obj.insert(40)
#obj.insert(11)
#obj.insert(31)

#obj.union(15,25)
#obj.union(25,35)
#obj.union(30,40)
#obj.union(35,30)
#obj.union(11,31)
#obj.union(31,35)

#print obj.find(11)


#obj = PriorityQueue()
#add("joshua",2)
#add("Arun",14)
#add("anand",4)

#lis = [5,6,3,7,10,4,16,18,8,9,19,20]
#obj = Search(lis) 
#print obj.binarysearch(7)





