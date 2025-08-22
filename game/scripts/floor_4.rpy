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
    # 4층: 정적이고 불안한 분위기
    $ renpy.music.play(bgm_floor_4_silent, fadein=1.0, loop=True)
    # 낡은 의자 위에 녹음기가 놓여있고, 천장 조명이 깜빡인다. 벽에는 전선이 뱀처럼 늘어져 있다.
    scene bg_4f_mental with dissolve
    
    n "여긴... 너무 조용해. 앞선 층들의 소음이 다 사라졌어."
    m "함정일 거야. 소리 없는 침묵은 더 위험해. 놈들은 우리를 덫으로 유인하고 있어."
    
    "천장의 조명이 위태롭게 깜빡이며 긴 그림자를 만들고, 벽에는 용도를 알 수 없는 전선들이 뱀처럼 늘어져 있다."
    
    n "이 침묵 속엔 뭔가 숨어있어. 비명조차 삼켜버릴 듯한 불길한 침묵."
    
    "의자 위에 놓인, 빨간 불이 깜빡이는 녹음기가 눈에 들어왔다."
    
    n "녹음기야. 이걸 틀면 뭔가를 들을 수 있지 않을까?"
    m "틀지 마. 저건 놈들의 함정일 거야. 저 안에 있는 건... 네 목소리가 들릴 거야."
    n "내 목소리라니? 무슨 소리야?"
    m "놈들의 수법이야. 네가 이곳에 갇히기 전에 녹음한 목소리일 수도 있어. 혼란에 빠뜨리려는 속셈이라고."
    n "하지만... 만약 네 말이 틀리다면? 만약 진실이 담겨 있다면?"
    
    menu:
        "재생한다 (나는 진실을 듣고 싶다)":
            "나는 떨리는 손으로 재생 버튼을 눌렀다. 스피커에서 '치직'거리는 소음이 터져 나왔다."
            jump play_recorder_4
        "그냥 지나친다 (이런 건 괜히 건드리는 게 아니야)":
            n "네 말이 맞는 것 같아. 괜히 위험을 자초할 필요는 없지."
            m "그래... 좋은 판단이야."
            jump floor_3
            
label play_recorder_4:
    # 미니게임: 주파수 맞추기
    call screen minigame_frequency

    if _return:
        "녹음기를 재생하자, 4층 전체를 울리는 목소리가 들려왔다."
        
        hide window
        show screen floor_4_recorder_dialogue with dissolve
        pause
        hide screen floor_4_recorder_dialogue with dissolve
        
        n "이 목소리는... 내 목소리잖아! 이게 어떻게...!"
        m "아니야! 아냐! 그건 네 목소리가 아니야! 놈들이 조작한 거라고! 가짜야! 다 가짜야!"
        n "아냐... 이건 내 목소리가 맞아! 녹음기 속 목소리가... 나에게 '문은 열면 안 돼'라고 말하고 있어!"
        m "이 모든 건 거짓이야! 놈들이... 놈들이 우리를 갈라놓으려 하고 있어! 믿지 마! 제발 나를 믿어줘! 우리가 함께 만들어온 이 시간마저... 거짓이라고 생각하는 거야?"
        
        $ renpy.sound.play(sfx_clue_gain)
        $ flag_clue_3 = True
        jump floor_3
    else:
        "녹음기는 계속해서 불길한 노이즈만 토해낼 뿐이었다."
        n "아무것도... 들리지 않아. 역시 아무것도 없었던 걸까."
        m "그래. 놈들은 아무것도 남겨두지 않았어. 이 모든 게 허상이야. 빨리 이곳을 벗어나자."
        jump bad_ending_4