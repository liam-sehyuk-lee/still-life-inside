# minigame_frequency.rpy

init python:
    # --- 미니게임 설정 ---
    FREQUENCY_TIME_LIMIT = 20.0
    FREQUENCY_SUCCESS_RANGE = 0.05
    FREQUENCY_ADJUST_RATE = 0.01 # 마우스 휠 스크롤당 막대가 움직이는 정도
    
    # --- 미니게임 변수 ---
    frequency_gauge = 0.5
    target_frequency = 0.0
    frequency_timer = 0.0
    minigame_over = False
    minigame_result = False
    
    def minigame_frequency_update():
        global frequency_timer, minigame_over, frequency_gauge, target_frequency, minigame_result

        if minigame_over:
            return

        dt = 0.01

        frequency_timer -= dt

        # 승리/패배 조건 확인
        if abs(frequency_gauge - target_frequency) <= FREQUENCY_SUCCESS_RANGE:
            minigame_result = True
            minigame_over = True
        
        elif frequency_timer <= 0:
            minigame_result = False
            minigame_over = True
        
        renpy.restart_interaction()

screen minigame_frequency():
    modal True
    
    on "show":
        action [
            SetVariable("frequency_gauge", renpy.random.uniform(0.1, 0.9)),
            SetVariable("target_frequency", renpy.random.uniform(0.1, 0.9)),
            SetVariable("frequency_timer", FREQUENCY_TIME_LIMIT),
            SetVariable("minigame_over", False),
            SetVariable("minigame_result", False)
        ]

    key "mousedown_4" action SetVariable("frequency_gauge", min(1.0, frequency_gauge + FREQUENCY_ADJUST_RATE))
    key "mousedown_5" action SetVariable("frequency_gauge", max(0.0, frequency_gauge - FREQUENCY_ADJUST_RATE))

    timer 0.01 repeat True action Function(minigame_frequency_update)

    timer 0.01 repeat True:
        if minigame_over:
            action Return(minigame_result)
        
    add "black" alpha 0.7
    vbox:
        align (0.5, 0.5)
        spacing 20

        text "소리가 가장 명확해지는 주파수를 찾아내세요.":
            style "minigame_guide_text"
        text "마우스 휠을 돌려 주파수를 조절하세요.":
            style "minigame_guide_text"

        bar:
            value frequency_gauge
            range 1.0
            xmaximum 800
            ymaximum 30
            left_bar Solid("#00aaff")  
            right_bar Solid("#444444")
            
        text "[max(0, frequency_timer):.1f]":
            align (1.0, 0.5)
            style "minigame_timer_text"