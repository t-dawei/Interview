
# ========================
# 求字符串重新排列的所有结果
# 思路：确定首位 然后递归确定第二位 再递归确定第三位... 跳出递归条件为输入s长度为1 
# ========================
def permute(self, nums: List[int]) -> List[List[int]]:
    
    res = []
    def helper(tmp_nums, seq):
        if not tmp_nums:
            res.append(seq)
            
        for j in range(len(tmp_nums)):
            helper(tmp_nums[:j] + tmp_nums[j+1:], seq + [tmp_nums[j]])
    
    helper(nums, [])

# =========================
# 判断一个数是否为2的整数幂
# 思路：2的整数幂在转化为2进制后 其首位都为1， 其余位都为0
#		利用比2的整数幂小1的数 进行与运算 结果为0 则为2的整数幂
# ========================
def power2(data):
	res = data & (data-1)
	# print(type(res), res)
	return res == 0

# ========================
# 归并排序思想:
# 利用归并排序的思想，先将两个数组排好序，然后比较两个数组的大小，
# 若第一个数组的元素小于第二个数组的元素，
# 则第一个数组的元素往后挪，反之，第二个数组的元素往后挪
# ========================
def guibingpaixu(list1, list2):

	len1 = len(list1)
	len2 = len(list2)
	p1 = p2 = 0
	res = []
	while  p1 < len1 and p2 < len2:
		if list1[p1] < list2[p2]:
			res.append(list1[p1])
			p1 += 1
		elif list1[p1] >= list2[p2]:
			res.append(list2[p2])
			p2 += 1
	# res = res + list1[p1:] + list2[P2:]
	res += list1[p1:] or list2[p2:]
	return res
	

# ========================
# 二分查找
# ========================

def erfenchazhao(data, K):
    left, right = 0, len(data)

    while left != right:
        mid = (left + right) // 2
        if data[mid] < K:
            left = mid+1
        elif data[mid] > K:
            right = mid-1
        else:
            print(mid)
    return mid

# ========================
# 树 ---（深度优先） 先序遍历 中序遍历 后序遍历 ---- 递归算法与非递归算法
# ========================
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def pre_trans(root):
    res = []
    if root:
        res.append(root.val)
        res += pre_trans(root.left)
        res += pre_trans(root.right)
    return res

def mid_trans(root):
    res = []
    if root:
        res += mid_trans(root.left)
        res.append(root.val)
        res += mid_trans(root.right)
    return res

def later_trans(root):
    res = []
    if root:
        res += later_trans(root.left)
        res += later_trans(root.right)
        res.append(root.val)
    return res

# 非递归遍历
def pre_trans_2(root):
    list_stack, res = [], []
    while root or list_stack:
        while root:
            res.append(root.val)
            list_stack.append(root)
            root = root.left
        if list_stack:
            root = list_stack.pop()
            root = root.right
    return res

def mid_trans_2(root):
    list_stack, res = [], []
    while root or list_stack:
        while root:
            list_stack.append(root)
            root = root.left
        if list_stack:
            root = list_stack.pop()
            res.append(root.val)
            root = root.right
    return res

def post_trans_2(root):
    list_stack, res = [], []
    pre = None
    list_stack.append(root)
    while list_stack:
        cur = list_stack[-1]
        # 如果当前结点没有子节点或者子节点都被访问了
        if (cur.left is None and cur.right is None) or ((pre is not None) and (pre == cur.left or pre == cur.right)):
            res.append(cur.val)
            list_stack.pop()
            pre = cur
        else:
            if cur.right is not None:
                list_stack.append(cur.right)
            if cur.left is not None:
                list_stack.append(cur.left)
    return res

# ========================
# 树 --- 层次遍历（广度优先）
# ========================
def level_trans(root):
    list_queue, res = [root], []
    while list_queue:
        cur = list_queue.pop()
        res.append(cur.val)
        if cur.left:
            list_queue.append(cur.left)
        if cur.right:
            list_queue.append(cur.right)
    return res

# =========================
# 树 转化 图链式表示
# =========================
import collections
conn = collections.defaultdict(list)
def connect(parent, child):
    if parent and child:
        conn[parent.val].append(child.val)
        conn[child.val].append(parent.val)
    if child.left: connect(child, child.left)
    if child.right: connect(child, child.right)


# ============================
# 图 深度遍历 图的链式表示 递归实现（通过栈实现）
# ============================
list_visited = []

def dfs(node):
	list_visited.append(node)
	for n in neighbor[node]:
		if n not in list_visited:
			dfs(n)


# ==============================
# 图 广度遍历 图的链式表示 非递归实现（通过队列实现）
# ==============================
def bfs(node):
	list_queue = [node]
	list_visited = []
	while list_queue:
		node = list_queue.pop()
		list_visited.append(node)
		for n in neighbor[node]:
			if n not in list_visited:
				list_queue.append()
	return list_visited

# 快速排序
def q_sort(L, left, right):
    if left < right:
        pivot = Partition(L, left, right)
        q_sort(L, left, pivot - 1)
        q_sort(L, pivot + 1, right)
    return L

def Partition(L, left, right):
    pivotkey = L[left]

    while left < right:
        while left < right and L[right] >= pivotkey:
            right -= 1
        L[left] = L[right]
        while left < right and L[left] <= pivotkey:
            left += 1
        L[right] = L[left]

    L[left] = pivotkey
    return left

def quickSort2(data):
    if len(data) < 2:
        return data
    else:
        pos = data[0]
        left = [w for w in data if w < pos]
        mid = [w for w in data if w == pos]
        right = [w for w in data if w > pos]
        return quickSort2(left) + mid + quickSort2(right)


'''
KMP 算法
'''

# 对模式窜求next数组
def call_next(modestr):
    if not modestr:
        return []

    _next = [None] * len(modestr)

    # 设置首位为-1 方便代码判断用
    _next[0] = -1

    # 设置索引i 为模式串遍历索引， k为模式串回溯索引
    i, k = 0, -1
    while i < len(modestr)-1:
        if k == -1 or modestr[i] == modestr[k]:
            i += 1
            k += 1
            _next[i] = k
        else:
            k = _next[k]
    return _next

def kmp(mainstr, modestr, _next):

    # i 为mainstr 的索引， j为modestr索引
    i, j = 0, 0
    while i < len(mainstr) and j < len(modestr):
        if j == -1 or mainstr[i] == modestr[j]:
            i += 1
            j += 1
        else:
            j = _next[j]

    if j == len(modestr):
        return mainstr[i-len(modestr):i]
    else:
        return None


# 递归回溯
# 机器人的运动范围
def robot_moving(m, n, k):
    visited = [[0] * n for _ in range(m)]

    core(m, n, k, 0, 0, visited)
    print(visited)
    count = 0
    for col in visited:
        for i in col:
            if i == 1:
                count += 1
    print(count)


def core(m, n, k, i, j, visited):
    sum_ = sum(numsplit(i) + numsplit(j))
    if sum_ <= k and 0 <= i < m and 0 <= j < n and not visited[i][j]:
        visited[i][j] = 1
        core(m, n, k, i+1, j, visited)
        core(m, n, k, i-1, j, visited)
        core(m, n, k, i, j+1, visited)
        core(m, n, k, i, j-1, visited)


def numsplit(num):
    if num == 0:
        return [0]
    res = []
    while num > 0:
        x = num % 10
        res.append(x)
        num = num // 10
    return res


# 递归回溯 剪纸模版
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        def backtrack(i, tmp_sum, tmp):
            if tmp_sum == target:
                res.append(tmp)
                return 
            for j in range(i, n):
                # 剪枝
                if tmp_sum + candidates[j] > target:
                    break
                backtrack(j,tmp_sum + candidates[j],tmp+[candidates[j]])
        backtrack(0, 0, [])
        return res

if __name__ == '__main__':
    '''
    L = [1, 3, 9, 8, 4, 1]
    left = 0
    right = len(L)-1
    print(q_sort(L, left, right))
    print(quickSort2(L))
    _next = call_next('ababc')
    print(kmp('aabcababc', 'abab', _next))
    '''
    robot_moving(100, 100, 10)
    # numsplit(3450)