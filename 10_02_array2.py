import numpy as np

# # 인덱싱, 슬라이싱
# a = np.array([0, 1, 2, 3, 4])
# print(a[0], a[-1])              # 0 4
# print(a[1:4])                   # [1 2 3]
# print(a[::2])                   # [0 2 4]

# num = 1
# print("=" *3, f"실습 {num}","=" *3)
# temp = np.array([4603, 4610, 4595, 4620, 4580, 4605, 4615, 4590, 4600, 4603])
# print("맨 앞 값:", temp[0]) 
# print("맨 뒤 값:", temp[-1]) 
# print("2~4번째 구간:", temp[1:4])
# print("하나 걸러 하나씩:", temp[::2])

# num = 2
# print("=" *3, f"실습 {num}","=" *3)
# data = np.array([
#     [4603, 2.1],
#     [4610, 2.3],
#     [4595, 2.2],
#     [4620, 2.5]
# ])
# print("세 번째 시점 한 줄:", data[2])
# print("모든 시점 회전수(0열):", data[:, 0])
# print("모든 시점 토크(1열):", data[:, 1])

# # 배열 연산
# a = np.array([1, 2, 3])
# b = np.array([10, 20, 30])
# print(a + b)                    # [11 22 33]
# # 같은 위치 값끼리 계산 (반목문 필요x)
# # 사칙연산 모두 같은 방식으로 계산

# # 스칼라 연산
# # - 숫자 하나를 배열 전체에 적용, 크기를 맞출 필요가 없다
# # - 연산 숫자는 수학과 같아서 곱하기 먼저 진행
# print(a * 10 + 3)

# # 브로드캐스팅
# table = np.array([[72, 2.4],[95, 6.8]])
# print(table.shape)                          # (2, 2)
# base = np.array([70,2.0])
# print(table - base)
# # [[ 2.   0.4]
# #  [25.   4.8]]
# # 한 줄짜리 기준값이 모든 행에 퍼져서 계산됨
# # 조건) 작은 쪽 크기가 1이거나 같아야 함
# # base.min() base.max()         최소값, 최대값

# num = 3
# print("=" *3, f"실습 {num}","=" *3)
# data = np.array([39, 67, 90, 23, 67, 45, 89, 12, 29, 10])
# max_val = data.max()
# min_val = data.min()

# normalized = (data - min_val) / (max_val - min_val)
# print("정규화 결과:", np.round(normalized, 2))

# # 비교 연산과 불리언 배열
# # 비교 연산
# vals =np.array([10, 95, 71, 88, 73])
# print(vals > 75)                        # [False  True False  True False]

# # 불리언 인덱싱
# # - 조건이 참/거짓인 배열을 만들고 -> 그 배열을 대괄호에 넣으면 참인 값만 남음
# print(vals[vals > 75])                  # [95 88]

# # np.where(조건, 참일 때 값, 거짓일 때 값)
# print(np.where(vals > 85, 1, 0))        # [0 1 0 1 0]

# # 다중 조건
# print(vals[(vals > 70) & (vals < 90)])  # [71 88 73]

# num = 4
# print("=" *3, f"실습 {num}","=" *3)
# rpm = np.array([4603, 4603, 58, 4603, 4603,
#                 1216, 4603, 4603, 1217, 4603])
# # 전류 데이터 (실습용 예시값)
# current = np.array([2, 2, 21, 2, 3,
#                     2, 2, 3, 2, 147])
# data = np.array([[4603, 2], [4603, 21]])


# low_rpm = rpm < 2000
# # 회전수 2000 미만
# print(rpm[low_rpm])
# # 회전수 2000 미만 또는 전류 25 초과
# print(rpm[low_rpm], current[current> 25])

# # 개수
# print(np.sum(low_rpm))
# print(np.sum((rpm < 2000) | (current > 25)))

# # 비율
# print(np.mean(low_rpm) * 100, "%")
# # - low_rpm : True False 배열 -> True: 1, False: 0
# print(np.mean((rpm < 2000) | (current > 25))* 100, "%")


# num = 5
# print("=" *3, f"실습 {num}","=" *3)
# tq = np.array([2, 2, 21, 2, 3, 2, 2, 3, 2, 147])
# high = tq > 10
# print(high.sum())   # 2
# print(round(high.mean(), 2))    # 0.2

# # 통계
# # - 정상을 알아야 이상을 알 수 있다
# # ex) 평균을 알아야 평균과 크게 차이가 나는 값이 나왔을 때 이상치 판단 가능
# # - 평균, 최대/최소, 표준편차, 분산
# # - NumPy 에서 함수 하나로 계산

# s = np.array([70, 72, 71, 95, 73])
# print("합계:",s.sum())
# print("평균:",s.mean())
# print("중앙값:",np.median(s))
# print("최대:",s.max())
# print("최소:",s.min())

# # 분산
# stable = np.array([70, 71, 70, 72, 71])
# unstable = np.array([60, 85, 65, 95, 70])
# print(round(stable.var(), 1))       # 0.6
# print(round(unstable.var(), 1))     # 170.0

# # 표준 편차
# print(round(stable.std(), 2))
# print(round(unstable.std(), 2))     # 13.04

# # axis 개념 (행/열 방향)
# mat = np.array([[70, 2.1],[72, 2.3]])
# print(mat.mean(axis=0))     # 열별 평균 (센서별)                    [71.   2.2]
# print(mat.mean(axis=1))     # 행별 평균 (시점별) -지금은 큰의미x     [36.05 37.15] 
# print(mat.mean())           # 전체 평균                             36.6

# num = 6
# print("=" *3, f"실습 {num}","=" *3)
# # 4시점 × 2센서(회전수, 토크) — 실측값
# data = np.array([[4603, 2], [4967, 21],
#                  [3632, 147], [58, 5]])

# print(np.round(data.mean(axis=0), 1))
# print(np.round(data.std(axis=0), 1))

# 파일에서 배열로 불러오기(np.loadtxt)

# rpm = np.loadtxt('data/10_mct_tool.csv',
#                  delimiter=",",         # 값을 나누는 기호
#                  skiprows=1,            # 첫줄(제목)은 건너뜀
#                  usecols=4)             # 5번째 열 = 회전수
# print(rpm)

# num = 7
# print("=" *3, f"실습 {num}","=" *3)
# rpm = np.loadtxt('data/10_mct_tool.csv',
#                  delimiter=",",      # 값을 나누는 기호
#                  skiprows=1,        # 첫 줄(제목)은 건너뜀
#                  usecols=4) 

# print(round(rpm.mean(), 1))
# print(round(rpm.std(), 1))
# print(rpm.min(), rpm.max())

# num = 8
# print("=" *3, f"실습 {num}","=" *3)
# tq = np.loadtxt('data/10_mct_tool.csv',
#                  delimiter=",",      # 값을 나누는 기호
#                  skiprows=1,        # 첫 줄(제목)은 건너뜀
#                  usecols=5) 

# high = tq[tq > 10]
# print(np.round(high, 1))
# print(high.size, round(high.mean(), 1))

num = 9
print("=" *3, f"실습 {num}","=" *3)
rpm_tq = np.loadtxt('data/10_mct_tool.csv',
                 delimiter=",",      # 값을 나누는 기호
                 skiprows=1,        # 첫 줄(제목)은 건너뜀
                 usecols=(4,5))  

rpm = rpm_tq[:, 0]
print(rpm_tq.shape, rpm_tq.dtype)
low = rpm[rpm < 2000]
print(low.size, round(low.mean(), 1))
print(round(rpm.mean(), 1))