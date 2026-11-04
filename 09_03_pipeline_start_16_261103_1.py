"""ICT 검사 CSV 처리 파이프라인 — 교육생 실습 시작 코드.

1단계부터 6단계까지 완성할 때마다 RUN_TO_STEP을 하나씩 올리세요.
PPT의 실습 1~6과 함수가 대응합니다. 추가 패키지는 필요하지 않습니다.
"""
import csv
from pathlib import Path

BASE = Path(__file__).resolve().parent
DATA_PATH = BASE / "data" / "09_ict_inspection_dirty.csv"
REPORT_PATH = BASE / "09_report.txt"
RUN_TO_STEP = 1  # 실습 1 완성 후 2, ... 6으로 변경

def read_csv_data(path):
    """[실습 1] (헤더 리스트, 데이터 행 리스트) 반환. 파일이 없으면 ([], [])."""
    # TODO: try / with open / csv.reader / next / list 사용
    # 파일이 없으면 FileNotFoundError를 처리하세요.
    try:
        with open(path, encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)
            rows = list(reader)
        return header, rows
    except FileNotFoundError:
        print("파일 없음:", path)
        return [], []

def group_by_part(rows):
    """[실습 2] ({부품명: [행, ...]}, 부품명 빈 행의 수) 반환."""
    # TODO: row[1]을 확인하고 부품별 딕셔너리에 묶기
    # 부품명이 빈 행과 열이 부족한 행에 대비하세요.
    # print(rows)
    by_part = {}    # 빈 딕셔너리 생성 (부품별 데이터 담을 공간)
    dropped = 0
    for row in rows:
        try:
            p = row[1]      # 부품명 가져오기
        except IndexError:
            dropped += 1
            continue
        
        if p not in by_part:        # 기존에 해당 부품명이 딕셔너리에 없을 경우
            by_part[p] = []
        
        by_part[p].append(row)      # 기존에 값이 있을 경우 값 추가
        # by_part.setdefault(p, []).append(row)
    # print(by_part)
    return by_part, dropped

def calc_stats(rows, column=2):
    """[실습 3] {'count', 'mean', 'max', 'min'} 딕셔너리 또는 None 반환."""
    # TODO: float(row[column])로 숫자를 모으고 변환 실패/짧은 줄은 제외
    # 숫자가 없다면 None을 반환하세요.
    values = []
    for row in rows:
        try:
            values.append(float(row[column]))
        except (ValueError, IndexError):
            continue
    
    if not values:
        return None
    return {
        "count": len(values),
        "mean": round(sum(values) / len(values), 2),
        "max": max(values),
        "min": min(values)
    }

def filter_valid_rows(rows, lo=0.0, hi=5000.0):
    """[실습 4] (유효 행 리스트, [(CSV 줄 번호, 검사ID, 사유), ...]) 반환."""
    # TODO: 0~5000 범위 검증, -999는 직접 raise ValueError
    # float 변환 오류와 IndexError를 처리하고 줄 번호/사유를 남기세요.
    # enumerate(rows, start=2)로 헤더 다음 줄부터 세어보세요.
    valid = []
    rejected = []
    for row in rows:
        try:
            v = float(row[2])
            if v < lo or v > hi:
                raise ValueError("범위 밖")
            valid.append(row)
        except (ValueError, IndexError) as e:
            rejected.append((row[0], str(e)))
            continue
    return valid, rejected


def save_report(path, total_rows, valid_rows, rejected, stats):
    """[실습 5] 리포트 텍스트 파일 저장."""
    # TODO: 전체/유효/제외 건수, 측정값 평균/최대/최소를 lines에 모으고
    # with open(path, 'w', encoding='utf-8')로 저장하세요.
    # 원본에 측정값의 물리 단위가 없으므로 임의로 '도'를 붙이지 마세요.
    lines = ["=== 리포트 ===",
            f"전체 {total_rows}건 / 유효 {len(valid_rows)}건 / 제외 {len(rejected)}건",
            f"측정값 평균 {stats['mean']} · 최고 {stats['max']} · 최저 {stats['min']}"]
    with open(path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
        
    


def verify_part_counts(valid_rows):
    """[실습 6] 유효 행을 부품별로 다시 묶고 합계가 전체와 같은지 확인."""
    # TODO: group_by_part(valid_rows)를 재사용하고
    # 각 부품에 calc_stats(part_rows, 2)를 적용해 건수를 합산하세요.
    by_valid, _ = group_by_part(valid_rows)     # 정상 데이터 15건 -> 부품명별로 분류 / _: 부품명 누락 건수를 사용X
    
    check_sum = 0
    
    for v in sorted(by_valid):
        check_sum += calc_stats(by_valid[v], 2)["count"]
    print(check_sum == len(valid_rows))



def main():
    header, rows = read_csv_data(DATA_PATH)
    print(f"[1단계] 헤더 {len(header)}개 / 데이터 {len(rows)}행")
    if RUN_TO_STEP == 1:
        return

    by_part, dropped = group_by_part(rows)
    print(f"[2단계] 부품 {len(by_part)}종 / 부품명 누락 {dropped}행")
    if RUN_TO_STEP == 2:
        return

    before = calc_stats(rows, 2)
    print(f"[3단계] 범위 검증 전 통계: {before}")
    if RUN_TO_STEP == 3:
        return

    valid, rejected = filter_valid_rows(rows)
    after = calc_stats(valid, 2)
    print(f"[4단계] 유효 {len(valid)}건 / 제외 {len(rejected)}건")
    for item in rejected:
        print("    제외:", item)
    if RUN_TO_STEP == 4:
        return

    save_report(REPORT_PATH, len(rows), valid, rejected, after)
    print(f"[5단계] 리포트 생성: {REPORT_PATH.name}")
    if RUN_TO_STEP == 5:
        return

    verify_part_counts(valid)


if __name__ == "__main__":
    main()
