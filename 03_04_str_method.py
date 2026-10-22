# 메서드 - 점(.) 문법
# 형식 : 문자열. 메서드 이름() (--> 꼭 괄호를 붙여야 실행)
word = 'python'
# upper() : 모두 대문자 / ioper() : 모두 소문자
print(word.upper())    # PYTHON
print(word.count('0')) # 1
print(word)            # python (원본 값 그대로)

print('NORMAL'.lower()) # normal
print('python'.capitalize()) # Python
print('hong gil'.title())    # Hong Gil

print("=" * 3,"실습 1","=" * 3) # 대문자로 바꾸기
print("ready".upper())

print("=" * 3,"실습 2","=" * 3) # 소문자로 바꾸기
print("WARNING".lower())

print("=" * 3,"실습 3","=" * 3) # 단어 첫 글자 대문자로 만들기
print('noh byeong hu'.title())

print("=" * 3,"실습 4","=" * 3) # 대소문자 무시하고 비교하기
print('Fault' == 'Fault')
print('FAULT' == 'FAULT')

print('Fault'.lower() == 'Fault')
print('FAULT'.lower() == 'FAULT')

# 확인 메서드 : is ~ 메서드는 참 / 거짓 반환
print('ABC'.isupper(),'abc'.islower())

# 공백 정리 - strip
# 형식 : strip() = 앞뒤 공백 제거
raw = ' 정상 '
print('['+ raw + ']')          # [ 정상 ]
print('[' + raw.strip() + ']') # [정상]

# .lstrip() -> 왼쪽 공백 제거 / .rstrip() -> 오른쪽 공백 제거
# 주의) strip은 '앞뒤' 공백만 제거 , 가운데 공백 제거x
s = "###정상###"
print(s.strip('#'))  # 정상

print("=" * 3,"실습 5","=" * 3) # 대문자인지 소문자인지 검사하기
print('ABC'.isupper(),"/",'abc'.islower(),"/",'Abc'.isupper())

print("=" * 3,"실습 6","=" * 3) # 파일명 규칙 한번에 점검하기
a = 'Sensor_LOG.CSV'
print(a.lower())

b = 'sensor_log.csv'
print(b.startswith('sensor'))
print(b.endswith('.csv'))

print("=" * 3,"실습 7","=" * 3) # 앞뒤 공백 제거하기
print(' 가동중 ')
print('  가동중  '.strip())

print("=" * 3,"실습 8","=" * 3) # 한쪽 공백만 제거하기
print('  대기  ')
print('  대기  '.lstrip(), '/' ,'  대기  '.rstrip())

print("=" * 3,"실습 9","=" * 3) # 특정 문자 제거하기
print("****경고****".strip("*"))

# 체이닝 - 메서드를 이러 붙이기
# 형식 : 문자열.strip().lower() -> 왼쪽부터 차례로 적용
clean = '  NORMAL  '.strip().lower()
print(clean.strip().lower())

print("=" * 3,"실습 10","=" * 3) # 메서드 이어붙이기
print(' WARNING '.strip().lower())

print("=" * 3,"실습 11","=" * 3) # 결과를 변수에 다시 저장하기
clean ='  경고  '.strip()
print(clean)