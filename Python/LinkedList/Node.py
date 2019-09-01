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
            # print (node.val) #print current value
            counter += 1
            node = node.next # move to next node
        print ("List length:", counter)
        return counter


    # print the nth node in a list 
    def printNthNode(self, nodeNumber):
        if self is None:
            return
        node = self
        for x in range(0, nodeNumber-1):
            node = node.next
        print (node.val)


    def getListMiddle(self):
        node = self
        length = node.getListLength()
        # if length is even just cut it in half
        if (length % 2) == 0: 
            middle = int(length/2)
            print("Middle:", middle)
            node.printNthNode(middle)
            node.printNthNode(middle+1) 
        else:
            middle = length
            middle += 1
            middle = int(middle/2)
            node.printNthNode(middle)
                   
        
             
def main():
    """ Main entry point of the app """
    print("hello world")
        
    node1 = Node(12) 
    node2 = Node(99) 
    node3 = Node(37)
    node4 = Node(66)
    node5 = Node(27)
    node1.next = node2 # 12->99
    node2.next = node3 # 99->37
    node3.next = node4
    node4.next = node5
    # the entire linked list now looks like: 12->99->37
    # node1.traverse()
    # node1.getListLength()
    # node1.printNthNode(3)
    node1.getListMiddle()

    # Rounded tests
    '''decimal = 5/2
    print("Decimal:", decimal)
    rounded = round(decimal, )
    print("Rounded:", rounded)'''

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
