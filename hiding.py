import base64

def hide_spell(message):
    print(f"📖 원본 메시지: {message}")
    # 텍스트를 바이트로 변환 후 Base64로 인코딩 (은신)
    encoded = base64.b64encode(message.encode()).decode()
    print(f"🖼  [도술] 전우치가 그림 속으로 숨었습니다 (인코딩 완료).")
    print(f"🔒 암호화된 상태: {encoded}")
    return encoded

secret = "임금님은 바보, 전우치가 황금을 가져간다!"
hide_spell(secret)