#　クイックソート（分割統治法）


def quick_sort(arr):
	if len(arr) < 2:
		return arr
	p = arr[0]
	arrf, arrb = devide(p, arr[1:])
	return quick_sort(arrf) + [p] + quick_sort(arrb)

def devide(p, arr):
	left = []
	right = []
	for i in arr:
		if i < p:
			left.append(i)
		else:
			right.append(i)
	return left, right

org_list = [2, 5, 1, 4, 6, 3]	
print(quick_sort(org_list))


#　リスト内包表記

def quick_sort(arr):
	if len(arr) < 2:
		return arr
	p = arr[0]
	left = [i for i in arr[1:] if i < p]
	right = [i for i in arr[1:] if i >= p]

	return quick_sort(left) +  [p] + quick_sort(right)


# devide() 分割統治法

def quick_sort(arr):
	if len(arr) < 2:
		return arr
	p = arr[0]
	arrf, arrb = divide(p, arr[1:])
	return quick_sort(arrf) + [p] + quick_sort(arrb)

def divide(p, arr):
	if len(arr) < 1:
		return [], []
	arrf, arrb = divide(p, arr[1:])
	top = arr[0]
	if top < p:
		return [top] + arrf, arrb
	else:
		return arrf, [top] + arrb

org_list = [2, 5, 1, 4, 6, 3]	
print(quick_sort(org_list))