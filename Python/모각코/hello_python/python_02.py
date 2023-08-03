#3-1. 자료형과 변수

#파이썬의 숫자형
#정수형(int) / 실수형(float)
#type() 함수를 사용해 자료형 직접 확인 가능
print(type(10))    #<class 'int'>
print(type(5.9))   #<class 'float'>

print(2080+1)      #2081
print(0.5+0.5)     #1.0

print("2080 + 1")  #2080 + 1
print("2080" + "1")#20801
print("0.5 + 0.5") #0.5 + 0.5
print("0.5" + "0.5")  #0.50.5
#문자열을 더하기하면 띄어쓰기 없는 출력이 됨

print(type("2080 + 1"))    #<class 'str'>
print(type("2080" + "1"))  #<class 'str'>
print(type("0.5 + 0.5"))   #<class 'str'>
print(type("0.5" + "0.5")) #<class 'str'>

#파이썬의 불 자료형
#불(bool(boolean)) : 참(True) / 거짓(False) **파이썬에서는 True, False 모두 맨 앞 글자가 대문자여야함
print(2 > 3)        #False
print(2 < 9)        #True

print(type(2 > 3))  #<class 'bool'>
print(type(2 < 9))  #<class 'bool'>

#파이썬의 변수
#변수 : 이름을 정하고 ,데이터를 매번 바꿔가며 저장할 수 있는 공간
my_name = "Bob" #my_name이라는 변수에 Bob이라는 문자 저장.
print(my_name)  #Bob 출력

my_name = "Sandy" #my_name이라는 변수에 Sandy라는 문자를 새로 저장
print(my_name)    #Sandy 출력

#숫자형을 저장하는 변수
#파이썬의 변수는 모든 자료형을 저장할 수 있음
my_age = 30       #my_age라는 변수에 30이라는 정수를 저장
your_age = 25     #your_age라는 변수에 25라는 정수를 저장

print(my_age)     #my_age 출력
print(your_age)   #your_age 출력

#문자열을 다루는 방법 - 인덱싱
#문자열 인덱싱을 사용하면 문자열에서 원하는 부분만 골라서 가져올 수 있음
#일반 코드
hi = "파이썬 공부는 즐거워!"
print(hi)          
#출력결과 : 파이썬 공부는 즐거워!
#파(0)이(1)...워(10)!(11)  *0부터 시작

#인덱싱 코드
#대괄호를 사용하여 그 안에 인덱스 번호 삽입 ex.hi[8]
print(hi[2])
print(hi[6])
print(hi[-1])    #썬 는 !

#print(h1[-1]) 음수 인덱싱은 뒤에서부터 읽을 수 있음
#파(-12)이(-11)...워(-2)!(-1)

#슬라이싱
#문자열을 잘라서 가져오는 방법
#hi = "파이썬 공부는 즐거워!"
print(hi[4:7])  # 4번부터 7-1번 문자열까지 출력
print(hi[-4:])  # -4부터 문자열의 마지막까지 슬라이싱
print(hi[:4])   # 문자열의 첫 글자부터 4-1번 문자열까지 슬라이싱
print(hi[4:-1]) # 4번부터 -2번 문자열까지 출력

#3-2. QUIZ
#1번
print(type(10))
print(type(0.5))
print(type(2>0))
print(type("안녕하세요"))

#2번
hi="제 닉네임은 ㅇㅈㅁㅈㅁ입니다."
print(hi[-9:-4])
