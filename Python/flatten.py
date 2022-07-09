new = []
def flatten(n):
    for i in n:
        if type(i) is list:
            flatten(i)
        else:
            new.append(i)
    return new

a = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

print(flatten(a))