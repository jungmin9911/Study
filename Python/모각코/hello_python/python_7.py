height = int(input("키를 입력하세요 : "))
weigh = int(input("몸무게를 입력하세요 : "))

BMI = weigh/((height/100)*(height/100))

if BMI>=25:
    print("비만입니다.")
elif 25>BMI>=23:
    print("과체중입니다.")
elif 23>BMI>=18.5:
    print("정상체중입니다.")
else:
    print("저체중입니다.")
