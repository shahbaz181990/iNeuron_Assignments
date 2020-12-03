def my_filter(li, my_func=lambda x: x):
    for i in li:
        if my_func(i):
            print(i, end=' ')
    print()


# taking a list as input
li1 = list(map(int, input().split()))
# specifying the function which we want to calculate, by default it will return the value as is.
my_filter(li1, lambda x: x % 2 != 0)


