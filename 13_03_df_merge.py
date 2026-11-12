import pandas as pd

F_SHOT = 'data/13_diecasting_shot.csv'
F_MASTER = 'data/13_diecasting_master.csv'

log = pd.read_csv(F_SHOT)
master = pd.read_csv(F_MASTER)

# print(log.shape)
# print(master.shape)

# three = log.head(3)[["샷", "설비ID", "비스킷두께"]]
# print(three.to_string(index=False))

# print(three.merge(master, on="설비ID").to_string(index=False))

# # marge 기본 사용법
# # - on: 두 표를 잇는 키 열
# # - 행은 예측불가, 열 수는 예측 가능

# # - how: 어느쪽을 다 남길 것인가
# # - (기본) how='inner'
# # - how = 'left' : 왼쪽은 다 남기고 짝 없으면 빈 칸
# # - how = 'outer' : 양쪽 다 남김

# m_inner = log.merge(master, on= "설비ID")
# m_left = log.merge(master, on= "설비ID", how="left")
# m_outer = log.merge(master, on= "설비ID", how="outer")

# print(m_inner.shape, m_left.shape, m_outer.shape)    # (185, 12) (200, 12) (201, 12)

# num = 1
# print("=" *3,f"실습 {num}","=" *3)
# log = pd.read_csv("data/13_diecasting_shot.csv")
# master = pd.read_csv("data/13_diecasting_master.csv")
# print(log.shape, master.shape)
# merged = log.merge(master, on="설비ID")
# print(merged.shape)
# print(merged[["샷", "설비ID", "라인", "도입연도"]].head(2).to_string(index=False))

# # 합치기 전후 점검 코드

# print(len(log))
# print(len(master), master["설비ID"].nunique())

# m_left = log.merge(master, on="설비ID", how="left")
# print(len(m_left))
# print(int(m_left["라인"].isna().sum()))

# unmatched = m_left[m_left["라인"].isna()]
# print(unmatched["설비ID"].head(1).tolist(), len(unmatched))

num = 2
print("=" *3,f"실습 {num}","=" *3)
m_inner = log.merge(master, on="설비ID")
m_left = log.merge(master, on="설비ID", how="left")
m_outer = log.merge(master, on="설비ID", how="outer")
print(m_inner.shape, m_left.shape, m_outer.shape)

# ② 결측치 및 미매칭 설비 확인
print("left 라인 결측 개수:", m_left["라인"].isna().sum())
print("left 미매칭 설비:", m_left[m_left["라인"].isna()]["설비ID"].unique().tolist())
print("outer 로그 없는 설비:", m_outer[m_outer["샷"].isna()]["설비ID"].tolist())


# merge는 옆으로 칸을 이어 붙이고, concat은 아래로 줄을 쌓는다
# concat은 키 열이 핑요 럾고, 칸 이름만 맞으면 된다

#df.concat

# ex) 설비 로그를 1차,2차로 나눠 받은 경우
part1 = log.iloc[:100].reset_index(drop=True)
part2 = log.iloc[:100].reset_index(drop=True)
print(part1.shape, part2.shape)                 # (100, 8) (100, 8)

stacked =pd.concat([part1,part2])
print(stacked.shape)                    # (200, 8)(200, 8)
print(stacked.index[-3:].tolist())      # [97, 98, 99]
print(len(stacked.loc[[0]]))            # 2

# - 번호를 다시 매기기 -> ignore_index
renumbered = pd.concat([part1, part2], ignore_index=True)
print(int(renumbered.index[-1]))

# - 칸이(열이) 다른 표를 붙이면 -> 빈 칸
# - 붙이기 전에 두 표의 columns 비교
#   -> set(표1.columns) - set(표2.columns)

num = 3
print("=" *3,f"실습 {num}","=" *3)
m_left = log.merge(master, on="설비ID", how="left")
unmatched = m_left[m_left["라인"].isna()]

# ② 품질등급이 양품이 아닌 행 필터링 및 비스킷두께 내림차순 정렬
result = m_left[
    (m_left["라인"].notna()) & (m_left["품질등급"] != "양품")
].sort_values("비스킷두께", ascending=False)

# ③ 결과 출력
print("라인 붙은 줄:", len(m_left))
print("양품 아닌 줄:", len(result))
print(result[["샷", "설비ID", "라인", "비스킷두께", "품질등급"]].head(5).to_string(index=False))

num = 4
print("=" * 3, f"실습 {num}", "=" * 3)

joined = log.merge(master, on="설비ID", how="left")
with_line = joined[joined["라인"].notna()]
print(len(with_line))

not_ok = with_line[with_line["품질등급"] != "양품"]
print(len(not_ok))

result = not_ok.sort_values("비스킷두께", ascending=False)
print(result[["샷", "설비ID", "라인", "비스킷두께", "품질등급"]].head(5).to_string(index=False))