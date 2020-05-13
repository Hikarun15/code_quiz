#動的計画法

def fib_memo(n):
	memo = [None]*(n+1)

	def fib(n):
		if n == 0 or n == 1:
			return 1
		if memo[n] != None:
			return memo[n]
		memo[n] = fib(n-1) + fib(n-2)
		return memo[n]
	
	return fib(n)
	
for i in range(35):
	print(fib_memo(i))