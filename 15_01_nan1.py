import pandas as pd

F_PROC = 'data/15_사출성형_공정.csv'
F_LOG = 'data/15_사출성형_로그.csv'


df = pd.read_csv(F_PROC)
log_raw = pd.read_csv(F_LOG)

# 결측 처리
# - 종류: NaN, None, NA, NaT
# ㄴ 표현은 달라도 isna()로 결측 여부 확인 가능

s = pd.Series([10, None, 20])
print(s.mean())                 # 15.0 -> NaN 값이 있다고 해서 계산이 멈춘다X (10+20)/2
print(s + 1)                    # 11.0, NaN, 21.0

num = 1
print("=" *3,f"실습 {num}","=" *3)
print(log_raw.shape)        # (16, 7)
print(log_raw.isna().sum())
# 측정시각     0
# 사출기      1
# 배럴온도     2
# 사출압력     1
# 스크루속도    1
# 누적샷      0
# 불량여부     0
print(int(log_raw["사출압력"].eq(0).sum()))         # 2
print(int(log_raw["스크루속도"].eq(-999).sum()))    # 2
print(int(log_raw["배럴온도"].eq(999).sum()))       # 1