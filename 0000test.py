import pydirectinput
import pyautogui

# 입력 간 내부 딜레이를 완전히 제거
pyautogui.PAUSE = 0.0
pydirectinput.PAUSE = 0.0

# 안전 장치: 마우스를 모서리로 가져가면 즉시 종료
pyautogui.FAILSAFE = True

print("5초 뒤 극한의 최대 속도 자동 클릭이 시작됩니다.")
print("종료하려면 마우스를 화면 모서리(가장자리)로 빠르게 이동시키세요.")
import time
time.sleep(5)

print("최대 속도 클릭 실행 중...")

try:
    while True:
        # sleep을 아예 쓰지 않고 연속으로 입력 전달
        pydirectinput.click()
        
except pyautogui.FailSafeException:
    print("\n마우스가 모서리로 감지되어 자동 클릭이 안전하게 중단되었습니다.")