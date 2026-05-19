import threading
import time

def spell(id):
    print(f"🌀 [도술] 분신 {id}호 소환! 시스템 교란 중...")
    time.sleep(1) # 1초 동안 작업 수행
    print(f"✨ [성공] 분신 {id}호 임무 완료 후 귀환.")

print("--- 전우치의 분신술 시동 ---")
# 5개의 분신(Thread)을 동시에 생성해서 실행
for i in range(1, 6):
    threading.Thread(target=spell, args=(i,)).start()
    