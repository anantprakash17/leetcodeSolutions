# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head == None:
            return None
        array = []
        
        # Convert the singly linked list into a list to make it
        # easier to work with.
        while head:
            array.append(head.val)
            head=head.next
        
        # This function simple recursivly builds the tree from the midpoint of the list.
        def recurseTree(array: list) -> TreeNode:
            if array == []:
                return None
            
            midPoint = len(array)//2
            
            #Build the left and right of the tree by using the left and 
            # right of the list because it is already sorted. 
            treeRoot = TreeNode(array[midPoint])
            treeRoot.left = recurseTree(array[:midPoint])
            treeRoot.right = recurseTree(array[midPoint + 1:])
            
            return treeRoot
        
        return recurseTree(array)
        
        
