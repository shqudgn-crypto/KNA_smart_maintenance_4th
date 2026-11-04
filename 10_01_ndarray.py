import numpy as np

# 리스트 vs 배열
# 1) 리스트
# - 서로 다른 자료형도 같이 존재 가능
# - 계산이 느리고 바복문을 돌아야 한다
list = [70,72,71]
print(list *2)  # [70, 72, 71, 70, 72, 71]
print([v * 2 for v in list])    # [140, 144, 142]

# 2) 배열
# - 같은 자료형만 존재 가능
# - 계산이 빠르다

temp = np.array([70, 72, 71])
print(temp)     # [70 72 71]

print(temp + 2) # [72 74 73] -> 반복문 없는 묶음 계산

# 튜플로 배열 만들기
print(np.array((1, 2, 3)))  # [1 2 3]
num = 1
print("=" *3,f"실습 {num}","=" *3)
temp = np.array([70.5, 69.8, 73.7, 71.2, 72.0, 68.9])
print("섭씨 온도:", temp)
print("화씨 온도:", (temp *1.8) + 32)

# 배열 생성
# mp.arange(시작, 끝, 간격) : 연속 정수
# - 끝값은 포함되지 않음
print(np.arange(5))             # [0 1 2 3 4]
print(np.arange(0, 10, 2))      # [0 2 4 6 8]

# np.linspace(시작, 끝, 개수) : 균등 분할
# - 끝값 포함
print(np.linspace(0, 1, 5))     # [0.   0.25 0.5  0.75 1.  ]
print(np.linspace(0, 10, 5))    # [ 0.   2.5  5.   7.5 10. ]

num = 2
print("=" *3,f"실습 {num}","=" *3)
print(np.linspace(0, 70, 8))        # [ 0. 10. 20. 30. 40. 50. 60. 70.]

num = 3
print("=" *3,f"실습 {num}","=" *3)
print(np.linspace(0, 40, 5))        # [ 0. 10. 20. 30. 40.]

# 배열 속성
# - ndim, shspe, size, dtype
# - 속성은 괄호 x

a = np.array([1, 2, 3])
b = np.array([[1, 2, 3],[4, 5, 6]])

print("dim", a.ndim, b.ndim)        # dim 1 2
print("shape", a.shape, b.shape)    # shape (3,) (2, 3)
print("size", a.size, b.size)       # size 3 6

num = 4
print("=" *3,f"실습 {num}","=" *3)
# 4시점 × 2센서(온도, 전류)
data = np.array([[30, 15.44], [30, 18.69],
                 [30, 62.48], [30, 18.37]])
print(data.ndim)
print(data.shape)
print(data.size)

num = 5
print("=" *3,f"실습 {num}","=" *3)
import numpy as np
current = np.array([18.69, 20.45, 19.12, 21.88])
print("자료형 확인:", current.dtype)

current_int = current.astype(int)
print("정수로 변환된 배열:", current_int)

# reshape() 로 형태 바꾸기
# - -1 사용 시 자동 계산
c = np.arange(12)
print(c.reshape(3, 4))
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# flatten() -> 1차원 만듦
b3 = np.array([[1, 2, 3],[4, 5, 6]])
print(b3.flatten())                     # [1 2 3 4 5 6]


num = 6
print("=" *3,f"실습 {num}","=" *3)
# 사이클타임 12회 측정 (실측값)
ct = np.array([21156, 15611, 15633, 15601,
               15607, 15557, 15557, 15636,
               15600, 15634, 21207, 15554])
print(ct.reshape(3, 4))

num = 7
print("=" *3,f"실습 {num}","=" *3)
# 4시점 × 3센서(온도, 전류, 회전수)를 한 줄로 이어 놓은 상태
flat = np.array([30, 15.44, 4603, 30, 18.69, 4603,
                 30, 62.48, 4967, 30, 18.37, 4603])

table = flat.reshape(4, 3)
print(table)
print(table.flatten())