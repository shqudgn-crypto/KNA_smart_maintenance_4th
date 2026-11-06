import numpy as np

F = 'data/11_hydraulic_cooler.csv'

def col(c):
    return np.genfromtxt(F, delimiter=",", skip_header=1, usecols=c)

# isnan - 결측값 위치 찾기
# - 결측값 : 값이 빈 칸 -> 0이 아니라 값을 모름

x = np.array([2.0, np.nan, 4.0])
print(np.isnan(x))          # [False  True False]
print(np.isnan(x).sum())    # 1

# nanmean, nanstd - 결측값을 무시한 통계
temp = np.array([70.1, np.nan, 71.2, 70.8])
print(np.mean(temp))
print(round(np.nanmean(temp),2))

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

vib_s = np.array([2.0, 2.2, 2.5, 2.8, 3.0, 6.5])
print(np.round(float(np.percentile(vib_s, 25)), 2))   # 2.28
print(np.round(float(np.percentile(vib_s, 75)), 2))   # 2.95

# 여러 자리 한번에
print(np.round(np.percentile(vib_s, [25, 50, 75]), 2))    # [2.28 2.65 2.95]

# quantile : 25 -> 0.25
print(np.round(float(np.quantile(vib_s, 0.25)), 2))     # 2.28

# 사분위 기반 이상치 범위 - IQR

q1, q3 = np.percentile(vib_s, [25, 75])
iqr = q3 - q1
upper = q3 + 1.5 * iqr
print(vib_s[vib_s > upper])


# 평균/표준편차로 정규화 - z-score
# - 부호의 의미: 양수는 평균보다 위, 음수는 아래
# - 방향 무시하고 크기만 보려면 절댓값 필요

z = (vib_s - np.mean(vib_s)) / np.std(vib_s)
print(vib_s[np.abs(z) > 2])


num = 2
print("=" *3,f"실습 {num}","=" *3)
temp = col(1)
q1, q3 = np.nanpercentile(temp, [25, 75])
iqr = q3 - q1
upper = q3 + 1.5 * iqr

outliers = temp[temp > upper]

print(f"중간 점검 - Q1: {q1:.2f}, Q3: {q3:.2f}, IQR: {iqr:.2f}")
print(f"상한 경계: {upper:.2f}")
print(f"걸리는 값: {outliers}")
print(f"이상치 건수: {len(outliers)}건")

num = 3
print("=" *3,f"실습 {num}","=" *3)
cyc = col(0)
temp = col(1)

mean_t = np.nanmean(temp)
std_t = np.nanstd(temp)

z = (temp - mean_t) / std_t
mask = np.abs(z) > 2

print(f"최대 z-score: {np.nanmax(np.abs(z)):.2f}")
print("이상 사이클 번호:", cyc[mask].astype(int))