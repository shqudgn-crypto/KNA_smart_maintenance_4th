# while - 조건이 참인 동안 반복
# 형식 :
# while 조건식:         (조건이 거짓이 되는 순간 멈춤)
#for - "몇 번" 이 정해 졌을때,whiledms '언제 끝날지 모르지만 조건으로 멈출 때' 사용

count = 4
while count <= 3:
    print(count)
    count += 1
# 주의) 무한 루프를 막으려면 (1)언젠가 거짓이 될 조건, (2)반복문 안에서 그 조건을 갱신
# 처음부터 조건이 거짓이면 한번도 실행되지 않는다

print("=" *3,"실습 1","=" *3) # while로 목표값 도달까지 반복하기
#answer = 7
#guess = 0
#while guess != answer:
#    guess = int(input("맞혀 보세요 (정답 맞추기): "))
#print("정답입니다!")

# break - 반복 도중에 완전히 멈추기
for i in range(1,11):
    if i == 5:
        break           # 5를 만나면 반복 즉시 종료
    print(i)            # 1 2 3 4

for i in range(1,7):
    if i % 2 == 0:
        continue
    print(i)            # 1 3 5

print("=" *3,"실습 2","=" *3) # 플래그로 조건 만족 값 검색하기
# ① 찾음 여부 플래그를 False로 준비하고 횟수 입력받기
found = False
n = int(input("측정 횟수를 입력하세요: "))

for i in range(n):
    v = int(input(f"{i+1}번째 측정값: "))
    if v > 80:
        found = True
        break
    
if found:
    print("결과: 80 초과 값이 하나라도 있습니다! (발견)")
else:
    print("결과: 80 초과 값이 없습니다. (모두 정상)")