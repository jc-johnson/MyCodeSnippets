class Node:
    
    # Constructor 
    def __init__(self,val):
        self.val = val
        self.next = None # the pointer initially points to nothing
        
        
    def traverse(self):
        node = self # start from the head node
        while node != None:
            print node.val # access the node value
            node = node.next # move on to the next node
            
            
    def main():
        """ Main entry point of the app """
        print("hello world")
        
        node1 = Node(12) 
        node2 = Node(99) 
        node3 = Node(37) 
        node1.next = node2 # 12->99
        node2.next = node3 # 99->37
        # the entire linked list now looks like: 12->99->37

    if __name__ == "__main__":
        """ This is executed when run from the command line """
        main()
