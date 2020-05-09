s = input().split()

stack = []
count = 0
flag = 1

result = 0

for i in range(len(s)):
	if s[i] == "+":
		if count < 2:	
			flag = 0
			break	
		count -= 2
		stack[count] = stack[count] + stack[count + 1]
		stack.pop(count + 1)
		count += 1
	elif s[i] == "-":
		if count < 2:
			flag = 0
			break
		count -= 2
		stack[count] = stack[count] - stack[count + 1]
		stack.pop(count + 1)
		count += 1
	elif s[i] == "*":
		if count < 2:
			flag = 0
			break
		count -= 2
		stack[count] = stack[count] * stack[count + 1]
		stack.pop(count + 1)
		count += 1
	elif s[i] == "++":
		if count < 1:
			flag = 0
			break
		stack[count] += 1
	elif s[i] == "@":
		if count < 3:
			flag = 0
			break
		count -= 3
		stack[count] = stack[count] * stack[count + 1] + stack[count + 1] * stack[count + 2] + stack[count + 2] * stack[count]
		stack.pop(count + 1)
		stack.pop(count + 1)
		count += 1
	else:
		stack.append(int(s[i]))
		count += 1

if len(stack) > 1 or flag == 0:
	flag = 0
else:
	result = stack[0]

if flag == 0:
	print("Invalid")
else:
	print(result)




