## minigame_breath.rpy

screen minigame_breath():
    style_prefix "breath_minigame"

    # 게임 변수 설정
    default breath_gauge = 50.0 # 숨 게이지 (0-100)
    default is_breathing = False # 숨 참는 상태

    # 배경
    add minigame_bg # 미니게임용 공통 배경 이미지
    
    # 숨소리 사운드 시작
    # on "show":
    #     $ renpy.sound.play(sfx_gauge_up, channel="minigame_sfx", loop=True)
        
    # 숨 게이지 바
    bar:
        value breath_gauge
        range 100
        xalign 0.5
        yalign 0.9
        xmaximum 800
        # 게이지 썸네일과 색상 변경
        thumb minigame_gauge_thumb
        thumb_offset 20
        style_group "breath_gauge"
            
    # 게이지를 조절하는 플레이어의 조작
    button:
        xfill True
        yfill True
        action SetScreenVariable("is_breathing", not is_breathing)

    # 게임 타이머 (30초) 및 성공 조건
    timer 30.0 action Return(True) # 30초 내에 성공하면 True 반환

    # 숨 게이지 변화 로직
    # on "show":
    #     $ renpy.restart_interaction()

    python:
        # 마우스 클릭 상태에 따라 게이지 증감
        if is_breathing:
            breath_gauge += renpy.display.get_delta_time() * 3.5 # 숨 참기
        else:
            breath_gauge -= renpy.display.get_delta_time() * 2 # 숨 내쉬기

        # 게이지 값에 따라 스타일의 bar_color를 변경합니다.
        if breath_gauge > 75 or breath_gauge < 25:
            renpy.style.breath_gauge_bar.bar_color = "#ff0000"
        else:
            renpy.style.breath_gauge_bar.bar_color = "#00ff00"

        # 실패 조건 (숨이 너무 차거나 너무 비었을 때)
        if breath_gauge <= 0 or breath_gauge >= 100:
            renpy.sound.stop(channel="minigame_sfx")
            renpy.hide_screen("minigame_breath")
            renpy.jump("minigame_fail")
            
label minigame_fail:
    return False