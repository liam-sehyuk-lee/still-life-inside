# 7층 스크립트의 시작 라벨
label floor_7:
    scene bg_7f_mental with fade

    # 배경음악 및 효과음 재생
    # $ renpy.sound.play(sfx_footsteps_creeping, loop=False)
    # $ renpy.sound.play(sfx_clock_ticking, loop=True)

    n "네가 움직이면, 놈도 반응해. 그러니까... 조용히 기다려야 해."
    n "...그런데 오늘은 느낌이 다르다."
    n "문 너머의 그림자가 망설인다."
    n "식관을 밀어 넣는 속도가 느려졌다."
    n "이건 기회일까?"
    n "이대로 끝낼 수도 있어."
    n "문이 열리는 그 순간, 놈의 목을 잡을 수 있다면..."

    menu:
        "조용히 기다린다":
            jump wait_quietly_7
        "문이 열리는 순간을 노린다":
            jump bad_ending_7
            
label wait_quietly_7:
    n "문이 천천히 열렸다 닫히고, 식판이 남겨진다."
    n "오늘도... 그냥 지나갔다."
    jump floor_6