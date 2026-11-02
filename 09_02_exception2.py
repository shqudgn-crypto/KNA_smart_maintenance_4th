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