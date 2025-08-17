label floor_4:
    scene bg_4f_mental with dissolve
    
    n "여긴 조용하다."
    n "너무 조용해서 내 호흡 소리조차 낯설다."
    n "하지만... 이 침묵 속엔 뭔가 숨겨져 있어."
    n "의자 위에 녹음기 하나."
    n "빨간 불이 깜빡이는 걸 보니, 재생은 가능해 보인다."
    n "재생해도 될까?"
    n "아니면 그냥... 지나쳐야 할까?"
    
    m "틀지 마. 네 목소리가 들릴 거야."
    
    menu:
        "재생한다 (나는 진실을 듣고 싶다)":
            jump play_recorder
        "그냥 지나친다 (이런 건 괜히 건드리는 게 아니야)":
            jump pass_by

label play_recorder:
    # $ renpy.sound.play(sfx_voice_recorder)
    "나는 괜찮아... 괜찮다고 했잖아..."
    "문은... 문은 열면 안 돼."
    "열지 마. 듣고 있지? 제발... 듣고 있어줘..."
    
    n "이 목소리... 나잖아?"
    n "언제, 어디서... 이걸 녹음했지?"
    
    $ renpy.sound.play(sfx_clue_gain)
    $ flag_clue_3 = True
    
    menu:
        "문을 연다 (밖에 뭐가 있든... 상관없어)":
            jump bad_ending_4
        "조용히 기다린다 (나는... 아직 그걸 볼 준비가 안 됐어)":
            jump wait_quietly_4

label pass_by:
    n "그냥 지나치는 게 나을 것 같았다."
    jump floor_3

label wait_quietly_4:
    n "발자국 소리가 점점 멀어진다."
    n "문이 자동으로 열렸다."
    jump floor_3