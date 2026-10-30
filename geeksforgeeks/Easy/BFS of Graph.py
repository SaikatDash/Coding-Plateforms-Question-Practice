from collections import deque
class Solution:
    def bfs(self, adj):
        #visited = []
        n=len(adj)
        ans=[]
        visited=[0]*n
        queue=deque()
        queue.append(0)
        visited[0]=1
        '''
        queue.append(starting_node)
        visited[starting_node]=1
        if len(queue) !=0:
            e=queue.popleft()
            ans.append(e)'''
        while len(queue) !=0:
            e=queue.popleft()
            ans.append(e)
            for node in adj[e]:
                if visited[node]==0:
                    queue.append(node)
                    visited[node]=1
        return ans