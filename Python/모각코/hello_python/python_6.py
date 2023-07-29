#1
print("1번")
count=0

for i in range(1,101):
    if i%2 == 0:
        if i%7 != 0:
            count+=1

print("1부터 100까지의 수 중에서 짝수이면서 7의 배수가 아닌 수 : [",count,"]개")

#2
print("")
print("2번")
add = 0
while True:
    a=int(input("숫자를 입력하세요 : "))
    if a!=0:
        add=add+a
    else :
        print(add)
        break
