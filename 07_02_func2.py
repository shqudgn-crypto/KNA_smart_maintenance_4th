# 매개변수와 반환값

# 매개변수와 인자
# 형식 :
# def 함수이름(매개변수):
# ~~
# 호출
# 함수이름(인자)

def check(name):                         # name = 매개변수
    print(name +" 점검을 시작합니다.")

check("압축기1")                         # "압축기1" = 인자
check("펌프1")

num = 2
print("=" *3,f"실습 {num}","=" *3)
def check(name,temp):
    print("이름: "+ name+ ", 온도: " + str(temp)+ " 도")   # 문자열 넣기

check("모터2", 35)
check("압력", 4.5)

# 키워드 인자
def report(name,temp):
    print(name,temp,"도") 

report(temp=78,name="펌프")

num = 3
print("=" *3,f"실습 {num}","=" *3)
def check(name, temp):
    print(name, str(temp) + " (순서 무관)")

check(12 , "모터")
check("펌프", 77)

# return
# - print: 사람이 확인할 수 있게 출력/ return: 값을 프로그램에게 돌려줘서 이어 쓸 수 있게 한다
def add(a,b):
    return a+b
    print("실행 안됨")      # return 을 만나면 즉시 함수 종료 -> 그 아래 코드는 실행 X
total = add(3,4)
print(total)

num = 4
print("=" *3,f"실습 {num}","=" *3)
def add(a,b):
    return a+b
total = add(40,20)
print(total)
print(total /2)

# 여러 값 반환 / 언패키
# - 쉼표로 여러 값을 return 하면 튜플로 묶여 돌아옴 -> 언패킹 가능
def min_max(values):
    return min(values),max(values)

print(min_max([75,10,100]))     # (10, 100)  *75는 중간값이라서 제외
low, high = min_max([75,10,100])
print(low,high)

none = report("펌프", 10)
print(none)                 # None -> return 값이 없는 함수 호출해서 변수로 받을 경우 None

num = 5
print("=" * 3, f"실습 {num}", "=" * 3)

def stats(v):
    low = min(v)
    high = max(v)
    avg = sum(v) / len(v)
    return low, high, avg 

lo, hi, avg = stats([78, 92, 85])

print(lo, hi, avg)