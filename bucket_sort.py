def bucket_sort(arr):
	arrc = [0] * (max(arr)+1)
	for i in arr:
		arrc[i] += 1
	for j in range(1, len(arrc)):
		arrc[j] = arrc[j] + arrc[j-1]
	arrs = [0] * len(arr)
	for i in arr:
		arrs[arrc[i]-1] = i
		arrc[i] -= 1
	return arrs

org_list = [2, 5, 1, 4, 6, 3]	
print(bucket_sort(org_list))