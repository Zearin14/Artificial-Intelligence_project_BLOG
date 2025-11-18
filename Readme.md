Problem Overview
Kefa wants to visit a restaurant located in a park represented as a tree of n vertices (nodes).
Each vertex may or may not have a cat.
Kefa’s mother, however, set one condition:
He cannot go through more than m consecutive vertices that have cats.
Kefa starts at vertex 1 (the root) and wants to visit leaf nodes (restaurants).
We must find how many leaf nodes Kefa can reach without exceeding the limit of consecutive cat nodes.
Algorithm Choice: Depth-First Search (DFS)
We use DFS (Depth-First Search) — a fundamental AI search algorithm — to explore all paths from the root to leaves.
Why DFS?
DFS is ideal for this problem because:
•	It explores complete paths recursively before backtracking.
•	It naturally fits tree traversal.
•	We can easily carry and reset the “consecutive cats” count as we move along the path.
DFS is widely used in AI for:
•	State-space search
•	Pathfinding
•	Constraint satisfaction problems

 Python Implementation
# Kefa and Park - Codeforces 580C
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


Example Input
7 1
1 0 1 1 0 0 0
1 2
1 3
2 4
2 5
3 6
3 7
Example Output
2

 
Problem Breakdown
We’re given a tree graph, so:
•	There is exactly one path between any two vertices.
•	We can represent it using an adjacency list.
•	Starting from node 1, we explore all paths to leaves.
•	We maintain a counter of consecutive cat nodes and stop exploring when the count exceeds m.
•	Whenever we reach a leaf within the limit, we increase our valid restaurant count.



Step-by-Step Explanation
Step	Action	Description
1	Read Input	Get number of vertices n, cat limit m, and cat presence list.
2	Build Graph	Create adjacency list to represent connections between vertices.
3	DFS Function	Traverse each path from root (node 1). Track consecutive cats.
4	Constraint Check	Stop exploring when consecutive > m.
5	Leaf Detection	If a node is a leaf (no children except its parent), count it.
6	Print Result	Total count of valid restaurant paths.

Complexity Analysis
Type	Analysis
Time Complexity	O(n) — each node is visited once
Space Complexity	O(n) — recursion stack and adjacency list

AI Insight
This problem reflects how AI search algorithms like DFS can efficiently explore decision spaces under constraints.
By pruning invalid paths early (when the constraint is violated), the algorithm mimics intelligent decision-making — exploring only viable solutions.
Conclusion
This project demonstrates how Depth-First Search (DFS) — a simple yet powerful AI search algorithm — can be adapted for real-world decision problems with constraints.
By applying recursive exploration, Kefa’s pathfinding problem is efficiently solved with minimal computational cost.


