# 序列
序列是元素的有序集合，通常通过整数索引访问。
- List：动态数组
	- append()
- collections.namedtuple：元组
	- 可以用名字而非序号来指定元组里的元素
	- collections.namedtuple(name, \*\*attributes)
	- Name(\*\*attributes)
	- t[1], t.attr
- Bytearray：动态数组
	- 可变的字节序列
	- bytearray(b'text'), bytearray([typle, list])
	- t[0], t.append(b't')
- LinkedList：自定义
	- 一个域表示值，另一个表示指针
	- 单链表、双链表、环

# 集合
- Set：哈希表
	- 可变集合
	- set(list)，.add()，.remove()不存在会报错，.discard() 不存在不会报错，.clear()
- Frozen Set: 哈希表
	- 不可变集合，可以作为字典的键
	- frozenset(alist)

# 字典
- collections.Counter：dict
	- 无序字典
	- Counter([None, str, dict, \*\*key=val])
	- del c['key']
	- elements() w repeat
	- most_common([n])-> list of tuple
	- total()
	- subtract()
	- update() adds the new counts to existing
- collections.OrderedDict：dict
	- 有序字典（记住插入顺序）
	- popitem(last=True) 
	- move_to_end(item, last=True)
- collections.defaultdict：dict
	- 对象不存在时提供默认值
- collections.ChainMap：list
	- 封装了多个字典


# 队列
- Queue：数组
	- FIFO
	- 用list和append pop(0)实现
	- 用collections.deque实现（双端都可以增删）（双向链表）
		- deque(), .append(), .appendleft(), .pop(), .popleft()
	- 用queue.Queue实现（deque）
		- qsize() empty() full() put() get()
- Stack：数组
	- LIFO
	- 用list和append pop实现
	- 用collections.deque实现
	- 用queue.LifoQueue实现
- Priority Queue / Heap：二叉树、数组
	- 优先级决定出栈顺序
	- heapq
		- heapq.heapify(alist) heappush(alist, (pri, item)) heappop(alist)
	- queue.PriorityQueue
		- PriorityQueue(), put((pri, item)), get()

# 树与图
- Binary Tree：自定义
	- DFS
		- Inorder：左根右
		- Preorder：根左右
		- Postorder：左右根
	- BFS
		- 用FIFO队列
- Graph：自定义
	- Adjacency Matrix
	- Adjacency List：二维数组，第i行内容表示与第i个顶点连接的列表（连接方向？）
	- BFS：Queue
	- DFS：递归

# 对比

| **数据结构**       | **主要优势 (平均)**                    | **主要局限**          |
| -------------- | -------------------------------- | ----------------- |
| **数组**         | 查找: **O(1)**，内存效率高，缓存友好          | 大小固定，插入/删除: O(n)  |
| **链表**         | 插入/删除: **O(1)**，大小灵活             | 查找: O(n)，内存效率低    |
| **哈希表**        | 查找/插入/删除: **O(1)**               | 无序, 空间开销, 最坏 O(n) |
| **栈 (Stack)**  | 顶部插入/删除: **O(1)**                | 只能访问顶部            |
| **队列 (Queue)** | 两端插入/删除: **O(1)**                | 只能访问两端            |
| **平衡BST**      | 查找/插入/删除: **O(log n)**           | 空间开销，实现复杂，嗑退化     |
| **堆 (Heap)**   | 查找极值: O(1), 插入/删极值: **O(log n)** | 查找非极值: O(n)       |
| 图              | 灵活                               | 实现复杂，算法复杂         |
