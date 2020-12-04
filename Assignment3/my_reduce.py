# reduce(my_add, numbers, 100)

# create your function here
my_func = lambda x, y: x + y

# Reduce function  
def my_reduce(my_func, li, n=0):
    ans = 0
    for i in li:
        ans = my_func(i, ans) + n
    return ans

# input data
li = list(map(int, input().split()))
# print output
print(my_reduce(my_func, li))

