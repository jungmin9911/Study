a=3420
print("1000원 :",a//1000)
print("100원 :",a%1000//100)
print("10원 :",a%100//10)
print("필요한 동전의 개수 :",a%1000//100 + a%100//10)