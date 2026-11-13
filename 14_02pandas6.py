import pandas as pd

F = 'data/14_hydraulic.csv'
F_QC = 'data/14_hydraulic_qc.csv'

# 그룹 통계와 상관관계
# - 그룹 통계 -> 원본 행과 그룹 기준 비교 -> 두 기준 표 -> 상하관계

df = pd.read_csv(F)
qc = pd.read_csv(F_QC)

# print(round(df["온도"].mean(), 2))
# print(round(df["온도"].std(), 2))

# print(df.groupby("냉각기상태")["온도"].mean().round(2))
# # 냉각기상태
# # 고장    54.67
# # 저하    45.46
# # 정상    35.89

# print(df.groupby("냉각기상태")["온도"].std().round(2))
# # 냉각기상태
# # 고장    3.76
# # 저하    1.47
# # 정상    0.36

# # 분산 / 표준편차
# v = df.groupby("냉각기상태")["온도"].var()
# std = df.groupby("냉각기상태")["온도"].std()
# print(v.round(2))
# # 냉각기상태
# # 고장    14.13
# # 저하     2.15
# # 정상     0.13

# print(std.round(2))
# # 냉각기상태
# # 고장    3.76
# # 저하    1.47
# # 정상    0.36

# print((std **2).round(2))
# # 냉각기상태
# # 고장    14.13
# # 저하     2.15
# # 정상     0.13


# agg - 여러 통계 한번에 표로 모으기
# ㄴ 리스트: 같은 대상에 여러 통계
# ㄴ 딕셔너리: 열별 통계
# ㄴ named aggregation: 결과 열의 이름까지 지정

# print(df.groupby("냉각기상태")["온도"].agg(["mean", "std", "max"]).round(2))
# print(df.groupby("냉각기상태")[["온도", "진동"]].agg(["mean", "std", "max"]).round(2))

# # 이름 붙이기
# summary = df.groupby("냉각기상태").agg(
#   평균온도=("온도", "mean"),
#   평균진동=("진동", "mean")
# )
# print(summary.round(2))

# # 열별로 다른 통계 목록 지정
# summary2 = df.groupby("냉각기상태").agg({
#   "온도": ["mean", "std"],
#   "진동": ["mean", "max"]
# })
# print(summary2.round(2))

num = 1
print("=" *3,f"실습 {num}","=" *3)
# print(qc["검사결과"].value_counts())
# # print(qc.groupby("검사결과")["온도"].agg(["mean", "std", "max"]).round(2))

# # table = qc.groupby("검사결과").agg(
# #   평균온도=("온도", "mean"),
# #   평균냉각효율=("냉각효율", "mean"),
# #   측정수=("온도", "count"),
# # )
# # print(table.round(2))

# # transform = 그룹 통계를 월래 행에 붙이기
# # - 원래 행 인덱스와 모양을 유지한다

# # 같은 그룹의 평균 붙이기
# print(df.groupby("냉각기상태")["온도"].mean().shape)     # (3,)
# print(df.groupby("냉각기상태")["온도"].transform("mean").shape)   # (120,)

# marked = df.copy()
# marked["그룹평균"] = marked.groupby("냉각기상태")["온도"].transform("mean")
# marked["편차"] = marked["온도"] - marked["그룹평균"]
# print(marked[["냉각기상태", "온도", "그룹평균", "편차"]].head(3).round(2))
# #   냉각기상태    온도   그룹평균     편차
# # 0    고장  35.6  54.67 -19.07
# # 1    고장  47.5  54.67  -7.17
# # 2    고장  50.7  54.67  -3.97

# pivot_table - 두 기준 표를 한 번에
# - margins=True -> 전체 집계 추가
# - 값이 없는 조합의 평균을 0으로 메우지 않도록

# temp_table = pd.pivot_table(df, index="밸브상태", columns="운전부하", values="온도", 
#                             aggfunc="mean", margins=True, margins_name="전체")
# # - index: 결과표의 행을 나누는 기준
# # - columns: 결과표의 열을 나누는 기준
# # - values: 각 칸에서 계산할 측정값
# # - aggfunc: 그 측정값으로 요약
# # - margins=True: 전체 집계 행.열 추가
# # - margins_name: 추가 집계 이름 표시

# print(temp_table.round(2))


num = 2
print("=" *3,f"실습 {num}","=" *3)
# marked = df.copy()
# marked["그룹평균"] = marked.groupby("냉각기상태")["온도"].transform("mean")
# marked["편차"] = marked["온도"] - marked["그룹평균"]
# cols = ["냉각기상태", "온도", "그룹평균", "편차"]
# print(marked[cols].head(3).round(2))
# marked["거리"] = marked["편차"].abs()
# furthest = marked.sort_values("거리", ascending=False).head(1)
# print(furthest[cols].round(2))
# #   냉각기상태    온도   그룹평균     편차
# # 0    고장  35.6  54.67 -19.07

# print(marked.groupby("냉각기상태")["편차"].sum().round(10))

# pivot = pd.pivot_table(marked, index="밸브상태", columns="운전부하", values="온도",
#                        aggfunc="mean", margins="True", margins_name="전체")
# print(pivot.round(2))
# print(pivot.shape)

# # corr - 두 지표의 상관계수 구하기
# print(round(df["온도"].corr(df["진동"]), 3))            # 0.931
# print(round(df["온도"].corr(df["냉각효율"]), 3))        # -0.951
# print(round(df["온도"].corr(df["압력"]), 3))            # 0.284


num = 3
print("=" *3,f"실습 {num}","=" *3)
four_col = df[["온도", "진동", "압력", "냉각효율"]]
corr4 = four_col.corr()
print(corr4.round(3))

#       온도     진동     압력   냉각효율
# 온도    1.000  0.931  0.284 -0.951
# 진동    0.931  1.000  0.524 -0.862
# 압력    0.284  0.524  1.000 -0.131
# 냉각효율 -0.951 -0.862 -0.131  1.000

# 표를 읽어 찾은 짝을 원래 값으로 확인
print("가장 강한 짝:", round(corr4.loc["온도", "냉각효율"], 3))
print("가장 약한 짝:", round(corr4.loc["압력", "냉각효율"], 3))

num = 4
print("=" *3,f"실습 {num}","=" *3)
sensor_cols = qc.select_dtypes(include="number").columns.tolist()

# 2. 상관 행렬 계산
corr_matrix = qc[sensor_cols].corr()

# 3. 이중 반복문을 통한 고유 상관쌍 표 생성
rows = []
for i in range(len(sensor_cols)):
    for j in range(i + 1, len(sensor_cols)):
        a = sensor_cols[i]
        b = sensor_cols[j]
        rows.append({
            "지표1": a,
            "지표2": b,
            "상관계수": corr_matrix.loc[a, b]
        })

pair_table = pd.DataFrame(rows)
pair_table["절댓값"] = pair_table["상관계수"].abs()

print(f"상관 행렬 크기: {corr_matrix.shape}, 생성된 상관쌍 개수: {len(pair_table)}")




num = 5
print("=" *3,f"실습 {num}","=" *3)
merged_df = pd.merge(df, spec, on="냉각기상태", how="left")

# 병합 결과 검증 (120행 유지 및 결측 확인)
print(f"병합 후 형태: {merged_df.shape}")  # 기대 결과: (120, 12)
print("결측치 개수:\n", merged_df[["위험도", "점검주기"]].isnull().sum())

# 2. 온도를 구간으로 나누기 (단계 ③)
bins = [0, 40, 50, 200]
labels = ["낮음", "보통", "높음"]
merged_df["온도구간"] = pd.cut(merged_df["온도"], bins=bins, labels=labels, right=False)

# 구간별 건수 확인 (낮음 41, 보통 40, 높음 39 확인용)
print("\n--- 온도 구간별 건수 ---")
print(merged_df["온도구간"].value_counts())

# 3. 상태별 집계 및 진단표 생성 (단계 ④, ⑦)
report = merged_df.groupby("냉각기상태").agg(
    측정수=("온도", "count"),
    평균온도=("온도", "mean"),
    온도표준편차=("온도", "std"),
    평균냉각효율=("냉각효율", "mean"),
    위험도=("위험도", "first"),
    점검주기=("점검주기", "first")
).reset_index()

# 위험도 내림차순, 같으면 평균온도 내림차순 정렬 (단계 ⑦)
report_sorted = report.sort_values(by=["위험도", "평균온도"], ascending=False)