
# 二分查找
import bisect
list_data = list(range(0, 10, 2))
index = bisect.bisect(list_data, 3, lo=1, hi=4)
print(index)