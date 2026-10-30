# 모듈 / 패키지 /라이브러리
# - 모듈: 기능을 모아둔 .py 파일 하나
# - 패키지: 모듈을 모아둔 폴더
# - 라이브러리: 위의 사항들을 통칭

# import 방식
# 형식: import 모듈 / from 모듈 improt 기능 / improt
import math                 # math 라는 모듈을 통째로 불러옴
print(math.sqrt(16))        # 4.0
from math import sqrt, ceil # 일부만 불러옴 -> 모듈명 없이 바로 사용
print(sqrt(16)),(ceil(4.1))
import math as m
print(m.sqrt(16))

unm = 1
print("=" *3,f"실습 {unm}","=" *3) # import 세방식으로모듈가져오기
import math                 
print(math.sqrt(16))        
from math import sqrt, ceil 
print(sqrt(16)),(ceil(4.1))
import math as m
print(m.sqrt(16))

# 표준 라이브러리 - math / random / datetime
# - 파이썬 설치 시 함께 깔리는 검증된 모듈들
import random
import datetime

print(random.randint(1,100))    # 랜덤값 출력 54
print(datetime.datetime.now())  # 2026-10-30 10:35:54.901562

unm = 2
print("=" *3,f"실습 {unm}","=" *3) # 표준 라이브러리로 센서값 만들기
import random
import math 
sensor_value = random.randint(1, 100)   # random 모듈로 랜덤으로 만들어 변수에 저장
print(f"무작위 센서값: {sensor_value}")
result = math.sqrt(sensor_value)        # math 모듈로 그 무작위 값을 가공(제곱근 계산)
print(f"센서값의 제곱근: {result}")

# 경로와 os 모듈
# - 파일을 다루려면 어디에 있는지 경로를 알아야한다
# 1) 절대경로
#   - 최상위부터 전체 주소
# 2) 상대경로
#   - 지금 실행중인 위치를 기준으로 한 주소

import os
print("현재 실행 위치(정대 경로):", os.getcwd())

# 폴더 유무 확인
print(os.path.exists("data"))   # True

# 폴더 목록 확인
files = os.listdir("data")
print(files)                    # ['08_press.csv']

# 폴더명 + 파일명 -> 경로
path = os.path.join("data","08_press.csv")

if os.path.exists(path):
    print("파일 경로 :", path)



import os
import datetime


unm = 3
print("=" *3,f"실습 {unm}","=" *3) # os 폴더로 목록 살펴보기
print(os.getcwd())      # 현재 작업 폴더
files = os.listdir("data")
for file in files:
    print(file)

print("=========")
for file in files:
    if file.endswith(".csv"):
        print(file)

unm = 4
print("=" *3,f"실습 {unm}","=" *3) # os 로 파일 존재 확인하기
path = os.path.join("data", "08_press.csv")
print(os.path.exists(path))   # True

if os.path.exists(path):
    print("파일 있음")
else:
    print("파일 없음")

unm =5
print("=" *3,f"실습 {unm}","=" *3) # datetime 으로 점검 기록 남기rl
files = os.listdir("data")
now = datetime.datetime.now()
print(f'파일 {len(files)}개, 점검 시작 {now}')

unm =6
print("=" *3,f"실습 {unm}","=" *3) # 폴더에서 csv 파일만 골라내기
files = os.listdir("data")
csvs = []
for n in files:
    if n.endswith(".csv"):
        csvs.append(n)

print("[CSV]")
for n in csvs:
    path = os.path.join("data", n)
    print(" -", path)