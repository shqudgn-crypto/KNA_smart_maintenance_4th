# 변수와 할당 - 값에 이름 붙이기
# 형식 : 변수이름 = 값 <- 오른쪽 값을 왼쪽 이름에 "저장" 하라는 명령
temp = 25
name = "센서A"
count = 3

print(temp)
print("temp")
X = 10
X = X + 5
print(X) #15

# 변수 이름 규칙
# 형식 : 영문자,숫자,밑줄 사용 가능 / 숫자로 시작 불가 / 공백 불가
sensor_count =3 # snake_case
temp2 = 10 # 숫자 사용 가능 (숫자로 시작x)
# 2temp = 2 #syntaxError

# 대소문자 구분, 재할당
temp = 25
Temp = 100
print(temp, Temp) # 25  100
# 재할당 : 마지막에 저장한 값만 남음
score = 10
score = 20
score = 30
print(score) # 30

print("=== 실습 1 ===")
temp = 25
print(temp)
name = "센서A"
print(name)

print("=== 실습 2 ===")
temperature = 30
print(temperature)

print("=== 실습 3 ===")
my_number = 99
print(my_number)
mood = "good_행복"
print(mood)

print("=== 실습 4 ===")
age = 32
labe = "나이"
print(labe)
print(age)

print("=== 실습 5 ===") # 변수 값 바꿔가며 추적하기
x = 10
print(x)
x = x + 5
print(x)
x = x * 2
print(x)

print("=== 실습 6 ===") # 두 변수 값 옮기고 바꾸기
a = 100
b = a
a = 999
print(a)
print(b) # 그 순간의 값을 복사할뿐 이후 a가 바뀌어도 b는 그대로

print("=== 실습 7 ===") # 일부러 오류 내고 고치기
test_temp = 88
print(test_temp)

print("=== 실습 8 ===") # 주석으로 변수 설명 달기
# temp = 100
count = 3 # 센서 개수
print(temp)

print("=== 실습 9 ===") # 값 예측 미니 퀴즈
x = 5
x = 10
x = x + 1
# 정답 예측 11
print(x)

print("=== 실습 10 ===") # 정보 카드 만들기
name1 = "공장1"
name2 = "설비A"
temp1 = 37.2 # 온도
temp2 = 3 # 점검 횟수
print(name1,name2,"온도 :",temp1,"점검 횟수 :",temp2)

print("=== 실습 11 ===") # 변수 이름 다듬기
device_temp = 24
sendor_count = 7
print(device_temp)
print(sendor_count)

print("=== 실습 12 ===") # 변수 한줄 만들기 도전
x,y,z = 2,4,5
print(y)
width,height = 13,28
print(width,height)
