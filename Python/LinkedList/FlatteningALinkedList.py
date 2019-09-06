class Node:
    
    # Constructor 
    def __init__(self,val):
        self.val = val
        self.next = None # pointer to the next node in main list
        self.down = None # pointer to next node in secondary/down list
        
    # Traverse a linked list 
    def traverse(self):
        node = self # start from the head node
        while node != None:
            print (node.val) # access the node value
            node = node.next # move on to the next node

    # Traverse a linked list
    @staticmethod
    def traverseMain(self):
        node = self # start from the head node
        while node != None:
            print (node.val) # access the node value
            node = node.next # move on to the next node

    # Traverse a linked list
    @staticmethod
    def traverseDown(self):
        node = self # start from the head node
        while node != None:
            print (node.val) # access the node value
            node = node.down # move on to the next node
       
    # returns the length of a list
    @staticmethod
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
    @staticmethod
    def printNthNode(self, nodeNumber):
        if self is None:
            return
        node = self
        for x in range(0, nodeNumber-1):
            node = node.next
        print (node.val)


    # returns middle node in list of odd lenght
    # returns middle two nodes in list of even length
    @staticmethod
    def getListMiddle(self):
        if (self is None):
            return 0
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

    # sort a single linked list
    @staticmethod
    def sort(self):
        if (self is None):
            return self
        min = self.val

        # traverse list and swap as needed
        node = self
        while node.next != None:
            print ("Node value:", node.val)
            print ("Current min:", min)
            # if (node.val < min):
            #    Node.swap(self)         
            if (node.val > node.next.val):
                Node.swap(self)
            node = node.next 
        

    # swaps positions of current node and its following node
    @staticmethod
    def swap(self):
        if (self is None): return None
        elif (self.next is None):
            return self
        else:
            temp = self.next.val
            self.next.val = self.val
            self.val = temp
        return self
        
  
def main():
    """ Main entry point of the app """
    print("hello world")
        
    # node1 = None
    node1 = Node(12) 
    node2 = Node(99) 
    node3 = Node(37)
    node4 = Node(66)
    node5 = Node(27)
    node1.next = node2 # 12->99
    node2.next = node3 # 99->37
    node3.next = node4 # 37->66
    node4.next = node5 # 66->27
    # the entire linked list now looks like: 12->99->37->66->27
    # node1.traverse()
    # node1.getListLength()
    # node1.printNthNode(3)
    # node1.getListMiddle()
    #Node.traverseMain(node1)


    #Node.traverse(node1)
    #Node.swap(node1)
    #Node.traverse(node1)

    Node.traverse(node1)
    Node.sort(node1)
    Node.traverse(node1)
    

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
