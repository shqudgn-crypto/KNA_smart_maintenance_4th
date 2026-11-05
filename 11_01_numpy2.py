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

num = 2
print("=" *3, f"실습 {num}","=" *3)