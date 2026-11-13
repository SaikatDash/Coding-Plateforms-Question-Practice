''' 
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def findCommon(self, r1: 'Node', r2: 'Node') -> list[int]:
        def inorder(root, values):
            stack = []
            curr = root

            while stack or curr:
                while curr:
                    stack.append(curr)
                    curr = curr.left

                curr = stack.pop()
                values.append(curr.data)
                curr = curr.right

        a, b = [], []
        inorder(r1, a)
        inorder(r2, b)

        ans = []
        i = j = 0

        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                if not ans or ans[-1] != a[i]:
                    ans.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1

        return ans