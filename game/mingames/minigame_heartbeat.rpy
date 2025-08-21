# minigame_heartbeat.rpy

init python:
    # --- 미니게임 설정 ---
    HEARTBEAT_TIME_LIMIT = 20.0
    HEARTBEAT_FILL_NORMAL = 5.0  # 평상시 게이지 증가 속도
    HEARTBEAT_FILL_FAST = 15.0   # 위험 시 게이지 증가 속도
    HEARTBEAT_DECAY_RATE = 20.0 # 클릭 시 게이지 감소 속도

    # --- 미니게임 변수 ---
    heartbeat_gauge = 0.0
    heartbeat_timer = 0.0
    mouse_is_down = False
    heartbeat_is_fast = False
    heartbeat_state_timer = 0.0
    heartbeat_next_switch_time = 2.0
    minigame_over = False
    minigame_result = False

    def minigame_heartbeat_update():
        global heartbeat_timer, heartbeat_state_timer, heartbeat_is_fast, heartbeat_next_switch_time, heartbeat_gauge, mouse_is_down, minigame_over, minigame_result

        if minigame_over:
            return

        dt = 0.01

        # 1. 타이머 업데이트
        heartbeat_timer -= dt
        heartbeat_state_timer += dt

        # 2. 심장박동 상태 변경 로직 (빠르게/느리게)
        if heartbeat_state_timer >= heartbeat_next_switch_time:
            if heartbeat_is_fast:
                heartbeat_is_fast = False
                heartbeat_next_switch_time = renpy.random.uniform(2.0, 5.0)
            else:
                heartbeat_is_fast = True
                heartbeat_next_switch_time = renpy.random.uniform(0.5, 1.5)
            heartbeat_state_timer = 0.0

        # 3. 게이지 조절 로직
        if heartbeat_is_fast:
            heartbeat_gauge = min(100, heartbeat_gauge + HEARTBEAT_FILL_FAST * dt)
        else:
            heartbeat_gauge = min(100, heartbeat_gauge + HEARTBEAT_FILL_NORMAL * dt)

        # 마우스를 누르면 게이지 감소
        if mouse_is_down:
            heartbeat_gauge = max(0, heartbeat_gauge - HEARTBEAT_DECAY_RATE * dt)

        # 4. 승리/패배 판정
        # 위험 상태에서 클릭하면 게임 오버
        if heartbeat_is_fast and mouse_is_down:
            minigame_result = False
            minigame_over = True
        # 시간이 끝나면 성공 (버티기)
        elif heartbeat_timer <= 0:
            minigame_result = True
            minigame_over = True
        # 게이지가 100%에 도달하면 실패
        elif heartbeat_gauge >= 100:
            minigame_result = False
            minigame_over = True

        renpy.restart_interaction()

screen minigame_heartbeat():
    modal True

    on "show":
        action [
            SetVariable("heartbeat_gauge", 0.0),
            SetVariable("heartbeat_timer", HEARTBEAT_TIME_LIMIT),
            SetVariable("mouse_is_down", False),
            SetVariable("heartbeat_is_fast", False),
            SetVariable("heartbeat_state_timer", 0.0),
            SetVariable("heartbeat_next_switch_time", renpy.random.uniform(2.0, 5.0)),
            SetVariable("minigame_over", False),
            SetVariable("minigame_result", False)
        ]

    key "mousedown_1" action SetVariable("mouse_is_down", True)
    key "mouseup_1" action SetVariable("mouse_is_down", False)

    timer 0.01 repeat True action Function(minigame_heartbeat_update)

    timer 0.01 repeat True:
        if minigame_over:
            action Return(minigame_result)

    add "black" alpha 0.7
    vbox:
        align (0.5, 0.5)
        spacing 20

        if heartbeat_is_fast:
            text "위험! 숨소리를 죽여야 해!"
            text "마우스를 누르지 마십시오.":
                style "minigame_guide_text"
        else:
            text "심장 박동을 늦춰야 해..."
            text "클릭으로 게이지를 낮추세요.":
                style "minigame_guide_text"

        bar:
            value heartbeat_gauge
            range 100
            xmaximum 800
            ymaximum 30
            left_bar Solid("#ff0000")
            right_bar Solid("#444444")

        text "[max(0, heartbeat_timer):.1f]":
            align (1.0, 0.5)
            style "minigame_timer_text"