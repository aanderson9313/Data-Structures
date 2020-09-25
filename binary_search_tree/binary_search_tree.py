"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #check if value is int
        value_type = type(value)
        if value_type != int and value_type != float:
            print (f"Error: Insert type is {value_type}")
            print ("Type must be 'int'")
            return
        #check if the value is < the value of the current node's value
        if value < self.value:
            #if there's no left child already there
            if not self.left:
                # add new node to the left
                left_node = BSTNode(value)
                #create a BSTNode and encapsulate the value in it and then set it to the Left Mode
                self.left = left_node
                #otherwise recursively call insert on the left node
            else:
                self.left.insert(value)
            #otherwise recursively call insert on the right node
        if value >= self.value:
            #otherwise
                #check if none
                if not self.right:
                    # add new node to the right
                    right_node = BSTNode(value)
                    self.right = right_node
                    #otherwise
                else: 
                    #call insert on the
                    self.right.insert(value)
            

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #if the value of the current node matches the target
        if target == self.value:
            #return True
            return True
        #check if the target is < the value of the current nodes value
        elif target < self.value:
            # if theres no left child already there
            if not self.left:
                #return False
                return False
            #otherwise if left value == target return true
            elif self.left.value == target:
                return True
            else: 
                #return a call of 'contains' on the Left child passing in the target value
                return self.left.contains(target)
            #otherwise the target is > the value of the current node
        elif target > self.value:
            #if theres no Right child already there
            if not self.right:
                #return False
                return False
            #otherwise if right == target return true
            elif self.right.value == target:
                return True
            else:
            #return call of 'contains' on the right child passing in the target value
                return self.right.contains(target)
        else: print(f"could not locate {target} in tree")

    # Return the maximum value found in the tree
    def get_max(self):
        #check for empty tree
        if not self.value:
            #return None
            print('tree is empty')
            return None
        
        #recursive
        #check if there is node to the right
        if not self.right:
            #if true return value
            return self.value
        #otherwise return call to get_max on the right child
        else:
            return self.right.get_max()
        
        #iterative
        #intialize
        max_value = self.value
        #get a ref to the current node
        current_node = self
        #Loop while there is a node
        while current_node:
            #if current > max value, update max_value
            if current_node.value > max_value:
                max_value = current_node.value
            #move onto the next right node
            current_node = self.right
            #return max value
            return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        #call function passing in the current nodes value
        fn(self.value)
        #if there is a node to the left
        if self.left:
            #call the fn on the left value
            self.left.for_each(fn)
        #if there is a node on the right
        if self.right:
            #call fn on the right value
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        #uses queues
        #set current_node
        current_node = self
        #create queue, intitialize with current_node
        queue = [current_node]
        
        #while theres data in the queue
        while queue:
            #dequeue from queue to the current_node
            current_node = queue.pop(0)
            print(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        #uses queues
        #set current_node
        current_node = self
        #create queue, intitialize with current_node
        stack = [current_node]
        #while theres data in the queue
        while stack:
            #pop from stack to current_node
            current_node = stack.pop()
            print(current_node.value)
            if current_node.left:
                stack.append(current_node.left)
            if current_node.right:
                stack.append(current_node.right)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()  
