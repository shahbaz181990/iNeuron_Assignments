import numpy as np


def numpy_assignment(x, n):
    # Counter Variable
    temp = 0
    # Final Array
    ans = []
    # Variable used to store the temp ans
    gm_sum = 0
    while temp < (len(x) - n + 1):
        for i in range(n):
            gm_sum += x[i]
        final = gm_sum // n
        ans.append(final)
        x.append(x.pop(0))
        temp += 1
        gm_sum = 0
    return ans


x = list(map(int, input().split()))
n = int(input())
ans = numpy_assignment(x, n)
print(ans)
