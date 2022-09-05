import collections
import heapq
import math


def optimised_bellman_ford_dfs(adj: list[list[tuple]], source: int) -> list:
    N = len(adj)
    dis = [math.inf] * N
    dis[source] = 0

    def dfs(i=source, d=0):
        if d < dis[i]:
            dis[i] = d
            for j, w in adj[i]:
                dfs(j, w + d)
    dfs()
    return dis


def dikstra(adj: list[list[tuple]], source: int) -> list:
    N = len(adj)
    dis = [math.inf] * N
    dis[source] = 0
    q = [(source, 0)]
    while q:
        i, di = heapq.heappop(q)
        if di > dis[i]: continue
        for j, wj in adj[i]:
            if wj + di < dis[j]:
                dis[j] = wj + di
                q.append((j, dis[j]))
    return dis

if __name__ == '__main__':
    a = collections.defaultdict(lambda : math.inf)
    print(a[0])
    if 0 < a[1]: a[1] = 0
    print(a[1])