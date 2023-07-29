a=int(input("정수를 입력하세요 : "))

def sum(b):
    c = 0
    for i in range(0,b+1):
        c+=i
    return c

print(sum(a))