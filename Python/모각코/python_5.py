from numpy import average
#1
print("#1번")
a=int(input("첫 번째 과목의 점수를 입력하세요 :"))
b=int(input("두 번째 과목의 점수를 입력하세요 :"))
c=int(input("세 번째 과목의 점수를 입력하세요 :"))

average = (a+b+c)/3

if average>=50:
    print("평균 점수는",average,"점으로 합격입니다.")
else:
    print("평균 점수는",average,"점으로 불합격입니다.")

#2
print("#2번")
A=input("단어를 입력해주세요 :")
B=input("문장을 입력해주세요 :")

if A in B:
    print("단어가 있습니다.")
else:
    print("단어가 없습니다.")