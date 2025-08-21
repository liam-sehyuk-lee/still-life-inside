## minigame_frequency.rpy

screen minigame_frequency():
    style_prefix "minigame_frequency"
    
    # 게임 변수 설정
    default frequency_value = 0.0
    default target_frequency = 0.75 # 목표 주파수 값 (0.0 ~ 1.0)
    default tolerance = 0.05 # 성공 범위 (타겟 값의 +- 0.05)

    # 배경 이미지
    add bg_minigame
    
    # 주파수 슬라이더
    vbar:
        value Preference("frequency", frequency_value)
        xalign 0.5
        yalign 0.5
        ysize 600
        thumb "gui/vbar/vthumb.png"
        
    # 게임 타이머 (30초)
    timer 30.0 action Return(False) # 30초 내에 성공하지 못하면 실패

    # 게임 사운드 로직
    # on "show":
    #     $ renpy.sound.play(sfx_radio_static, channel="frequency", loop=True)
    
    python:
        # 슬라이더 값에 따라 사운드 볼륨을 조절
        freq_diff = abs(frequency_value - target_frequency)
        if freq_diff <= tolerance:
            # 성공 범위에 도달했을 때
            renpy.sound.set_volume(1.0, channel="voice_recorder")
            renpy.sound.set_volume(0.0, channel="frequency")
            renpy.hide_screen("minigame_frequency")
            renpy.jump("minigame_success_frequency")
        else:
            # 성공 범위 밖일 때, 노이즈 볼륨 조절
            volume = min(1.0, freq_diff * 5)
            renpy.sound.set_volume(volume, channel="frequency")
            
# 숨겨진 음성 기록 사운드 (미니게임 시작 시 미리 로드)
# init:
    # $ renpy.sound.play(sfx_voice_recorder, channel="voice_recorder", loop=True)
    # $ renpy.sound.set_volume(0.0, channel="voice_recorder")
        
label minigame_success_frequency:
    return True