# 입력 (input)
# 주의) 사용자 입력은 항상 "문자열"
#형식 : 변수 = input("안내문구: ")
#name = input("이름: ")
#age = input("나이: ")
#print(name)

# 형변환 - int() , float() , str()
#print(age + 1)        #TypeError
#print(int(age) + 1)   #int() 형변환후 실행

# 실습 내용은 주석 해제후 확인할것!!!!!!!!!!!!!!!!!

#=== 실습 1 === 숫자 입력 받아 계산하기
#birth_year = int(input("출생년도: "))
#age = 2026 - birth_year
#print("나이: ",age,"세")

#height = fioat("172.7")  #float() 실수 변화

#=== 실습 2 === 여러개의 값 입력받기
#name = input("국가: ")
#city = input("지역: ")
#print("국가: ",name,"지역: ",city)

#=== 실습 3 === 두 수 입력 받아 사칙연산
#a = int(input("수1: "))
#b = int(input("수2: "))
#print("합: ",a + b)
#print("합: ",a * b)

#=== 실습 4 === 입력값 비교해 출력하기
#temp = int(input("온도: "))
#print(10 < temp <= 50)

#=== 실습 5 === 입력.변환.계산.비교.출력(종합)
#김학생 = int(input("김학생_점수: "))
#이학생 = int(input("이학생_점수: "))
#박학생 = int(input("박학생_점수: "))
#print("평점: ",(김학생 + 이학생 + 박학생) / 3)
#avg = ((김학생 + 이학생 + 박학생) / 3)
#print("60점이상: ",avg >=60)
