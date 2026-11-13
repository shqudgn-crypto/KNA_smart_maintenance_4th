import time
import keyboard
import pydirectinput

# ==================== [사용자 설정 영역] ====================
# 시작할 때의 클릭 간격 (초 단위)
# 예: 0.2초 = 1초에 약 5번 클릭 (안전한 속도)
click_interval = 0.2
CLICK_HOLD_TIME = 0.05  # 마우스를 누르고 있는 시간

HOTKEY_STOP = "esc"  # 긴급 정지 키
HOTKEY_FASTER = "="  # 속도 빠르게 (= 키)
HOTKEY_SLOWER = "-"  # 속도 느리게 (- 키)
# ==========================================================

pydirectinput.PAUSE = 0.01

print("=" * 50)
print("속도 조절형 안전 오토클리커 준비 완료")
print(f" - 중지: [{HOTKEY_STOP.upper()}] 키")
print(f" - 빠르게: [{HOTKEY_FASTER}] 키 (간격 0.05초씩 단축)")
print(f" - 느리게: [{HOTKEY_SLOWER}] 키 (간격 0.05초씩 연장)")
print("=" * 50)
print("게임 창을 클릭해 활성화하세요. 3초 뒤 시작합니다:")

for i in range(3, 0, -1):
  print(f"{i}...")
  time.sleep(1)

print(f"\n오토클릭 시작! (현재 클릭 간격: {click_interval}초)")

click_count = 0

try:
  while True:
    # 1. 긴급 정지 확인
    if keyboard.is_pressed(HOTKEY_STOP):
      print(f"\n[긴급 정지] 총 {click_count}회 클릭 후 중단되었습니다.")
      break

    # 2. 속도 빠르게 조절 (= 키)
    if keyboard.is_pressed(HOTKEY_FASTER):
      click_interval = max(0.05, click_interval - 0.05)  # 최소 0.05초 제한
      print(f"[속도 변경] 현재 클릭 간격: {click_interval:.2f}초 (빨라짐)")
      time.sleep(0.3)  # 키 중복 입력 방지 딜레이

    # 3. 속도 느리게 조절 (- 키)
    if keyboard.is_pressed(HOTKEY_SLOWER):
      click_interval = click_interval + 0.05
      print(f"[속도 변경] 현재 클릭 간격: {click_interval:.2f}초 (느려짐)")
      time.sleep(0.3)  # 키 중복 입력 방지 딜레이

    # 4. 클릭 수행
    pydirectinput.mouseDown()
    time.sleep(CLICK_HOLD_TIME)
    pydirectinput.mouseUp()

    click_count += 1

    # 5. 설정된 속도만큼 대기
    time.sleep(click_interval)

except Exception as e:
  print(f"\n오류 발생: {e}")