# 셋 = 중복 자동제거, 순서 없음
# 형식 : {값1, 값2} 또는 set(리스트)
# - 빈 셋 set()
logs = ["S01", "S02", "S01", "S03"]
unipue_logs = set(logs)
print(unipue_logs)              # {'S01', 'S03', 'S02'} 셋은 순서가 없어 인덱싱 불가
print(sorted(unipue_logs))      # ['S01', 'S02', 'S03']

# add - 값 추가
alerts = {"S01","S02"}
alerts.add("S03")
print(alerts)
print("S02"in alerts) # 동일한 값이 있는지 확인 True

print("=" *3,"실습 4","=" *3) # 셋으로 중복 센서 제거하기
lest = ["ddd", "ccc", "aaa", "ddd"]
print(lest)
log = set(lest)
print(log)
print(sorted(log))
print(len(log))

# 집합 연산 -union(전체) / intersection(공통) / difference(차이)
#line_a = {"S01","S02","S03"}
#line_b = {"S03","S04"}
#print(line_a.union(line_b))
#print(line_a.intersection(line_b))
#print(line_a.difference(line_b))

print("=" *3,"실습 5","=" *3) # 두 라인의 센서 구성 비교하기
line_a = {"S01","S02","S03","S05"}
line_b = {"S03","S04"}
print("전체: ",line_a.union(line_b))
print("공통: ",line_a.intersection(line_b))
print("a만: ",line_a.difference(line_b))
print("b만: ",line_b.difference(line_a))

print("=" *3,"실습 6","=" *3) # 두 시점 이벤트 센서 추적하기
today = {"A01","A02","A03","A05"}
yesterday = {"A03","A04"}
print("신규이상: ",today.difference(yesterday))
print("지속이상: ",today.intersection(yesterday))
