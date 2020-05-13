# # 選択ソート

# def select_sort(arr):
# 	for i in range(len(arr) - 1):
# 		select_min(arr, i)

# def select_min(arr, i):
# 	min = i
# 	for j in range(i+1,len(arr)):
# 		if arr[min] > arr[j]:
# 			min = j
# 	arr[i], arr[min] = arr[min], arr[i]


# org_list = [17,11, 12, 5, 14, 9, 6, 16, 4, 10]	
# select_sort(org_list)
# print(org_list)


# # 挿入ソート

# def insert_sort(arr):
# 	for i in range(1, len(arr)):
# 		insert_min(arr, i)

# def insert_min(arr ,i):
# 	temp = arr[i]
# 	for j in range(i - 1, -1, -1):
# 		if temp < arr[j]:
# 			arr[j+1] = arr[j]
# 		else:
# 			arr[j+1] = temp 
# 			break
# 	else:
# 		arr[0] = temp

# org_list = [17,11, 12, 5, 14, 9, 6, 16, 4, 10]	
# insert_sort(org_list)
# print(org_list)

# バブルソート
def bubble_sort(arr):
	for i in range(len(arr)-1):
		exchange(arr,i)

def exchange(arr,i):	
	for j in range(len(arr)-1,i, -1):
		if arr[j-1] > arr[j]:
			arr[j-1], arr[j] = arr[j], arr[j-1]

org_list = [17,11, 12, 5, 14, 9, 6, 16, 4, 10]	
bubble_sort(org_list)
print(org_list)