# 연산자
# - 산술 , 비교 , 논리 연산자

# 산술 연산자
# 형식 : + , - , * , / , // (몫) , % (나머지) , ** (거듭제곱)

# 우선 순위
# - 곱셈 , 나눗셈 등이 우선 ,  괄호를 이용하여 변경 가능

# 복합 할당
# 형식 : score += 10 <-> score = score + 10
score = 100
score += 10
print(score)
# -= , *= , /=

# 문자열 연산
# + , *
print("안녕"+"하세요") #안녕하세요
print("=" * 3) # === -> 반복
# 주의) 자료형이 같은 것 끼리 연산 할 수 있다

print("=" *3,"실습 1","=" *3) # 사칙연산 계산기
a = 4
b = 2
print(a + b , a - b , a * b , a / b)
print(a // b , a % b , a ** b )

print("=" * 3,"실습 2","=" * 3) # 평균과 도형 계산
a = 5 # 가로
b = 5 # 세로
c = 5 # 높이

print("평균", (a + b + c) / 3 ) # 평균
print("넓이", a ** 2 )          # 넓이
print("부피", a * b * c)        # 부피
print("평균", (a + b + c) / 3  , "넓이", a ** 2 , "부피", a * b * c )

# 비교 연산자
# 형식 : == (같다)  != (다르다) <> <= >=
print(5 == 5)        # True
print("A" == "a")    # False

# 논리 연산자
# - and : 모두가 참이어야 함, or : 하나만 참이어도 참. not : 반대
print(True and False)  #False
print(True or False)   #True
print(not True)        #False

print("=" * 3,"실습 3","=" * 3) # 비교 연산 출력
print(2 == 2) #True
print(1 != 2) #True
print(1 > 2)  #Fslse
print(3 < 4)  #True
print(8 >= 3) #True
print(5 <= 4) #Fslse

print("=" * 3,"실습 4","=" *3) # 정상벙위와 다중센서 판정
temp = 85
temp_ok = 60 <= temp and temp <= 90
print(temp_ok)                # True
pressure = 5
pres_ok = 3 <= pressure and pressure <= 7
print(pres_ok)                # True
print(temp_ok and pres_ok)    # True  (둘 다 정상)

print("=" * 3,"실습 5","=" *3) # 복합 할당으로 재고 추적
stock = 100
stock += 50
print(stock)   # 150  (입고)
stock -= 30
print(stock)   # 120  (출고)
stock += 5
print(stock)   # 125  (반품)

print("=" * 3,"실습 6","=" *3) # 설비 지표 계산
total = 500
defect = 23
print(defect / total * 100, "%")   # 4.6   (불량률 %)
run_h = 21
all_h = 24
print(run_h / all_h * 100, "%")    # 87.5  (가동률 %)


print("=" * 3,"실습 7","=" *3) # 시간 변환과 상자 포장
minutes = 500
print(minutes // 60)   # 8   (시간)
print(minutes % 60)    # 20  (분)
print(minutes // 60, "시간", minutes % 60, "분")