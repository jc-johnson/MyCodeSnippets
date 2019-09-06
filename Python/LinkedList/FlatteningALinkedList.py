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

    # removes first node from linked list
    @staticmethod
    def removeHead(node):
        if (node is None):
            return None
        elif (node.next is None):
            return node
        elif (node.next is not None):
            copy = node.next
            Node.traverse(copy)
            return copy

    # appends one list to the end of another
    @staticmethod
    def append(list1, list2):
        if (list1 is None): return list2
        if (list2 is None): return list1
        
        #iterate to the end of list 1
        current = list1
        while (current.next is not None):
            current = current.next
        current.next = list2
        return current
  
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

    '''
    # swap test
    Node.traverse(node1)
    Node.swap(node1)
    Node.traverse(node1)

    # sort test
    Node.traverse(node1)
    Node.sort(node1)
    Node.traverse(node1)
    
    # remove head test
    print("Original List")
    Node.traverse(node1)
    print("Removed Head")
    # Node.removeHead(node1)
    node = Node.removeHead(node1)
    Node.traverse(node)
    '''

    # append test
    list1 = Node(2) 
    node2 = Node(22) 
    node3 = Node(19)
    list1.next = node2
    node2.next = node3
    print("List 1:")
    Node.traverse(list1)

    list2 = Node(7) 
    node4 = Node(29) 
    node5 = Node(100)
    list2.next = node4
    node4.next = node5
    print("List 2:")
    Node.traverse(list2)

    print("Appended List")
    Node.append(list1, list2)
    Node.traverse(list1)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
