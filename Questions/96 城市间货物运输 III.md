```python
ncity, nroad = map(int, input().split())

edges = []
for _ in range(nroad):
    edges.append(tuple(map(int, input().split())))

src, dst, k = map(int, input().split())

distances = [float('inf') for _ in range(ncity + 1)] 
distances[src] = 0 # 不要忘记初始化

for round in range(k + 1):
    backup = distances[:]
    for s, t, v in edges:
        if backup[s] + v < distances[t]:
            distances[t] = backup[s] + v

if distances[dst] == float('inf'):
    print("unreachable")
else:
    print(distances[dst])
```

# queue
```python
from collections import deque

ncity, nroad = map(int, input().split())

edges = [[] for _ in range(ncity + 1)]
for _ in range(nroad):
    s, t, v = map(int, input().split())
    edges[s].append((t, v))

src, dst, k = map(int, input().split())

distances = [[float('inf')] * (k + 2) for _ in range(ncity + 1)] # step, cost

q = deque([(src, 0, 0)]) # node, cost, step

distances[src][0] = 0

min_answer = float('inf')

while q:
    u, cost, steps = q.popleft()
    
    if steps >= k + 1:
        continue
    
    if cost > distances[u][steps]:
        continue

    for v, w in edges[u]:
        new_cost = cost + w
        new_steps = steps + 1
        
        if new_cost < distances[v][new_steps]:
            distances[v][new_steps] = new_cost
            q.append((v, new_cost, new_steps))

ans = float('inf')
for s in range(k + 2):
    ans = min(ans, distances[dst][s])

if ans == float('inf'):
    print("unreachable")
else:
    print(ans)
```