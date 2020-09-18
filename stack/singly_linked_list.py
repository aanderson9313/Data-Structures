class Node:
    def __init__(self, value, next_node = None):
        #value the node is holding
        self.value = value
        #ref to the next node in the chain
        self.next_node = next_node
        
    def get_value(self):
        """
        Method to get the value of a node
        """
        return self.value
    
    def get_next_node(self):
        """
        Method to get the next node
        """
        return self.next_node
    
    def set_next_node(self, new_next):
        """
        Method to update the node's "next_node"
        """
        self.next_node = new_next
        
class LinkedList:
    def __init__(self):
        # what attributes do we need?
        self.head = None
        self.tail = None
        
    def add_to_tail(self, value):
        # create a new Node
        new_node = Node(value)
        #check if LL is empty
        if self.head is None and self.tail is None:
            # update head & tail attributes
            self.head = new_node
            self.tail = new_node
            #otherwise list must have at least one item
        else:
            # set next_node of my new Node to the head
            self.tail.set_next_node(new_node)
            # update tail attribute
            self.tail = new_node
            
    def remove_head(self):
        # empty list
        if self.head is None and self.tail is None:
            return None
        
        if self.head == self.tail:
            #store value of node being removed
            value = self.head.get_value()
            #remove node
            #set head and tail to none
            self.head = None
            self.tail = None
            #return stored value
            return value
        else:
            #store old heads value
            value = self.head.get_value()
            #set self.head to old heads next
            self.head = self.head.get_next_node()
            #return value
            return value
    
    def remove_tail(self):
        #remove last node in chain and return its value
        #check for empty list
        if self.head is None and self.tail is None:
            #return None
            return None
        #check if there is only one node
        if self.head == self.tail:
            #store the value of the node being removed
            value = self.tail.get_value()
            #remove node
            #set head and tail to none
            self.head = None
            self.tail = None
            #return stored value
            return value
        #otherwise
        else:
            #store value of node being removed
            value = self.tail.get_value()
            #set self.tail to the second to last node
            # can only be done by traversing the entire list from beg to end
            #starting from the head
            current_node = self.head
            #keep iterating until the node after current node is the tail
            while current_node.get_next_node() != self.tail:
                #keep looping
                current_node = current_node.get_next_node()
            #at the end of the iteration set self.tail to current_node
            self.tail = current_node
            #set the new tails next_node to none
            self.tail.set_next_node(None)
            #return value
            return value
    
    def contains(self, value):
        # loop through LL until next pointer is None
        cur_node = self.head
        while cur_node is not None:
            # if we find 'value'
            if cur_node.get_value() == value:
                return True
            return False
        
    def get_max(self):
        #TODO
        pass
    
    