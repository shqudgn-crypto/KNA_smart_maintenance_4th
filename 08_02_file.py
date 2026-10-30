# 파일 입출력
# open()
# 형식: open(파일명, 모드, encoding)
# - 모드: r=읽기, w=새로쓰기, a=이어쓰기
# - encoding ="utf-8" => 한글이 깨지지 않도록 하는 것

FILE = "data/08_press.csv"

f = open(FILE, "r", encoding="utf-8")
text = f.read()
print(text)
f.close()           # 파일을 열고 난 후 닫기까지

# with open - 블록이 끝나면 자동 닫힘
with open(FILE, "r", encoding="utf-8") as f:
    for line in f:
        print(line)

# write()
#with open("data/test.txt", "w", encoding= "utf-8") as f:
#    f.write("쓰기 테스트")

num = 2
print("=" *3,f"실습 {num}","=" *3) # with open 으로 파일에 쓰기
#with open("data/test.txt", "w", encoding= "utf-8") as f:
#    f.write("실습2 테스트")

num = 3
print("=" *3,f"실습 {num}","=" *3) # a 모드로 기록 이어 붙이기
#with open("data/test.txt", "a", encoding= "utf-8") as f:
#    f.write("실습3 테스트\n")
#    f.write("이상 없음 \n")
#with open("data/test.txt", "r", encoding= "utf-8") as f:
#    print(f.read())

import csv
import os
# csv.reader
with open(FILE, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

num = 4
print("=" *3,f"실습 {num}","=" *3) # csv.reader로 CSV 읽기
with open(FILE, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# csv.writer
with open("data/08_summary.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["설비ID", "상태"])     # 헤더
    writer.writerow(["PRESS-01", 1])
    writer.writerow(["PRESS-02", 1])

with open("data/08_summary.csv", "r", encoding="utf-8") as f:
    print(f.read())