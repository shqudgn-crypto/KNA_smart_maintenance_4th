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
answer = 7
guess = 0
while guess != answer:
    guess = int(input("맞혀 보세요 (정답 맞추기): "))
print("정답입니다!")