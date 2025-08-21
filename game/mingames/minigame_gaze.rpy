# minigame_gaze.rpy

init python:
    # --- 미니게임 설정 ---
    GAZE_TIME_LIMIT = 30.0
    GAUGE_FILL_RATE = 20
    GAUGE_DECAY_RATE = 5

    # --- 미니게임 변수 ---
    gaze_gauge = 0.0
    gaze_timer = 0.0
    mouse_is_down = False
    gaze_is_dangerous = False
    gaze_state_timer = 0.0
    gaze_next_switch_time = 2.0
    minigame_over = False
    minigame_result = False

    def minigame_gaze_update():
        global gaze_timer, gaze_state_timer, gaze_is_dangerous, gaze_next_switch_time, gaze_gauge, mouse_is_down, minigame_over, minigame_result

        if minigame_over:
            return

        dt = 0.01

        # 1. 타이머 업데이트
        gaze_timer -= dt
        gaze_state_timer += dt

        # 2. 눈 상태 변경 로직
        if gaze_state_timer >= gaze_next_switch_time:
            if gaze_is_dangerous:
                gaze_is_dangerous = False
                gaze_next_switch_time = renpy.random.uniform(2.0, 5.0)
            else:
                gaze_is_dangerous = True
                gaze_next_switch_time = renpy.random.uniform(0.5, 1.5)
            gaze_state_timer = 0.0

        # 3. 게이지 조절 로직
        if mouse_is_down:
            gaze_gauge = min(100, gaze_gauge + GAUGE_FILL_RATE * dt)
        else:
            gaze_gauge = max(0, gaze_gauge - GAUGE_DECAY_RATE * dt)

        # 4. 승리/패배 판정
        if gaze_gauge >= 100:
            minigame_result = True
            minigame_over = True
        elif gaze_timer <= 0:
            minigame_result = False
            minigame_over = True
        elif gaze_is_dangerous and mouse_is_down:
            minigame_result = False
            minigame_over = True
            
        renpy.restart_interaction()

transform static_eye_100px:
    xalign 0.5
    yalign 0.5
    size (300, 300)

screen minigame_gaze():
    modal True
    
    on "show":
        action [
            SetVariable("gaze_gauge", 0.0),
            SetVariable("gaze_timer", GAZE_TIME_LIMIT),
            SetVariable("mouse_is_down", False),
            SetVariable("gaze_is_dangerous", False),
            SetVariable("gaze_state_timer", 0.0),
            SetVariable("gaze_next_switch_time", renpy.random.uniform(2.0, 5.0)),
            SetVariable("minigame_over", False),
            SetVariable("minigame_result", False)
        ]

    key "mousedown_1" action SetVariable("mouse_is_down", True)
    key "mouseup_1" action SetVariable("mouse_is_down", False)

    # 게임 로직을 업데이트하는 타이머
    timer 0.01 repeat True action Function(minigame_gaze_update)

    # 게임 종료 상태를 감지하고 스크린을 종료하는 타이머
    timer 0.01 repeat True:
        if minigame_over:
            action Return(minigame_result)
        
    # --- UI 부분 (변경 없음) ---
    add "black" alpha 0.7
    vbox:
        align (0.5, 0.5)
        spacing 20
        if gaze_is_dangerous:
            add gui.gaze_bright at static_eye_100px
        else:
            add gui.gaze_normal at static_eye_100px
        text "눈이 잠잠할 때 게이지를 끝까지 채우세요.":
            style "minigame_guide_text"
        text "마우스를 클릭하면 게이지가 차오릅니다.":
            style "minigame_guide_text"
        bar:
            value gaze_gauge
            range 100
            xmaximum 800
            ymaximum 30
            left_bar Solid("#00aaff")  
            right_bar Solid("#444444")
        text "Time Left: [max(0, gaze_timer):.1f]s":
            align (1.0, 0.5)
            style "minigame_timer_text"