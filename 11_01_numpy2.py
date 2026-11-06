import numpy as np

F = 'data/11_diecasting_series.csv'

ct = np.genfromtxt(F, delimiter=",", skip_header=1,usecols=1)
print(ct.shape, ct.dtype)       # (50,) float64

def col(c):
    return np.genfromtxt(F, delimiter=",", skip_header=1, usecols=c)

# 자리 찾기
# fancy indexing : 여러 위치 한번에 추출 가능 (떨어진 자리도 한번에 가능)

vib = np.array([2.1, 2.3, 2.0, 5.8])
pick = np.array([0, 3])
print(vib[pick])        # [2.1 5.8]


# 정렬과 정렬 순서
# - sort, argsort : 원래 자리 번호 돌려줌

print(np.sort(vib))         # [2.  2.1 2.3 5.8]
print(np.argsort(vib))      # [2 0 1 3]

num = 1
print("=" *3, f"실습 {num}","=" *3)
cyc = col(0)
ct = col(1)

idx = ct.argmax()
print(cyc[idx], ct[idx])        # 50.0 6170.0

# diff
vib = np.array([2.0, 2.1, 2.2, 7.0, 7.1])
change = np.diff(vib)
print(np.round(change, 1))      # [0.1 0.1 4.8 0.1]
print(np.argmax(change))        # 2

# clip - 보정
pres = np.array([4.5, 9999.0, 4.6, -1.0])
fixed = np.clip(pres, 0, 10)
print(fixed)

# num = 2
# print("=" *3, f"실습 {num}","=" *3)
# cyc = col(0)
# ct = col(1)

change = np.abs(np.diff(ct))
j =change.argmax()
print(int(cyc[j]), int(cyc[j+1]),round(change[j],1))

# cumsum - 누적 합
defects = np.array([0, 1, 0, 2, 3, 5])
print(np.cumsum(defects))

# np.where 심화
vib = np.array([2.1, 3.5, 2.0, 6.2])
label = np.where(vib >= 5, 2, np.where(vib >= 3, 1, 0))
print(label)

# unique - 중복 정리
# - return_counts 옵션: 각 종류의 개수 확인
status = np.array([0, 0, 1, 0, 2, 1, 0])
kinds, counts = np.unique(status, return_counts =True)
print(kinds)
print(counts)

# num = 3
# print("=" *3, f"실습 {num}","=" *3)
# cyl = col(2)
# cyl[0] = 9999
# print(round(cyl.mean(), 1))     # 421.5

# fixed = np.clip(cyl, 100, 300)
# print(round(fixed.mean(), 1))    # 227.5

# num = 4
# print("=" *3, f"실습 {num}","=" *3)
# ct = col(1)
# lable = np.where(ct >= 1000, 2, np.where(ct >= 50, 1, 0))

# kinds, count = np.unique(label,return_counts=True)
# print(kinds, count)
# print(count / count.sum())

# any, all - 조건 충족 여부 판정
# - any: 하나라도 만족하면 True
# - all: 모두 만족해야 True

vib = np.array([2.1, 3.5, 2.0, 6.2])
print(np.any(vib > 5))    # True
print(np.all(vib < 10))   # True

# concatenate, stack - 배열 합치기
am = np.array([2.0, 2.1, 2.2])
pm = np.array([2.3, 2.4, 2.5])
print(np.concatenate([am, pm]))   # [2.  2.1 2.2 2.3 2.4 2.5]
print(np.stack([am, pm]))
#[[2.  2.1 2.2]
#  [2.3 2.4 2.5]]

# num = 5
# print("=" *3, f"실습 {num}","=" *3)
# M = np.stack([col(1), col(2), col(3), col(4)])
# print(M.shape)

# recent = M[:, -10:]
# print(recent.shape)

num = 6
print("=" *3, f"실습 {num}","=" *3)
cyc, ct, cyl = col(0), col(1), col(2)

i = ct.argmax()
print(int(cyc[i]), ct[i])                    # 50 6170.0

ch = np.abs(np.diff(ct))
j = ch.argmax()
print(int(cyc[j]), int(cyc[j+1]))           # 49 50

warn = np.where((ct >= 50) | (cyl < 150), 1, 0)
print(round(warn.mean(), 2))      # 0.12

top = np.argsort(ct)[::-1][:3]
print(top)      # [49 47 42]  -> 인덱스
print(cyc[top])   # [50. 48. 43.]