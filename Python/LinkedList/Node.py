class Node:
    
    # Constructor 
    def __init__(self,val):
        self.val = val
        self.next = None # the pointer initially points to nothing
        
    # Traverse a linked list 
    def traverse(self):
        node = self # start from the head node
        while node != None:
            print (node.val) # access the node value
            node = node.next # move on to the next node
       
    # returns the length of a list
    def getListLength(self):
        if self is None:
            return 0
        node = self
        counter = 0
        while node != None:
            print (node.val) #print current value
            counter += 1
            node = node.next # move to next node
        print (counter)
        return counter

    # print the nth node in a list 
    def printNthNode(self, nodeNumber):
        if self is None:
            return
        node = self
        for x in range(0, nodeNumber-1):
            node = node.next
        print (node.val)
        
             
def main():
    """ Main entry point of the app """
    print("hello world")
        
    node1 = Node(12) 
    node2 = Node(99) 
    node3 = Node(37) 
    node1.next = node2 # 12->99
    node2.next = node3 # 99->37
    # the entire linked list now looks like: 12->99->37
    # node1.traverse()
    # node1.getListLength()
    node1.printNthNode(3)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
