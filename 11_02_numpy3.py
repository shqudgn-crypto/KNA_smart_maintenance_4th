import numpy as np

F = 'data/11_hydraulic_cooler.csv'

def col(c):
    return np.genfromtxt(F, delimiter=",", skip_header=1, usecols=c)

# isnan - 결측값 위치 찾기
# - 결측값 : 값이 빈 칸 -> 0이 아니라 값을 모름

# x = np.array([2.0, np.nan, 4.0])
# print(np.isnan(x))          # [False  True False]
# print(np.isnan(x).sum())    # 1

# nanmean, nanstd - 결측값을 무시한 통계
# temp = np.array([70.1, np.nan, 71.2, 70.8])
# print(np.mean(temp))
# print(round(np.nanmean(temp),2))

# nanmean, nanmax, nanmin

# num = 1
# print("=" *3,f"실습 {num}","=" *3)
# vib = col(2)

# print(np.isnan(vib).sum())
# print(round(np.isnan(vib).mean(), 2))
# print(round(np.nanmean(vib), 3))
# print(np.mean(vib))

# 백분위수, 사분위수 - percentile, quantile
# - 데이터를 크기순으로 줄 세웠을 때 특정 위치의 값
# - 25, 50, 75 백분위수 -> 1사분위, 중앙값, 3사분위
# - 평균과 달리 극단적인 이상값에 휘둘리지 않음

# vib_s = np.array([2.0, 2.2, 2.5, 2.8, 3.0, 6.5])
# print(np.round(float(np.percentile(vib_s, 25)), 2))   # 2.28
# print(np.round(float(np.percentile(vib_s, 75)), 2))   # 2.95

# 여러 자리 한번에
# print(np.round(np.percentile(vib_s, [25, 50, 75]), 2))    # [2.28 2.65 2.95]

# # quantile : 25 -> 0.25
# print(np.round(float(np.quantile(vib_s, 0.25)), 2))     # 2.28

# 사분위 기반 이상치 범위 - IQR

# q1, q3 = np.percentile(vib_s, [25, 75])
# iqr = q3 - q1
# upper = q3 + 1.5 * iqr
# print(vib_s[vib_s > upper])


# 평균/표준편차로 정규화 - z-score
# - 부호의 의미: 양수는 평균보다 위, 음수는 아래
# - 방향 무시하고 크기만 보려면 절댓값 필요

# z = (vib_s - np.mean(vib_s)) / np.std(vib_s)
# print(vib_s[np.abs(z) > 2])


# num = 2
# print("=" *3,f"실습 {num}","=" *3)
# temp = col(1)
# q1, q3 = np.percentile(temp, [25, 75])
# upper = q3 + 1.5 * (q3 - q1)    # 상한값
# print(temp[temp > upper])   # 상한 초과
# print(int((temp > upper).sum()))

# num = 3
# print("=" *3,f"실습 {num}","=" *3)
# cyc = col(0)
# temp = col(1)

# 표준화
# z = (temp - np.nanmean(temp)) / np.nanstd(temp)
# abnormal = np.abs(z) > 2
# print(cyc[abnormal].astype(int))      # [47 48 49 50]
# print(round(np.abs(z).max(), 2))    # 3.39

# num = 4
# print("=" *3,f"실습 {num}","=" *3)
# cyc = col(0)
# temp = col(1)

# high = np.nanmean(temp) + 3 * np.nanstd(temp)
# print(round(high, 2))
# print(cyc[temp > high].astype(int))


# 센서 간 상관관계 - corrcoef
# - 세기는 절댓값이 정함. +0.99와 -0.99는 세기가 똑같고 방향만 반대
# - 양수: 한쪽이 오르면 다른 쪽도 오름 / 음수는 반대
# - 0에 가까움 -> 관계가 없는 상태

# temp = np.array([70, 72, 74, 76, 78])
# vib = np.array([2.0, 2.2, 2.5, 2.7, 3.0])
# print(round(float(np.corrcoef(temp, vib)[0, 1]), 3))        # 0.998

#
# print(np.round(np.corrcoef(temp, vib), 3))
# [[1.    0.998]
# [0.998 1.   ]]
# 온도-온도, 온도-진동, 진동-온도, 진동-진동 네 조합을 모두 계산해 줌


# 2D 배역 axis별 통계 활용
# 행은 센서, 열은 시점인 행렬 axis로 방향을 정해 통계
# axis = 1 - 각 행을 옆으로 > 센서별 통계
# axis = 0 - 각 열을 아래로 > 시점별 통계

# data = np.array([[70., 72., 74.],[2.0, 2.2, 2.5]])
# print(np.round(np.mean(data, axis = 1), 2))     # [72.    2.23]
# print(np.round(np.mean(data, axis = 0), 2))     # [36.   37.1  38.25]

# num = 5
# print("=" *3,f"실습 {num}","=" *3)
# temp = col(1)
# ce = col(3)

# corr = np.corrcoef(temp, ce)
# print(round(corr[0, 1], 2))     # -0.99

# num = 6
# print("=" *3,f"실습 {num}","=" *3)
# M = np.stack([col(1), col(2), col(3), col(4)])
# print(M.shape)
# print(np.round(np.nanmean(M, axis = 1), 1)) # [37.7  0.6 44.7 57.7]
# print(np.round(np.nanstd(M, axis = 1), 1))  # [6.  0.1 7.6 1.6]


# 변화점 탐지
# - 누적 합으로 찾는 원리
# - 각 값에서 전체 평균을 배면 평균보다 작은 값은 음수, 큰 값은 양수
# - 해당 값들을 앞에서부터 누적하면 평균보다 낮은 구간에서는 계속 내려가고,
#   평균보다 높은 구간에서는 계속 올라감
# - 그래서 누적 곡선이 가장 낮아지는 자리가 내려가기를 멈추고 올라가기 시작한 자리

# v = np.array([2.0, 2.1, 2.0, 5.0, 5.2, 5.1])
# cs = np.cumsum(v - np.mean(v))
# print(np.argmin(cs))        # 2

num = 7
print("=" *3,f"실습 {num}","=" *3)
cyc = col(0)
temp = col(1)

cs = np.cumsum(temp - np.nanmean(temp))
k = np.argmin(cs)
print(int(cyc[k]), round(cs[k], 1))     # 45 -81.7

num = 8
print("=" *3,f"실습 {num}","=" *3)
cyc = col(0)  # 사이클 번호
t = col(1)    # 온도
ce = col(3)   # 냉각효율
st = col(5)   # 상태 라벨

# z-score 절댓값 구하기
def z(a):
  return np.abs((a - np.nanmean(a)) / np.nanstd(a))

score = z(t) + z(ce)

i = np.nanargmax(score)

print(int(cyc[i]), round(score[i], 2))

# 상위 세 시점
top = np.argsort(score)[::-1][:3]
print(cyc[top].astype(int))