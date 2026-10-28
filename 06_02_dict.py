# 딕셔너리
# 형식 : {키 : 값, 키 : 값} - 키는 문자열
# - 리스트는 번호(인덱스)로 찾지만 딕셔너리는 이름(키)으로 찾는다

#sensors = {"모터온도": 78,"진동": 0.5}
#print(sensors)
#print(sensors["모터온도"])  # 78
#print(type(sensors))       # <class 'dict'> 딕셔너리 로 나옴
#print(sensors["유량"])      # 없는 키는 * KeyError: '유량'

# 추가 / 수정 / 삭제 
# 형식 : 딕셔너리[키] = 값 (없는 키 - 추가, 있는 키 - 수정)
# 형식 : (삭제) del 딕셔너리[키]

#sensors["펌프압력"] = 95         # 추가
#sensors["모터온도"] = 80         # 수정
#del sensors["진동"]              # 삭제 (없는 키 삭제는 오류)
#print(sensors)                   # {'모터온도': 80, '펌프압력': 95}

# get / in
# 형식 : 딕셔너리.get(키,기본값)    / 키 in 딕셔너리
#print(sensors.get("유량"))          # None
#print(sensors.get("유량",0))        # 0
#print("모터온도" in sensors)        # True  (*키만 포함 여부 확인 가능)
#print(80 in sensors)               # False (값은 확인 안됨)

print("=" *3,"실습 1","=" *3) # 딕셔너리 만들고 다루기
sensors = {"모터온도": 78, "진동": 0.5}
print("초기 센서 딕셔너리:", sensors)
print("모터온도 값 조회:", sensors["모터온도"])
print("-" * 30)
sensors["압력"] = 95
sensors["모터온도"] = 80
print("추가·수정된 딕셔너리:", sensors)
print("-" * 30)
print("유량 조회 결과 (기본값 적용):", sensors.get("유량", 0))
print("'모터온도' 키 존재 여부:", "모터온도" in sensors)

# keys / values / items / len
sensors = {"모터온도": 78,"진동": 0.5}
print(sensors.keys())       # ['모터온도', '진동']
print(sensors.values())     # [78, 0.5]
avg = sum(sensors.values()) / len(sensors)
print(avg)                  # 평균 39.25

for name, value in sensors.items():
    print(name,value)

# for k in sensors.keys()
# for v in sensors.values()

# update - 여러 항목 한번에 갱신 (키가 있으면 수정, 없으면 추가)
d = {"온도": 78}
d.update({"온도": 80,"압력": 95})

print("=" *3,"실습 2","=" *3) # update로 여러 값 한 번에 갱신하기
sensors = {"모터온도": 78, "진동": 0.5}
new_data = {"모터온도": 80, "유량": 42}
sensors.update(new_data)
print("갱신된 딕셔너리:", sensors)
del sensors["진동"]
print("삭제 후 딕셔너리:", sensors)
print("센서 수:", len(sensors))

print("=" *3,"실습 3","=" *3) # 딕셔너리로 통계내기
sensors = {"모터온도": 78, "진동": 0.5, "압력": 95}
print("센서 데이터:", sensors)

total_sum = sum(sensors.values())  
total_count = len(sensors)    
total_avg = total_sum / total_count

print(f"평균: {total_avg:.1f}")

max_name = ""
max_value = 0  

for name, value in sensors.items():
    if value > max_value:
        max_value = value
        max_name = name

print(f"최댓값 센서: {max_name} {max_value}")

# zip : 센서명 - 값 매핑하기
name = ["온도","진동","압력"]
value = [78,0.5,95]
sensors = dict(zip(name,value))     # {'온도': 78, '진동': 0.5, '압력': 95}
print(sensors)              

# 딕셔너리의 값에 리스트 / 딕셔너리 - 중첩 딕셔너리
plant = {
    "1번모터": {"온도": 78,"상태": "정상"},
    "2번펌프": {"압력": 95,"상태": "경고"}
}

print(plant["2번펌프"]["압력"])

print("=" *3,"실습 4","=" *3) # zip으로 센서명 -값 매핑하기
name = ["온도","진동","압력"]
value = [78,0.5,95]
sensors = dict(zip(name,value))
print(sensors)
for name, value in sensors.items():
    print(name,value)

print("=" *3,"실습 5","=" *3) # 임계갑으로 경고 센서 분류하기
values = {"모터온도": 95, "압력": 88}
limits = {"모터온도": 90, "압력": 90}
warning_sensors = []    # 경고 센서를 담을 빈 리스트
for name, value in values.items():
    if value > limits[name]:
        warning_sensors.append(name)

print("경고 센서:", warning_sensors)

print("=" *3,"실습 6","=" *3) # 중첩 딕셔너리로 설비 관리하기
plant = {
    "1번모터": {"온도": 78,"상태": "정상"},
    "2번펌프": {"압력": 95,"상태": "경고"}
}
print(plant["2번펌프"]["압력"])

for name, info in plant.items():
    if info["상태"] == "경고":
        print(name, "점검필요")

print("=" *3,"실습 7","=" *3) # 표 데이터를 딕셔너리로 변환하기
rows = ["모터온도,78.5", "압력,95.0", "진동,0.5"]
sensors = {}
for row in rows:
    name, value = row.split(",")
    sensors[name] = float(value)

print("변환된 딕셔너리:", sensors)

print("=" *3,"실습 8","=" *3) # 
sensors = {"온도": 95, "압력": 96}
limits = {"온도": 90, "압력": 90}

# values() 이용한 평균
avg = sum(sensors.values()) / len(sensors)
print("평균:", round(avg, 1))

# items() 순회 -> 임계값 비교 -> 초과한 값은 셋에 담기(키 값 담기)
danger = set()
for name, v in sensors.items():
  if v > limits[name]:
    danger.add(name)

# 셋 정렬하여 출력
print("위험 센서:", sorted(danger))