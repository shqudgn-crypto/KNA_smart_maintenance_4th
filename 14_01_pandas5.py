import pandas as pd

F = 'data/14_hydraulic.csv'
F_QC = 'data/14_hydraulic_qc.csv'

# 빈도와 그룸 집계
# - 값별로 세기와 그룹별 집계하기

df = pd.read_csv(F)
qc = pd.read_csv(F_QC)
print(df.shape, qc.shape)       # (120, 8) (200, 11)


# 1. 빈도
# - value_counts
# - pd.cut

# print(df['냉각기상태'].value_counts())
# # 냉각기상태
# # 고장    40
# # 저하    40
# # 정상    40
# # Name: count, dtype: int64

# print(df['밸브상태'].value_counts())
# # 밸브상태
# # 정상    61
# # 지연    20
# # 경미    20
# # 심각    19
# # Name: count, dtype: int64

# # 개수 -> 비율 : normalize
# counts = df["result"].value_counts()
# ratios = df["result"].value_counts(normalize=True)
# print(counts)
# print(ratios.round(3))
# print((ratios * 100).round(1))

num = 1
print("=" *3,f"실습 {num}","=" *3)
# print(df.shape)
# valve_counts = df["밸브상태"].value_counts()
# load_counts = df["운전부하"].value_counts()
# print(valve_counts)
# print(df["밸브상태"].value_counts(normalize=True).round(3))
# print(load_counts)
# print(df["운전부하"].value_counts(normalize=True).round(3))

# for counts in [valve_counts, load_counts]:
#     print("가장 많은 값: ", counts[counts == counts.max()])
#     print("가장 적은 값: ", counts[counts == counts.min()])



# pd.cut
band = pd.cut(df["온도"], bins=[0, 40, 50, 200], labels=["낮음", "보통", "높음"], right=True)
print(band.value_counts(sort=False))
# 온도
# 낮음    41
# 보통    40
# 높음    39
# Name: count, dtype: int64


num = 2
print("=" *3,f"실습 {num}","=" *3)
# counts = qc["검사결과"].value_counts()
# ratios = qc["검사결과"].value_counts(normalize=True)
# print(counts, ratios.round(3))
# print("불합격 비율:", round(ratios.loc["불합격"] * 100, 1), "%")    # 불합격 비율: 6.0 %


num = 3
print("=" *3,f"실습 {num}","=" *3)
# print(df["진동"].min(), df["진동"].max())
# band_v = pd.cut(
#      df["진동"], bins=[0, 0.6, 0.7, 10],
#      labels=["약함", "보통", "강함"], right=True
#  )

# counts = band_v.value_counts()
# print(counts)
# print("검산:", counts.sum(), "구간 미지정:", band_v.isna().sum())
# print("최대 구간:", counts[counts == counts.max()])
# print("최소 구간:", counts[counts == counts.min()])



# 그룹 집계
# - 분할 -> 적용 -> 결합 구조
# - groupby

# means = df.groupby("냉각기상태")["온도"].mean()
# print(means.round(2))
# 고장    54.67
# 저하    45.46
# 정상    35.89

# print(df.groupby("냉각기상태")["온도"].max())
# 고장    57.8
# 저하    51.2
# 정상    36.4

# 여러 키 그룹 코드
# keys = ["냉각기상태", "운전부하"]
# print(df.groupby(keys)["온도"].mean().round(2))
# # 냉각기상태  운전부하
# # 고장     고부하     55.51
# #        저부하     54.05
# # 저하     고부하     44.07
# #        저부하     45.58
# # 정상     고부하     35.89

# # crosstab - 두 기준 결과를 가로세로 표로
# print(pd.crosstab(df["냉각기상태"], df["운전부하"]))
# # 운전부하   고부하  저부하
# # 냉각기상태          
# # 고장      17   23
# # 저하       3   37
# # 정상      40    0

num = 4
print("=" *3,f"실습 {num}","=" *3)
counts = df.groupby("냉각기상태").size()
means = df.groupby("냉각기상태")["온도"].mean()
maxima = df.groupby("냉각기상태")["온도"].max()
print(counts)
print(means.round(2))
# # 냉각기상태
# # 고장    54.67
# # 저하    45.46
# # 정상    35.89
# # Name: 온도, dtype: float64
print(maxima)
# # 냉각기상태
# # 고장    57.8
# # 저하    51.2
# # 정상    36.4
print("평균 차이: ", round(means.max()-means.min(), 2))

num = 5
print("=" *3,f"실습 {num}","=" *3)
total = df["밸브상태"].value_counts()
print(total)
# 밸브상태
# 정상    61
# 지연    20
# 경미    20
# 심각    19
# Name: count, dtype: int64

broken = df[df["result"] == "고장"]
broken_counts = broken.groupby("밸브상태").size()
print(broken_counts)
# 밸브상태
# 경미    14
# 심각    14
# 정상    12
# 지연    13
# dtype: int64

# 고장 라벨이 0건인 상태도 빠지지 않도록 이름표를 맞춘다
broken_counts = broken_counts.reindex(total.index, fill_value = 0)
ratios = broken_counts / total
print(ratios.sort_values(ascending=False).round(3))
# 밸브상태
# 심각    0.737
# 경미    0.700
# 지연    0.650
# 정상    0.197
# dtype: float64