init python:
    BREATH_SURVIVAL_TIME = 10.0
    BREATH_DECREASE_RATE = 25
    BREATH_INCREASE_RATE = 20
    breath_gauge = 0.0
    breath_timer = 0.0
    mouse_is_down = False

screen minigame_breath():
    modal True
    
    on "show":
        action SetVariable("breath_gauge", 40.0), SetVariable("breath_timer", 0.0), SetVariable("mouse_is_down", False)

    key "mousedown_1" action SetVariable("mouse_is_down", True)
    key "mouseup_1" action SetVariable("mouse_is_down", False)

    # 하나의 타이머가 모든 로직을 처리하도록 단순화
    timer 0.01 repeat True action [
        SetVariable("breath_timer", breath_timer + 0.01),
        If(mouse_is_down,
            SetVariable("breath_gauge", max(0, breath_gauge - (BREATH_DECREASE_RATE * 0.01))),
            SetVariable("breath_gauge", min(100, breath_gauge + (BREATH_INCREASE_RATE * 0.01)))
        )
    ]

    # 승리/패배 조건 확인
    if breath_timer >= BREATH_SURVIVAL_TIME:
        timer 0.01 action Return(True)
    elif breath_gauge >= 100:
        timer 0.01 action Return(False)

    # --- UI 부분 ---
    add "black" alpha 0.7
    vbox:
        align (0.5, 0.5)
        spacing 20
        text "문 너머의 존재가 사라질 때까지...":
            style "minigame_guide_text"
        text "마우스를 클릭해서 숨을 참으세요.":
            style "minigame_guide_text"
        bar:
            value breath_gauge
            range 100
            xmaximum 800
            ymaximum 30
            left_bar Solid("#cc0000")
            right_bar Solid("#555555")
        text "[max(0, BREATH_SURVIVAL_TIME - breath_timer):.1f]":
            align (1.0, 0.5)
            style "minigame_timer_text"