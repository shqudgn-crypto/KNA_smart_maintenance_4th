# 문자열 연산과 검색
# - 문자열 연결(+), 반복(*)

# ien() - 글자 수
# 형식: ien(문자열)
print(len('PTTHON'))   # 6
print(len('AI 분석'))  # 5 (공백도 글자 수에 포함)
print(len(''))         # 0 (빈 문자열)

# in / not in - 포함 / 불포함 여부 (결과값 bool)
# 형식 : '찾을 것' in 문자열
print('고장' in '설비 고장 발생') # True
print('정상' not in '고장 발생')  # True

# count 
# 형식 : 문자열.count('x') -> 개수
print('banana' . count('a')) # banana라는 단어에서 a개수가 3개 존재한다

# find
# 형식 : 문자열.find('x') -> 처음 나오는 위치
print('banana' . find('a'))  # 1
print('banana' . find('t'))  # -1 (못 찾을 경우)

print("=" * 3,"실습 1","=" * 3) # 길이 재기
numder = '01033255809'
print(len(numder))

print("=" * 3,"실습 2","=" * 3) # 포함 확인하기
print('고장' in '설비 고장 발생')
print('고장' not in '설비 고장 발생')

print("=" * 3,"실습 3","=" * 3) # 개수 세기
print('03_03_str_finc' . count("3"))

print("=" * 3,"실습 4","=" * 3) # 위치 찾기
print('03_03_str_finc' . find("_"))
print('03_03_str_finc' . find("z"))

# index
# 주의) 위치를 반환하지만 없으면 오류
email = 'shqudgn@naver.com'
at = email.index('@')
print(at)
print(email[:at]) 

#startswith / endwith
# 형식 : 문자열.startswith('x') -> bool
print('EQP-001'.startswith('EQP'))  #True
print('cmapss.csv'.endswith('csv')) #True

print("=" * 3,"실습 5","=" * 3) # 시작과 끝 확인하기
name = 'sensor_log.csv'
print('sensor_log.csv'.startswith('sensor'))
print('sensor_log.csv'.endswith('csv'))      

print("=" * 3,"실습 6","=" * 3) # 대소문자 비교하기
label = "WARNING"
print("WARNING" == "WARNING")
print("WARNING" == "warntng")