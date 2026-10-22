# 인덱싱 - 위치 번호로 글자 하나 꺼내기
# 형식: 문자열[번호]  (첫 글자 = 0)

word = "PYTHON"
print(word[0], word[2], word[5]) # P T N
# 음수 인덱스 ; 뒤에서부터 -1, -2 ~
print(word[-1], word[-3]) # N H

#에러 내보기
#print(word[6]) # IndexError: string index out of range (범위가 밧어났다 (6번 인덱스 번호가 없음))

print("=" * 3, "실습 1" ,"=" * 3) # 양수 인덱스로 글자 꺼내기
word = "SIGNAL"
print(word[0],"/",word[2],"/",word[5])

print("=" * 3, "실습 2" ,"=" * 3) # 음수 인덱스로 글자 꺼내기
word = "SIGNAL"
print(word[-1],"/",word[-2])

# 슬라이싱 - # 구간으로 잘라내기 
# 형식: 문자열[시작:끝]  (시작 포함, 끝 제외)
word = "PYTHON"
print(word[0:3]) # P Y T
# 생략 가능
# - 시작 생략 = 처음부터 (0번부터)
# - 끝 생략 = 끝까지
# - 둘다 생략 = 전체
print(word[:3]) # PYT
print(word[3:]) # HON
print(word[:])  # PYTHON
# 음수
print(word[-3:]) # HON
print(word[:-1]) # PYTHO

print("=" * 3, "실습 3" ,"=" * 3) # 구간 자르기
word = "SIGNAL"
print(word[0:3],"/",word[2:5])

print("=" * 3, "실습 4" ,"=" * 3) # 앞부분 가져오기
word = "temp_sensor"
print(word[0:4])

print("=" * 3, "실습 5" ,"=" * 3) # 뒤쪽 전체 가져오기
word = "temp_sensor"
print(word[5:])

print("=" * 3, "실습 6" ,"=" * 3) # 뒤 n글자 가져오기
word = "sensor_01"
print(word[-2:])

# step 간격주기
# 형식 : 문자열 [시작:끝:간격]
word = "PYTHON"
print(word[::2])  # PTO
print(word[1::3]) # Y O

print("=" * 3, "실습 7" ,"=" * 3) # 건너뛰며 가져오기
word = "SIGNAL"
print(word[::2])

print("=" * 3, "실습 8" ,"=" * 3) # 문자열 뒤집기
print(word[::-1])
