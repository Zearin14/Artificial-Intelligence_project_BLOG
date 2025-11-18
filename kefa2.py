import sys
sys.setrecursionlimit(2000000)
input = sys.stdin.readline

n, m = map(int, input().split())
cats = list(map(int, input().split()))

adj = [[] for _ in range(n)]

# Read EXACTLY n-1 edges (so no waiting for more input)
for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * n
ans = 0

def dfs(u, consecutive):
    global ans
    visited[u] = True

    if cats[u] == 1:
        consecutive += 1
    else:
        consecutive = 0

    if consecutive > m:
        return

    leaf = True
    for v in adj[u]:
        if not visited[v]:
            leaf = False
            dfs(v, consecutive)

    if leaf:
        ans += 1

dfs(0, 0)
print(ans)
