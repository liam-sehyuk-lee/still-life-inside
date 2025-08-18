label floor_7:
    # (화면 어두운 방, 금속문 너머 발소리 점점 가까워짐. 숨소리, 시계 초침 소리 섞임)
    scene bg_7f_mental with fade
    $ renpy.sound.play(sfx_footsteps_creeping, loop=False)
    $ renpy.sound.play(sfx_clock_ticking, loop=True)

    m "네가 움직이면, 놈도 반응해. 그러니까... 조용히 기다려야 해."
    "...그런데 오늘은 느낌이 다르다."
    "문 너머의 그림자가 망설인다."
    "식관을 밀어 넣는 속도가 느려졌다."
    "이건 기회일까?"
    "이대로 끝낼 수도 있어."
    "문이 열리는 그 순간, 놈의 목을 잡을 수 있다면..."

    # (문 아래 그림자가 멈춘다. 식판 그림자가 보임)

    menu:
        "조용히 기다린다":
            jump wait_quietly_7
        "문이 열리는 순간을 노린다":
            jump bad_ending_7
            
label wait_quietly_7:
    "문이 천천히 열렸다 닫히고, 식판이 남겨진다."
    "오늘도... 그냥 지나갔다."
    jump floor_6