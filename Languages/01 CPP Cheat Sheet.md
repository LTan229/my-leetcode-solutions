
|      | Python       | C++                             |
| ---- | ------------ | ------------------------------- |
| 动态数组 | `list`       | `vector<int> res;`              |
| 添加元素 | `.append()`  | `.push_back()`                  |
| 数组长度 | `len(arr)`   | `arr.size()`                    |
| 哈希表  | `dict`       | `unordered_map<int, int> mp;`   |
| 哈希集合 | `set`        | `unordered_set<int> st;`        |
| 排序   | `arr.sort()` | `sort(arr.begin(), arr.end());` |
| 字符串  | `str`        | `string s = "";`                |
| 打印输出 | `print()`    | `cout << x << endl;`            |
# Vector

```cpp
vector<int> nums; // Python: nums = []
vector<int> nums(n); // Python: nums = [0] * n
vector<int> nums(n, -1); // Python: nums = [-1] * n
vector<int> nums = {1, 2, 3}; // Python: nums = [1, 2, 3]
vector<vector<int>> matrix(m, vector<int>(n, 0));  // Python: nums = [[0] * n for _ in m]
```

# Unordered_map

```cpp
unordered_map<int, int> mp; // Python: mp = {}
unordered_map<string, int> mp = { {"apple", 1}, {"banana", 2} };
mp[key] = value;
if (mp.count(key))
```

# Unordered_set

```cpp
unordered_set<int> st; // Python: st = set()
unordered_set<int> st = {1, 2, 3}; // Python: st = {1, 2, 3}
st.insert(1); // Python: st.add(1)
```

# Head

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm> // sort
using namespace std; 
```

# Sort

```cpp
sort(nums.begin(), nums.end());
```
