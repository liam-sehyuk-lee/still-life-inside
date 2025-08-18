screen floor_4_recorder_dialogue:
    frame:
        background "#00000080"
        padding (100, 100)
        xalign 0.5
        yalign 0.5
        
        text """나는 괜찮아... 괜찮다고 했잖아...
문은... 문은 열면 안 돼.
열지 마. 듣고 있지? 제발... 듣고 있어줘...""":
            size 50
            color "#ffffff"

label floor_4:
    # 낡은 의자 위에 녹음기가 놓여있고, 천장 조명이 깜빡인다. 벽에는 전선이 뱀처럼 늘어져 있다.
    scene bg_4f_mental with dissolve
    
    "정적. 아무 소리도 들리지 않는다. 앞선 층들의 소음이 거짓말이었던 것처럼."
    "천장의 조명이 위태롭게 깜빡이며 긴 그림자를 만들고, 벽에는 용도를 알 수 없는 전선들이 뱀처럼 늘어져 있다."

    "여긴 조용하다."
    "너무 조용해서 내 호흡 소리조차 낯설다."
    "하지만... 이 침묵 속엔 뭔가 숨겨져 있어. 비명조차 삼켜버릴 듯한 불길한 침묵."
    
    "의자 위에 녹음기 하나."
    "빨간 불이 깜빡이는 걸 보니, 재생은 가능해 보인다."
    "저 작은 기계 안에... 무엇이 담겨 있을까."
    
    m "틀지 마. 네 목소리가 들릴 거야."

    "어김없이 들려오는 목소리. 나를 비웃고, 유혹하고, 이제는 경고까지 한다."
    "내 목소리라고? 그럴 리가 없어. 하지만... 만약 저것이 사실이라면?"
    "확인해야 할까? 아니면 모른 척해야 할까?"
    
    menu:
        "재생한다 (나는 진실을 듣고 싶다)":
            jump play_recorder_4
        "그냥 지나친다 (이런 건 괜히 건드리는 게 아니야)":
            "그냥 지나치는 게 나을 것 같았다."
            jump floor_3

label play_recorder_4:
    "나는 떨리는 손으로 재생 버튼을 눌렀다. 스피커에서 '치직'거리는 소음이 터져 나왔다."
    "아무것도 들리지 않는 것 같지만, 이 노이즈 너머에 무언가 숨어있다. 집중해서... 진짜 '소리'를 찾아내야 해."

    # 미니게임: 주파수 맞추기
    # $ minigame_result = renpy.call("call_minigame", "frequency")

    # 주파수 맞추기 미니게임 시작 (테스트용 분기)
    $ minigame_result = renpy.random.choice(["success", "fail"])

    if minigame_result == "success":
        "녹음기를 재생하자, 4층 전체를 울리는 목소리가 들려왔다."
        
        hide window
        show screen floor_4_recorder_dialogue with dissolve
        pause
        hide screen floor_4_recorder_dialogue with dissolve
        
        "이 목소리... 나잖아?"
        
        $ renpy.sound.play(sfx_clue_gain)
        $ flag_clue_3 = True
        
        "녹음이 끝나자, 정적과 함께 눈앞의 철문이 천천히 자동으로 열렸다."
        jump floor_3
    else:
        "주파수를 맞추려 할수록 노이즈는 더 커져만 갔다. 결국 스피커에서 '찍'하는 굉음과 함께 연기가 피어올랐다."
        "녹음기는... 망가졌다. 진실을 들을 기회는 사라졌다."
        "잠시 후, 아무 일도 없었다는 듯 철문이 스르륵 열렸다. 이건... 함정인가?"
        jump floor_3