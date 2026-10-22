"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        def dfs(node, seen = {}):
            if node == []:
                return seen
            if node in seen:
                return seen[node]

            copy = Node(node.val)
            seen[node] = copy
            if node.neighbors and node.neighbors != []:
                for n in node.neighbors:
                
                    neigh = n
                
                    copy.neighbors.append(dfs(neigh, seen))
                
               
                 
                

            return copy
        
       
        node_copy = dfs(node)
        print(node_copy.val, "final") 
      

        return node_copy
         

        