import pandas as pd

F_SMALL= 'data/13_diecasting_small.csv'
F_SHOT = 'data/13_diecasting_shot.csv'

# 열 골라내기
# - 열 이름
df = pd.read_csv(F_SMALL)

# print("이름으로 앞 3개:", df["실린더압력"].head(3).tolist())    # [214.0, 217.0, 215.0]

# 단일 열 선택
# - df["실린더압력"]
# - 결과 값은 Series
# print(df["실린더압력"])
# 0     214.0
# 1     217.0
# 2     215.0

# 복수 열 선택
# - 여러 열은 이름들을 리스트로 묶어서 넣는다
# - 결과 값은 DataFrame
# print(df[["형체력", "실린더압력"]])

num = 1
print("=" *3,f"실습 {num}","=" *3)
# print(df["실린더압력"])
# print(df[["형체력", "실린더압력"]])


# 행 선택
# - 라벨과 위치 번호의 창이
# - 라벨: 그 행에 붙은 이름표 = 인덱스 값
# - 위치 번호: 맨 위에서부터 몇 번쨰인지, 항상 0부터

sorted = df.sort_values("형체력", ascending= False)

print("정렬 후 인덱스 앞 4개: ", sorted.index[:4].tolist())  # 정렬 후 인덱스 앞 4개:  [22, 17, 27, 12]
print("정렬 후 iloc[0] 샷: ", int(sorted.iloc[0]['샷']))    # 정렬 후 iloc[0] 샷:  23
print("정렬 후 loc[0] 샷: ", int(sorted.loc[0, '샷']))      # 정렬 후 loc[0] 샷:  1

# 여러 행 선택
print(df.loc[0:4].shape)        # (5, 8)
print(df.iloc[0:4].shape)       # (4, 8)

# 행, 열 동시 선택
# df.loc[행,열] - 열 이름 사용o / df.iloc[행,열] - 열이름 사용x ->숮자로 접근
print(df.loc[0:4, ['실린더압력', '형체력']].shape)
print(df.iloc[0:5, [2, 6]].shape)

num = 2
print("=" *3,f"실습 {num}","=" *3)
print(df.loc[0, '샷'])
print(df.loc[0]['샷'])

sorted + df.sort_values('형체력', ascending=False)
print(sorted.loc[0, '샷'])
print(sorted.loc[0]['샷'])

num = 3
print("=" *3,f"실습 {num}","=" *3)
print(list(df.columns))

a = df.loc[0:4,['실린더압력','형체력']]
print(a.shape)

b = df.iloc[0:5, [2, 6]]
print(b.shape)
print(a.equals(b))

num = 4
print("=" *3,f"실습 {num}", "=" *3)
print("--- 앞쪽 10줄 (loc) ---")
print(df.loc[0:9, ['설비ID', '비스킷두께', '품질등급']])

# ② 맨 뒤 5줄 전체 추출 (iloc)
print("\n--- 맨 뒤 5줄 (iloc) ---")
print(df.iloc[-5:, :])