# try_except-else-finally
# - else: 예외가 하나도 안 났을 때만 실행
# - finallt: 성공/실패 상관 없이 무조건 마지막 실행

# text = "62.5"
# try:
#     temp = float(text)
# except ValueError:
#     print("변환 실패")
# else:
#     print("변환 성공: ", temp)
# finally:
#     print("종료")

num = 1
print("=" *3,f"실습 {num}","=" *3)
# try:
#     f = open("data/09_ict_indpection.csv", encoding=="utf-8")
#     first = f.readline()
#     print(first.strip())
# except FileNotFoundError:
#     print("파일이 존재하지 않습니다")
# finally:
#     f.close()
# print("파일이 안전하게 닫힘")

num = 2
print("=" *3,f"실습 {num}","=" *3)
try:
    with open("data/09_ict_inspection_dirty.csv", encoding="utf-8") as f:
        rows = f.readlines()[1:]      # 슬라이싱 (헤더 빼려고)
except FileNotFoundError:
    rows = []

total = 0.0
skipped = 0
for line in rows:
    try:
        total += float(line.split(",")[2])      # 측정값(2열)
    except (ValueError, IndexError):
        skipped += 1
        continue

print("합계:", round(total, 1), "/건너뜀:", skipped)


num = 4
print("=" *3,f"실습 {num}","=" *3)
names = [
    "data/09_ict_inspection.csv",
    "data/09_없는파일.csv",  # 중간에 배치
    "data/09_ict_inspection_dirty.csv",
]
done = 0
for name in names:
    # TODO: try에서 with open(name)
    try:
        with open(name, "r", encoding="utf-8") as f:
            # TODO: 데이터 행 수 출력 / done 갱신
            rows = f.readlines()[1:]
        print("읽기 성공:", name, len(rows), "행")
        done += 1
    # TODO: FileNotFoundError 안내, continue
    except FileNotFoundError:
        print("건너뜀:", name)
        continue
print("처리한 파일:", done)

num = 5
print("=" *3,f"실습 {num}","=" *3)
def check_value(text, lo=0.0, hi=5000.0):
    v = float(text)
    # TODO: 범위 밖이면 ValueError 발생
    if not (lo <= v <= hi):
        raise ValueError(f"정상 범위 밖: {v}")
    return v

for t in ["128.5", "결측", "-999"]:
    try:
        print("통과:", check_value(t))
    except ValueError as e:
        print("제외:", e)