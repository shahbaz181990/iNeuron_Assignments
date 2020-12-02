

# Take input from user
n = int(input())

# This for loop will print the first part of the pattern in increasing order from 1 to n
for i in range(n):
    for j in range(i):
        print("*", end=" ")
    print()

# This for loop will print the first part of the pattern in decreasing order from n to 1
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
