## minigame_heartbeat.rpy

screen minigame_heartbeat():
    style_prefix "minigame_heartbeat"

    # 게임 변수 설정
    default heartbeat_gauge = 25.0 # 심장박동 게이지 (0-100)
    default is_calming = False # 심장박동을 진정시키는 상태

    # 배경
    add bg_minigame
    
    # 심장박동 사운드 시작
    # on "show":
    #     $ renpy.sound.play(sfx_heartbeat, channel="minigame_sfx", loop=True)
        
    # 심장박동 게이지 바
    bar:
        value heartbeat_gauge
        range 100
        xalign 0.5
        yalign 0.9
        xmaximum 800
        thumb minigame_gauge_thumb
        thumb_offset 20
        style_group "heartbeat_gauge"
            
    # 게이지를 조절하는 플레이어의 조작
    button:
        xfill True
        yfill True
        action SetScreenVariable("is_calming", not is_calming)

    # 게임 타이머 (20초) 및 성공 조건
    timer 20.0 action Return(True) # 20초 동안 버티면 성공하고 True 반환

    # 심장박동 변화 로직
    # on "show":
    #     $ renpy.restart_interaction()

    python:
        # 괴물이 지나가며 심장박동 게이지 증가
        heartbeat_gauge += renpy.display.get_delta_time() * 2

        # 마우스 클릭 상태에 따라 심장박동 조절
        if is_calming:
            heartbeat_gauge -= renpy.display.get_delta_time() * 3 # 진정시키기

        # 게이지 값에 따라 스타일의 bar_color를 변경합니다.
        if heartbeat_gauge > 80:
            renpy.style.heartbeat_gauge_bar.bar_color = "#ff0000"
        else:
            renpy.style.heartbeat_gauge_bar.bar_color = "#00ff00"

        # 실패 조건 (심장박동이 너무 빨라지거나 너무 느려졌을 때)
        if heartbeat_gauge >= 100 or heartbeat_gauge <= 0:
            renpy.sound.stop(channel="minigame_sfx")
            renpy.hide_screen("minigame_heartbeat")
            renpy.jump("minigame_fail_heartbeat")

label minigame_fail_heartbeat:
    return False