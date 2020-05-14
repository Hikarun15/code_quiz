import random

key = random.randint(1, 10)
print(str(key) + "が含まれるかチェック")

# 線形探索
def linear_search(arr):
	for i in len(arr):
		if key ==  arr[i]:
			return i
	return None

s_list = [1, 2, 5, 8, 10]
print(linear_search(s_list))

#二分探索
def binary_search(arr):
	left = 0
	right = len(arr)
	while left < right:
		mid = (left+right) // 2
		if arr[mid] == key:
			return mid
		elif arr[mid] > key:
			right = mid
		else:
			left = mid + 1
	return None

s_list = [1, 2, 5, 8, 10]
print(binary_search(s_list))