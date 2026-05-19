import random

def get_weather_magic():
    weathers = ["맑음", "비", "천둥번개", "안개"]
    current = random.choice(weathers) # 실제 API에서 데이터를 가져오는 과정과 비슷함
    
    print(f"☁️  현재 조선의 기상 상태를 감지 중... [{current}]")
    
    if current == "비" or current == "천둥번개":
        print("⚡️ [도술 성공] 전우치가 기상 시스템을 해킹하여 천지조화를 일으켰습니다!")
    else:
        print("💨 [대기 중] 기상 조건이 맞지 않아 다음 도술을 준비합니다.")

get_weather_magic()