A=[6,4,2,8,9,3]

def max(a):
    a=A[0]
    for i in A:
        if i > a:
            a = i
    return a

print(A.index(max(A)))