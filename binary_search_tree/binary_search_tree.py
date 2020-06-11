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
        #left and right pointer
        self.left = None
        self.right = None
        
    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        if value > self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else: 
                self.right.insert(value)
        if value == self.value:
            self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target > self.value:
            if not self.right:
                return False
            elif target == self.right:
                return True
            else:
                return self.right.contains(target)
        if target < self.value:
            if not self.left:
                return False
            elif target == self.left:
                return True
            else:
                return self.left.contains(target)
            

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        #always will call function of self.value
        ##base case: fn(self.value) is called and function ends
        fn(self.value)
        if self.right is None and self.left is None:
            return None
        if self.right is not None and self.left is None:
            self.right.for_each(fn)
        if self.left is not None and self.right is None:
            self.left.for_each(fn)
        if self.left is not None and self.right is not None:
            self.left.for_each(fn)
            self.right.for_each(fn)   
        
            

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        #lowest number is always furthest to left
        #base case?
        if node is None:
            return None
        if node.left is None:
            print(node.value)
            self.in_order_print(node.right)
        if node.left is not None:
            #check if node.left has a value to its left
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)
        
            

        #recursive case? (gets us closer to base case)
        # self.in_order_print(self.left)
        #your call stack is your clue










    
#     class Queue():
#     #Storage?
#     def __init__(self, size=None, storage=None):
#         self.size = 0
#         self.storage = LinkedList()
#     #Find length of linkedlist
#     def __len__(self):
#         current = self.storage.head
#         length = 0
#         while current:
#             length = length + 1
#             current = current.next_node
#         return length
#     #add to the end of linked list (tail)
#     def enqueue(self, value):
#         return self.storage.add_to_tail(value)
#     #Take away first item from queue
#     def dequeue(self):
#         return self.storage.remove_head()
# #need to instantiate queue????

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        #use a queue
        #start queue with root node

        #while loop that checks size of queue
            #pointer variable
            #that updates at the beginning of each loop
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        #stack
        #start stack with root node

        #use while loop that checks stack size
            #use pointer
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
