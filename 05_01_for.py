# for 반복문
# for문 (range 이용한 반복)
# 형식 : for 변수 in range(횟수):
#for i in range(5):
#    print("안녕하세요")

#for i in range(5):
#    print(i)            # 0 1 2 3 4 

# range (시작, 끝, 증가값)

#for i in range(1,6):
#    print(i)            # 1 2 3 4 6

#for i in range(1,10,2):
#    print(i)            # 1 3 5 7 9

#for i in range(5,0,-1):
#    print(i)            # 5 4 3 2 1

print("=" *3,"실습 1","=" *3) # range로 숫자 흐름 출력하기
#for i in range(1,7):
#    print(i)            # 1 2 3 4 6
#print("순서대로","=" *10)

#for i in range(0,12,2):
#    print(i)            # 1 3 5 7 9
#print("짝수","=" *10)

#for i in range(6,0,-1):
#    print(i)            # 5 4 3 2 1
#print("역순","=" *10)

# 누적 변수 패턴 (합계, 갯수 , 평균)
total =1
for i in range(1,6):
    total += i
print("합계:", total)   # 합계 16

# 조건을 만족하는 경우 세기
count = 0
for i in range(1,11):
    if i > 5:
        count +=1
print("갯수: ", count)

# 평균
#total, count =0,0
#for i in range(1,6):
#    total
#    count += 1
#if count > 0:
#    print("평균: ", total/count)

print("=" *3,"실습 2","=" *3) # 반복으로 1부터 N까지 합계 구하기
#n = int(input("N을 입력하세요: "))
#total = 0
#for i in range(1, n + 1):
#    total += i 
#print(f"(N={n}) 합: {total}")

# enumerate : 순서 + 값을 함께 준다
temps = [25, 26, 27]
for idx, t in enumerate(temps):
    print(idx + 1,"번째: ", t)  # 1 번째:  25~ 2 번째:  26~ 3 번째:  27

# 중첩 반복 (바깥 한 바퀴마다 안쪽이 처음부터 끝까지)
#for dan in range(2,4):      # 바깥: 2, 3단
#    for su in range(1,4):   # 안쪽: 1,2,3 (바깥 한번마다 3번씩)
#        print(f'{dan} x {su}={dan * su}')
#    print("------")

print("=" *3,"실습 3","=" *3) # 중첩 반복으로 구구단 출력하기
for dan in range(2,10):      
    for su in range(1,10):   
        print(f'{dan} x {su}={dan * su}')
    print("------")

print("=" *3,"실습 4","=" *3) # 기준을 초과하는 값의 개수 세기
n = int(input("측정 횟수를 입력하세요: "))
count = 0
for i in range(n):
    val = int(input("측정값을 입력하세요: "))
    if val > 80:
        count += 1
print("초과 개수:", count)