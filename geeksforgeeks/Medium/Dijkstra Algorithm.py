import heapq
class Solution:
    def dijkstra(self, adj: list[list[list[int]]], src: int) -> list[int]:
        '''adj = [[] for _ in range(V)]
        for u,v,d in edges:
            adj[u].append([v,d])'''
        
        #distance = [float("-inf") for _ in range(V)]
        n=len(adj)
        distance = [float("inf")]*n
        distance[src] = 0
        priority_queue = [[0,src]]
        
        
        #while len(priority_queue) !=0:
        while priority_queue:
            currnt_dist,node = heapq.heappop(priority_queue)
            if currnt_dist>distance[node]:
                continue
            for adjNode,weight in adj[node]:
                dist_travl = currnt_dist+weight
                if dist_travl< distance[adjNode]:
                    distance[adjNode] = dist_travl
                    heapq.heappush(priority_queue, ([dist_travl, adjNode]))
                    #priority_queue.append([dist_travl,adjNode])
        return distance

if __name__ == "__main__":
    n=int(input("Enter Number of edges : "))
    graph = [0 for _ in range(n+1)]
    
    
        