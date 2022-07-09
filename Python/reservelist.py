def reserve(n):
    n = n[::-1]
    for i in range(0,len(n)):
        if type(n[i]) is list:
            n[i] = n[i][::-1]
     return n


a = [[1, 2], [3, 4], [5, 6, 7]]
print(reserve(a))