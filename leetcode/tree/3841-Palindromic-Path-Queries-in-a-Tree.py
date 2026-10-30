class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        size = [1] * n
        heavy = [-1] * n

        # Iterative DFS: parent, depth, order
        order = []
        stack = [0]
        visited = [False] * n
        visited[0] = True

        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    stack.append(v)

        # Subtree sizes
        for u in reversed(order):
            p = parent[u]
            if p != -1:
                size[p] += size[u]

        # Heavy child
        for u in range(n):
            best, best_size = -1, 0
            for v in adj[u]:
                if v != parent[u] and size[v] > best_size:
                    best, best_size = v, size[v]
            heavy[u] = best

        head = [0] * n
        pos = [0] * n
        cur = 0

        # Iterative heavy-light decomposition
        stack = [0]
        visited = [False] * n
        visited[0] = True

        while stack:
            u = stack.pop()
            chain = []
            x = u
            while x != -1:
                visited[x] = True
                chain.append(x)
                x = heavy[x]

            for x in chain:
                head[x] = u
                pos[x] = cur
                cur += 1

            for x in chain:
                for v in adj[x]:
                    if v != parent[x] and v != heavy[x] and not visited[v]:
                        stack.append(v)

        # XOR segment tree over HLD positions
        base = [0] * n
        for u in range(n):
            base[pos[u]] = 1 << (ord(s[u]) - 97)

        tree_n = 1
        while tree_n < n:
            tree_n <<= 1

        tree = [0] * (2 * tree_n)
        tree[tree_n:tree_n + n] = base
        for i in range(tree_n - 1, 0, -1):
            tree[i] = tree[2 * i] ^ tree[2 * i + 1]

        def update(i: int, value: int) -> None:
            i += tree_n
            tree[i] = value
            i >>= 1
            while i:
                tree[i] = tree[2 * i] ^ tree[2 * i + 1]
                i >>= 1

        def query(l: int, r: int) -> int:  # inclusive [l, r]
            res = 0
            l += tree_n
            r += tree_n + 1
            while l < r:
                if l & 1:
                    res ^= tree[l]
                    l += 1
                if r & 1:
                    r -= 1
                    res ^= tree[r]
                l >>= 1
                r >>= 1
            return res

        def path_xor(u: int, v: int) -> int:
            res = 0
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u
                res ^= query(pos[head[u]], pos[u])
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u
            res ^= query(pos[u], pos[v])
            return res

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u, c = int(parts[1]), parts[2]
                update(pos[u], 1 << (ord(c) - 97))
            else:
                u, v = int(parts[1]), int(parts[2])
                mask = path_xor(u, v)
                ans.append(mask & (mask - 1) == 0)

        return ans