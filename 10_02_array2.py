import numpy as np

# 인덱싱, 슬라이싱
a = np.array([0, 1, 2, 3, 4])
print(a[0], a[-1])              # 0 4
print(a[1:4])                   # [1 2 3]
print(a[::2])                   # [0 2 4]

num = 1
print("=" *3, f"실습 {num}","=" *3)
temp = np.array([4603, 4610, 4595, 4620, 4580, 4605, 4615, 4590, 4600, 4603])
print("맨 앞 값:", temp[0]) 
print("맨 뒤 값:", temp[-1]) 
print("2~4번째 구간:", temp[1:4])
print("하나 걸러 하나씩:", temp[::2])

num = 2
print("=" *3, f"실습 {num}","=" *3)
data = np.array([
    [4603, 2.1],
    [4610, 2.3],
    [4595, 2.2],
    [4620, 2.5]
])
print("세 번째 시점 한 줄:", data[2])
print("모든 시점 회전수(0열):", data[:, 0])
print("모든 시점 토크(1열):", data[:, 1])