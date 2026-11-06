from typing import List
from collections import defaultdict

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs by request time.
        # logs[i] = [server_id, time]
        logs.sort(key=lambda log: log[1])

        # Sort queries by time, but remember original index
        # so answers can be placed correctly.
        indexed_queries = sorted((q, i) for i, q in enumerate(queries))

        freq = defaultdict(int)  # freq[server_id] = active request count
        active_servers = 0       # distinct server IDs in current window
        add = 0                  # next request to add
        remove = 0               # next request to remove
        ans = [0] * len(queries)

        for query, original_index in indexed_queries:
            lower_bound = query - x

            # Add every request with time <= query.
            while add < len(logs) and logs[add][1] <= query:
                server_id = logs[add][0]

                if freq[server_id] == 0:
                    active_servers += 1

                freq[server_id] += 1
                add += 1

            # Remove every request with time < query - x.
            while remove < len(logs) and logs[remove][1] < lower_bound:
                server_id = logs[remove][0]

                freq[server_id] -= 1

                if freq[server_id] == 0:
                    active_servers -= 1

                remove += 1

            # Servers with zero requests = total servers - active servers.
            ans[original_index] = n - active_servers

        return ans