print("=" *3,"실습 1","=" *3) # 조건에 맞는 값만 출력하기
temps = 25, 32 , 28, 35, 19
for t in temps:
    if t >= 30:
        print("고온: ", t)

print("=" *3,"실습 2","=" *3) # 두 조건을 모두 만족하는 값 고르기
hours = 4, 8, 6, 11, 5, 10, 3
for t in hours:
    if 5 <= t <= 10:
        print("조건 만족: ",t)

# 최대, 최소
temps = [25, 32, 28, 36, 27, 31]
biggest = temps[0]
for t in temps:
    if t > biggest:
        biggest = t     # 더 큰값일 때 갱신
print(biggest)

# 빈 리스트 채우기
temps = [25, 32, 28, 36, 27, 31]
doudled = []
for t in temps:
    doudled.append(t *2)  # [50, 64, 56, 72, 54, 62] 두배로 
print(doudled)

print("=" *3,"실습 3","=" *3) # 조건에 맞는 값만 골라 평균 구하기
temps = [25, 32, 28, 35, 27]
total = 0
count = 0
matched_list = []
for t in temps:
    if t > 30:
        total = total + t  # 합계 누적
        count = count + 1  # 개수 1 증가
        matched_list.append(t)
average = total / count
print("조건에 맞는 값들:", matched_list)
print("합계:", total, "/ 개수:", count)
print("고온 평균:", average)

print("=" *3,"실습 4","=" *3) # 조건에 맞는 값으로 새 리스트 만들기
온도 = [20,17,37,48,32,68,24,64,59]
high = []
for t in 온도:
    if t > 30:
        high.append(t)
print("원본 온도: ",온도)
print("새 리스트(고온): ",high)
print("개수: ",len(high))

print("=" *3,"실습 5","=" *3) # 값을 가공해 새 리스트 만들기
온도 = [25, 32, 28, 35, 27]
fahrenheit = []
for t in 온도:
    fahrenheit.append(t * 1.8 + 32)
print("원본 섭씨:", temps)
print("변환된 화씨:", fahrenheit)

# 중첩 리스트 - 리스트 안에 리스트
# - 표(행,열)처럼 한 줄에 여러 값이 묶인 데이터. 바깥 반복은 '행', 안쪽 인덱스로 '열'
rows = [["펌프", 25], ["모터", 32], ["압축기", 28]]
for row in rows:
  print(row[0], "온도", row[1])

print("=" *3,"실습 6","=" *3) # 센서 데이터 종합 분석하기
온도 =[24,86,43,89,12,52,32]
total = 0
high = []
for t in 온도:
    total = total + t      # 전체 합계 누적
    if t > 30:
        high.append(t)     # 30 초과 값만 새 리스트에 담기
전체평균 = total / len(온도)
고온평균 = sum(high) / len(high)

print("전체 평균:", 전체평균)
print("고온 개수:", len(high))
print("고온 평균:", 고온평균)
    