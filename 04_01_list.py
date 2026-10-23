# 리스트
# 형식 : 이름 = [값1, 값2,~~]
# - 리스트는 여러 값을 '순서대로' 하나의 이름에 담는다

temps = [25, 26, 27, 28, 29] # 숫자 리스트
machines = ["펌프", "모터", "압축기"]
mixed = ['펌프', 87, True]   # 종류가 달라도 한 리스트에 담을 수 있음

print(len(temps)) # 5
print(len([]))    # 0 (공백)

print("=" *3,"실습 1","=" *3) # 나만의 데이터 리스트 만들기
temps = [1, 5, 10, 36, 45, 26, 78]
print(temps)
print(len(temps))   # 7
print(len([]))      # 0

print("=" *3,"실습 2","=" *3) # 인덱스로 값 꺼내기
temps = [1, 5, 10, 36, 45, 26, 78]
print(temps[0],'/',temps[2],'/',temps[-1])

print("=" *3,"실습 3","=" *3) # 인덱스로 꺼낸 값 계산하기
temps = [200, 230, 300, 287, 304, 193, 292]
합 = (temps[0] + temps[-1])
평균 = (합 /2)
print(f'합계:{합} / 평균:{평균}')

print("=" *3,"실습 4","=" *3) # 슬라이싱으로 구간 자르기
temps = [49,65,29,58,32,12,34,45,57,39]
앞3 = temps[0:3]
뒤3 = temps[-3:]
길이 = len(앞3)
print(f'{앞3,뒤3,길이}')

print("=" *3,"실습 5","=" *3) # 데이터를 두 구간으로 나누기
temps = [49,28,65,48,29,58,32,12,34,45,94,57]
first = temps[0:6]
second = temps[-6:]
print(f'{first}/{second} {len(first)} {len(second)}')

# 값 바꾸기 / in 존재 확인
# 형식 : 리스트[번호] = 새 값 / 값 in 리스트
nums = [25, 26, 24, 28, 27]
nums[2] = 99
print(nums)  # [25, 26, *99, 28, 27] 
print('모터' in machines) # True

# 값 추가 - append, insert, extend
# 형식 : 리스트.append(값) / 리스트.insert(위치,값) / 리스트.extend(다른 리스트)
data = [25, 26, 27]
#data.append(28)          # [25, 26, 27, 28] - 28추가
#data.insert(1,99)        # [25, 99, 26, 27] - 1번자리에 99로 추가
#data.extend([30,31])     # [25, 26, 27, 30, 31]
print(data)

print("=" *3,"실습 6","=" *3) # 값 찾아 바꾸기
온도 = [25, 26, 240, 28]
print(240 in 온도)
print(온도.index(240))
온도[2] = 24
print(온도)
print(240 in 온도)

print("=" *3,"실습 7","=" *3) # 측정값 추가하기
빈리스트 = []
빈리스트.append(30)
print(빈리스트)
빈리스트.insert(0,28)
print(빈리스트)
빈리스트.extend([31,32])
print(빈리스트)

# 값 삭제 - remove, del
# 형식 : 리스트.remove(값) / 꺼낸 값 = 리스트.pop(위치) / del 리스트[위치]
d = [25, 26, 24, 28, 27]
d.remove(24)    # [25, 26, 28, 27]
print(d)
got = d.pop(1) 
print(got, d)   # 26 [25, 28, 27]
del d[0]
print(d)        # [28, 27]

# 정렬, 탐색 - sort, reverse / count, index
# 형식 : 리스트.sort()  .reverse()  .count(값)  .index(값)
#l = [27, 24, 30, 22, 26]
#l.sort()    #
#l.sort(reverse=True)
#l.reverse()
#print(l)

r = ["정상", "이상", "정상", "정상","이상"]
print(r.count("정상"),r.index("이상"))  # 3 1

print("=" *3,"실습 8","=" *3) # 잘못된 값 제거하기
temps = [25, 26, 999, 24, 28, 26]
temps.remove(999)
print(temps)
removed_val = temps.pop(1)
print(f'꺼낸값 {removed_val}')
del temps[0]
print(temps)

print("=" *3,"실습 9","=" *3) # 정렬하고 탐색하기
temps = [26, 22, 28, 24, 30, 24, 27]
temps.sort()
print(temps)
temps.reverse()
print(temps)
temps.sort()
target_count = temps.count(24)
target_index = temps.index(24)
print(target_count) 
print(target_index)