
# IO
```python
n = int(input())
a, b = input().split()
a, b = int(a), int(b)
print(a)
```

# 字母数字转化
```python
num = ord(char)
char = ord(num)
```
# 数据结构

## Dict
```python
d = {}
if item in d
d.keys()
d.values()
d.pop(item)
d.pop(item, None)
d.items()
len(d)
```
## Defaultdict
```python
from collections import defaultdict
d = defaultdict([int, list, set, lambda: value])
d[newkey] += 1
d.get(key, default)
```
## Counter
```python
from collections import Counter
cnt = Counter()
cnt[var] += 1
cnt.pop[var]
cnt.elements() -> [var * cnt[var]]
cnt.total() -> cnt[var1] + ...
cnt.most_common()
+ - &交集 |并集 == <=
```

| 特性    | dict (字典)                                   | collections.Counter (计数器)                                      |
| ----- | ------------------------------------------- | -------------------------------------------------------------- |
| 主要用途  | 通用的数据存储，映射任意键到任意值。                          | 专门用于计算==可哈希对象==的出现次数。                                          |
| 处理缺失键 | 访问不存在的键会引发KeyError异常。                       | 访问==不存在的键会返回0==，不会报错。                                          |
| 初始化   | 可以通过多种方式创建，包括字面量{}和dict()构造函数。              | 可以接受一个可迭代对象直接进行计数初始化。                                          |
| 特有方法  | 具备如get(), keys(), values(), items()等标准字典方法。 | 额外提供了most_common(), elements(), subtract(), update()的==增强功能==。 |
| 数学运算  | 不直接支持数学运算。                                  | 支持加、减、交集和并集等操作。                                                |

## Queue
```python
from queue import Queue
que = Queue(maxsize) # FIFO
LifoQueue(maxsize) # maxsize <= 0 -> inf size
PriorityQueue(maxsize) # lowest first
Que.put(item)
q.qsize()
q.empty()
q.full()
q.get() # w remove
```

## Deque
从 deque 的任一端添加和弹出条目，在两个方向上的大致性能均为 _O_(1)
```python
from collections import deque
dq.append()
appendleft()
clear()
copy()
count(x) # count var == x
extend(iter_var) # to the right
extendleft(iter_var)
index(x)
insert(i, x)
pop() # rightmost, if no element raise Index Error
popleft() # leftmost
remove() # remove first or Value Error
reverse() # -> None
rotate(n_steps) # > 0 to the right, < 0 to the left
```
## OrderedDict
擅长重新排序
## Heapq
```python
import heapq
pq = []
heapq.heappush(pq, item) # heappush_max
item = heapq.heappop(pq) # heappop_max
heapq.heapify(x) # heapify_max
```
