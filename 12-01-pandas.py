import numpy as np
import pandas as pd

F = 'data/12_metro_compressor.csv'
FS = 'data/12_metro_compressor_semicolon.csv'

# Pandas
# - 표 형태의 데이터를 잘 다루기 위해
# - series : 하나의 열들
# - Dataframe : series가 모여서 합쳐진 것, 표 구조 (df)

# 앞 단원 방식 -> 숫자 열만 골라야 함
# pandas 방식 -> 글자 열까지 그대로, 열은 이름으로

df = pd.read_csv(F)
print("데이터 크기: ", df.shape)    # 데이터 크기:  (200, 7)
#print(df.head)
#print("열 이름: ",df.columns.tolist())
    # ['측정시각', '압축압력', '배출압력', '저장압력', '오일온도', '모터전류', '가동상태']

#print(df.dtypes)
# 측정시각        str
# 압축압력    float64
# 배출압력    float64
# 저장압력    float64
# 오일온도    float64
# 모터전류    float64
# 가동상태        str
# dtype: object

state =df["가동상태"].values
print("가동상태 종류 개수: ", np.unique(state, return_counts= True))
# 가동상태 종류 개수:  (array(['가동', '정지'], dtype=object), array([ 96, 104]))

cur = df["모터전류"].values
print("모터전류 평균 %.2f / 가운데 값 %.2f" % (np.mean(cur), np.median(cur)))
# 모터전류 평균 2.06 / 가운데 값 0.04

s = df["오일온도"]
print(s.head(3))
# 0    51.3
# 1    56.8
# 2    55.7
# Name: 오일온도, dtype: float64

# Pandas - 열 이름
new = pd.read_csv(F, usecols=["오일온도", "모터전류"])
print(new.shape)                            # (200, 2)
# 행 수를 제한하는 설정
print(pd.read_csv(F, nrows=10).shape)       # (10, 7)
# read_csv 옵션
# - usecols, nrows, encoding, sep(구분자)

num = 2
print("=" *3,f"실습 {num}","=" *3)
sel = pd.read_csv(F, usecols=["측정시각", "오일온도", "모터전류"])
print(sel.shape)    # (200, 3)

part = pd.read_csv(F, nrows=20)
print(part.shape)   # (20, 7)


num = 3
print("=" *3,f"실습 {num}","=" *3)
a = pd.read_csv(FS)
print(a.shape)      # (200, 1)

# 값을 나누는 기호를 알려줘서 나눠줘야함
b = pd.read_csv(FS, sep=";", encoding="utf-8")
print(b.shape)      # (200, 7)
print(b.columns.tolist())

num = 4
print("=" *3,f"실습 {num}","=" *3)
df_selected = pd.read_csv(
    FS, 
    sep=";", 
    encoding="utf-8", 
    usecols=["측정시각", "오일온도", "모터전류"], 
    nrows=50
)

print(df_selected.shape)
print(df_selected.head())