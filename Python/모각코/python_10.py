from doctest import Example

list=[1,2,3,4,5,6,7]
add=0

for i in list:
    a = int(input("정수를 입력하세요 : "))
    add += a

avg = add/7
print(avg)