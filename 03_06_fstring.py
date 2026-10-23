# f - string - 문자열 안에 변수 바로 끼우기
# 형식 : f"~~~ {변수}~~'

name ="홍길동"
age = 25
print(f'{name}님은 {age}살 입니다')  # 홍길동님은 25살 입니다
# 숫자도 str 변환 없이 바로 들어감
print(f'온도: {25.5}')
# 중괄호 안에 계산식 가능
hours = 3
print(f'{hours * 60}분')
# 소수점 자리수 조정
# 형식 : {값(변수):2f} -> 소수점 둘째 자리까지 (자동 반올림)
value = 25.8567
print(f'측정값: {value:.2f}')  # 측정값: 25.86 (자동 반올림)
print(f'측정값: {value:.1f}')  # 측정값: 25.9 (자동 반올림)

print('=' * 3,'실습 1','=' * 3) # f-string 으로 변수 끼워 출력하기
name ="PUMP_A"
temp = 25.3
print(f'설비:{name} / 온도:{temp}°C ')

print('=' * 3,'실습 2','=' * 3) # f-string 안에서 계산하기
김학생 = 61
박학생 = 93
이학생 = 78
print(f'{(김학생 + 박학생 + 이학생) /3}')
평균 = 77.33333333333333
print(f'평균: {평균:.2f}점')  # 평균: 77.33점

print('=' * 3,'실습 3','=' * 3) # 소수점 자릿수 지정하기
측정값 = 63.7459
print(f'측정값: {측정값:.1f}','/',f'{측정값:.3f}') 

print('=' * 3,'실습 4','=' * 3) #  센서 로그 한 줄 정리 리포트 만들기
raw = " 5 , sensor_2 , WARNING , 0.78912 "
parts = raw.strip().split(',')
sid = parts[1].strip()
status = parts[2].strip().lower()
value = float(parts[3].strip())

print(f"[센서 {sid}] 상태 {status}, 측정값 {value:.2f}")
