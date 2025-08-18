## minigame_gaze.rpy

screen minigame_gaze():
    style_prefix "minigame_gaze"

    # 게임 변수 설정
    default gaze_x = 0.5
    default gaze_y = 0.5
    default gaze_size = 0.1 # 시선의 크기
    default gaze_speed = 0.005 # 시선의 이동 속도

    # 배경 이미지
    add minigame_bg
    
    # 5초 간의 준비 타이머
    timer 5.0 action Function(renpy.jump, "start_gaze_game")
    
    # 거울 속 시선 (플레이어가 클릭하면 안 되는 영역)
    imagebutton:
        xalign gaze_x
        yalign gaze_y
        focus_mask True
        idle "gui/gaze.png" # 시선 이미지
        hover "gui/gaze_hover.png" # 마우스 오버 시 이미지
        action [Return(False)] # 시선을 클릭하면 실패하고 False 반환

    # 게임 타이머 (30초)
    timer 30.0 action Return(True) # 30초 동안 버티면 성공하고 True 반환

    # 시선 움직이는 로직
    # on "show":
    #     $ renpy.restart_interaction()
    
    python:
        import renpy.random as random

        # 시선의 위치를 랜덤으로 업데이트
        gaze_x += random.uniform(-gaze_speed, gaze_speed)
        gaze_y += random.uniform(-gaze_speed, gaze_speed)

        # 화면 밖으로 나가지 않도록 범위 제한
        gaze_x = max(0.1, min(0.9, gaze_x))
        gaze_y = max(0.1, min(0.9, gaze_y))
        
label start_gaze_game:
    return