# 자료형

count = 3  # int 정수
temp = 25.5  # float 실수
name = "센서A"  # str 문자열

ok = True  #bool 불린형 - 참/거짓
no = False 

# type() -> 자료형을 알려준다
print(type(25))       #<class 'int'>
print(type("센서A"))   #<class 'str'>
print(type(ok))        #<class 'bool'>

# 자료형 마다 다른 동작
print(3 + 5)      # 8 (숫자 더하기 = 계산)
print( "3" + "5") # 25(글자 더하기 = 이어 붙이기)

print("=== 실습 1 ===") # 여러 자료형 변수 만들기
count = 1
temp = 2.5
name = "센서A"
ok = True
no = False

print(count)
print(temp)
print(name)
print(ok)

print("=== 실습 2 ===") # type()으로 자료형 확인하기
print(type(1))
print(type(2.5))
print(type("센서A"))
print(type(ok))

print("=== 실습 3 ===") # 자료형 맞히기 퀴즈
print(type(100)) #int 정수
print(type(100.0)) #float 실수
print(type("100")) #str 문자열

print("=== 실습 4 ===") # 문자열 숫자와 숫자 비교하기
print(2 + 3)
print("2" + "3")
print("20" + "30")

print("=== 실습 5 ===") # bool값 만들어 확인하기
print(3 > 2) # True
print(5 == 5) # True
print(4 < 3) # False

print(type(3 >2))

print("=== 실습 6 ===") # 변수의 자료형 변경하기
print(type("센서A"))

print("=== 실습 7 ===") # 직접 자료형 표현하기
print(2.2) # device_temp / float 실수
print(5) # check_count / int 정수
print("온도") # device_name / str 문자열
print(3 < 7) # is_normal / bool 불린형