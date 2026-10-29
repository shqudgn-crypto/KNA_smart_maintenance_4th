# 함수
# 함수의 기본 구조
# 형식 :
# def 함수이름():
#   실행할 코드

def greet():
    print("점검을 시작합니다")


# 정의만으로는 실행 안됨 -> 호출해야 실행
# 호출: 함수 이름 적고 괄호 붙이기
greet()

print("=" *3,"실습 1","=" *3) # 첫 함수 만들고 호출하기
def greet():
    print("측정 시작합니다")

greet()
greet()

num = 2
print("=" * 3, f"실습 {num}", "=" * 3)  # 반복 코드를 함수로 정리하기
def start_check():
    print("점검을 시작합니다")
    print("안전 장비를 확인하세요")
    print("기록을 준비하세요")
start_check()
start_check()

num = 3
print("=" *3,f"실습 {num}","=" *3)
# hello         # NameError (정의 전 호출 시)
def hello():
    print("안녕하세요")

hello()
hello()

num = 4
print("=" *3,f"실습 {num}","=" *3)
def line():
    print("=" *10)

def check():
    print("점검을 시작합니다")
    print("기록을 준비하세요")    

line()
check()

line()
check()