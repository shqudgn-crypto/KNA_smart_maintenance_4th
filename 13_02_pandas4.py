import pandas as pd

F_SHOT = 'data/13_diecasting_shot.csv'

# 조건 필터링과 정렬
df = pd.read_csv(F_SHOT)
print(df.shape)

# # 배열에서 하던 것
# arr = df["비스킷두께"].values
# print("배열에서 조건 참 개수: ", int((arr >= 16).sum()))               # 74

# # 표에서 하는 것
# print("표에서 조건 참 개수: ", int((df ["비스킷두께"] >= 16).sum()))    # 74

# # 조건 -> boolean series
# s = df["비스킷두께"] >= 16
# print(s.head(3).tolist())                                   # [False, False, False]

# print(int(df["비스킷두께"].isna().sum()))   # 14
# print(int((df["비스킷두께"] < 16).sum()))   # 112


# # 복합 조건
# both = df[(df["비스킷두께"] >= 16) & (df["사이클타임"] >= 25)]
# either = df[(df["비스킷두께"] >= 16) & (df["사이클타임"] >= 25)]
# print(len(both), len(either))

# # 부정 조건 : ~
# print(len(df[~(df["품질등급"] == "불량")]))

# # isin : 값이 포함되어 있는지
# print(len(df[df["품질등급"].isin(['주의', '불량'])]))   # | 사용과 같은 결과

# # between : 사이를 의미(양쪽 경계 모두 포함)
# print(len(df[df["비스킷두께"].between(10, 16)]))

# # 문자열 조건
# # -str.contains : 해당 문자열을 포함하는 값
# print(len(df[df["설비ID"].str.contains("A")]))  # A라인 전체

# # - str.split, str.erplace, str.strip ~
# print(df["설비ID"].head(1).tolist())                    # ['DIE-A-01']
# print(df["설비ID"].str.split("-").head(1).tolist())     # [['DIE', 'A', '01']]


# num = 2
# print("=" *3,f"실습 {num}","=" *3)
# cond_both = (df['비스킷두께'] >= 16) & (df['사이클타임'] >= 25)
# cond_either = (df['비스킷두께'] >= 16) | (df['사이클타임'] >= 25)
# cond_defect = ~(df['품질등급'] == '불량')
# print("그리고:", len(df[cond_both]), "또는:", len(df[cond_either]), "불량 아님:", len(df[cond_defect]))


# num = 3
# print("=" * 3, f"실습 {num}", "=" * 3)

# cond_isin = df['품질등급'].isin(['주의', '불량'])
# cond_between = df['비스킷두께'].between(10, 16)
# cond_contains = df['설비ID'].str.contains('A')
# cond_exact = df['설비ID'] == 'DIE-A-01'

# print("목록 매칭 줄 수:", len(df[cond_isin]))
# print("범위 검사 줄 수:", len(df[cond_between]))
# print("글자 포함 줄 수:", len(df[cond_contains]), "/ 정확히 일치 줄 수:", len(df[cond_exact]))

# 정렬, 복사본
# 정렬 - sort_values
asc = df.sort_values("비스킷두께")
print(asc["비스킷두께"].head(3).tolist())

# 다중 키 정렬, 내림 차순
dec = df.sort_values("사이클타임", ascending=False)
print(dec["사이클타임"].head(3).tolist())               # [6170.0, 652.3, 125.9]

# 다중 키 정렬
two = df.sort_values(["품질등급","비스킷두께"], ascending=[True, False])
print(two["샷"].head(3).tolist())                       # [198, 192, 197]

# copy
x = df[df["품질등급"] == "불량"].copy()
print(x.shape)      # (20, 8)
x["위험등급"] = "높음"
print(x.shape)      # (20, 9)

num = 4
print("=" * 3, f"실습 {num}", "=" * 3)
sorted = df.sort_values("비스킷두께", ascending=False)
print(sorted["샷"].head(5).tolist())

sorted2 = df.sort_values(["품질등급", "사이클타임"], ascending=[True, False])
print(sorted2["샷"].head(5).tolist())

print(df["샷"].head(3).tolist())

num = 5
print("=" * 3, f"실습 {num}", "=" * 3)
state = df[(df["품질등급"] != "양품") & (df["비스킷두께"] >= 16)]
print(len(state))

sort_df = state.sort_values("비스킷두께", ascending=False)
report = sort_df[["설비ID", "비스킷두께", "품질등급"]]
print(report.head(3))
#          설비ID  비스킷두께 품질등급
# 197  DIE-A-01   27.0   불량
# 191  DIE-B-01   26.0   불량
# 42   DIE-A-01   21.0   주의

# 결측 때문에 제외된 양품 아닌 샷 확인
x = df[(df["품질등급"] != "양품") & df["비스킷두께"].isna()]
print(len(x))      # 3