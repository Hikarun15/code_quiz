
def fate():
    sum = 0
    if n == 0:
        return 0

    for i in range(n):
   
        t[i], l[i] = input().split()
        time = list(t[i])
        lg = int(l[i])

        if lg > A:
            lg = lg - A
            k = lg // C 
            sum = sum + B + D * k
        else:
             sum += B
    
        if time[0] == 2 and (time[1] == 2 or time[1] == 3):
            sum = int(sum * 1.2)
    return sum

A, B, C, D = (int(x) for x in input().split())
n = int(input())
t = [0] * n
l = [0] * n

print(fate())

# 3 4 6 1
# 2
# 10:25 1500
# 23:40 2001
# 592


# def fate():
#     sum = 0
#     if n == 0:
#         return 0

#     for i in range(n):
   
#         t, l = input().split()
#         time = list(t)
#         lg = int(l)

#         if lg > A:
#             lg = lg - A
#             k = lg // C 
#             sum = sum + B + D * k
#         else:
#              sum += B
    
#         if time[0] == 2 and (time[1] == 2 or time[1] == 3):
#             sum = int(sum * 1.2)
#     return sum


    
