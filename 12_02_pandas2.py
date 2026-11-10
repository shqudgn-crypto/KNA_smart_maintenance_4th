import pandas as pd
import numpy as np

F = 'data/12_metro_compressor.csv'
FD = 'data/12_metro_digital.csv'

df = pd.read_csv(F)

# 데이터 미리보기 및 구조 파악

# 1) 앞 부분 미리보기
# - df.haed() > 위에서 5줄, 숫자 지정 가능
print(df.head())

# 2) 뒷 부분 미리보기
# - df.tail() > 밑에서 5줄, 숫자 지정 가능


num = 1
print("=" *3,f"실습 {num}","=" *3)
print(df.tail())

print("=== head() 기본 (앞 5줄) ===")
print(df.head())

# ③ 뒷부분을 띄워 마지막 번호(인덱스)가 몇인지 확인하기
print("\n=== tail() 기본 (뒤 5줄) ===")
print(df.tail())

# ④ 괄호 안 숫자를 바꿔 앞 세 줄과 뒤 열 줄 보기
print("\n=== head(3) (앞 3줄) ===")
print(df.head(3))

print("\n=== tail(10) (뒤 10줄) ===")
print(df.tail(10))

# 3) 행/열 크기
# - df.shape
print(df.shape)

# 4) 열 이름 목록
# - df.colums   > 인덱스 형태로 출력
# - df.coums.tolist()   > 목록으로 보기 좋게
print(df.columns.tolist())
# ㄴ 여기서 나오는 값으로 특정 열의 데이터 값 추출

# 5) 행 번호표
# - df.index
print(df.index)     # RangeIndex(start=0, stop=200, step=1)
# ㄴ 0부터 시작< 199까지 1씩

# 6) 열별 자료형
# - df.dtypes
# print(df.dtypes)
# print("----------------------------")
# print(pd.read_csv(FD).dtypes)
# # 측정시각       str
# # 압축기      int64
# # 타워       int64
# # 저압스위치    int64
# # dtype: object
# df2 = pd.read_csv(FD, dtype={"압축기": str})

# num = 2
# print("=" *3,f"실습 {num}","=" *3)
# df = pd.read_csv(FD)
# print(df.shape)
# print(df.columns.tolist)
# print(df.dtypes)
# print(df.head())

# 7) 전체 구조
# - df.info
#print(df.info())

# <class 'pandas.DataFrame'>            
# RangeIndex: 120 entries, 0 to 119             > 200행
# Data columns (total 4 columns):               > 7열
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   측정시각    120 non-null    str  
#  1   압축기     120 non-null    int64
#  2   타워      120 non-null    int64
#  3   저압스위치   120 non-null    int64
# dtypes: int64(3), str(1)
# memory usage: 3.9 KB
# None


# 기초 통계 요약
# - 숫자 열들의 평균/최대/최소 등을 한번에 자동 계산. 글자 열은 자동으로 빠짐

print(df.describe().round(2))

# 특정 조건에서의 통계 필요 시
state = df["가동상태"].values
cur = df["모터전류"].values
print(round(float(np.mean(cur[state == "가동"])), 2))

# num = 3
# print("=" *3,f"실습 {num}","=" *3)
# df = pd.read_csv(F)
# print(df.info())

# num = 4
# print("=" *3,f"실습 {num}","=" *3)
# df = pd.read_csv(F)
# print(df.describe().round(2))

# # 두 열을 배열로 꺼내 상태별로 나눠 확인
# state = df["가동상태"].values
# cur = df["모터전류"].values

# print(round(float(np.mean(cur[state == "가동"])), 2))   # 4.25
# print(round(float(np.mean(cur[state == "정지"])), 2))   # 0.04

num = 6
print("=" *3,f"실습 {num}","=" *3)
FS = 'data/12_metro_small.csv'
df = pd.read_csv(FS)
print(df.head(3))
print('크기:', df.shape)
print(df.info())

stats = df.describe()

miss = int(df["오일온도"].isna().sum())
print('오일온도 결측:', miss, '건')

mean_current = round(float(stats["모터전류"]["mean"]), 2)
median_current = round(float(stats["모터전류"]["50%"]), 2)
print("모터전류 평균/중앙값:", mean_current, median_current)