# マージソート（分割統治法）
def merge_sort(arr):
	if len(arr) < 2:
		return arr
	mid = len(arr) // 2
	return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

# マージ
def merge(arrf, arrb):
	if len(arrf) < 1:
		return arrb
	if len(arrb) < 1:
		return arrf
	if arrf[0] <= arrb[0]:
		return [arrf[0]] + merge(arrf[1:], arrb)
	else:
		return [arrb[0]] + merge(arrf, arrb[1:])
	
	

org_list = [2, 5, 1, 4, 6, 3]	
print(merge_sort(org_list))