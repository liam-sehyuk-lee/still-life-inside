screen bad_ending_7_text():
    frame:
        background "#00000080"
        xfill True
        yfill True
        text "배드엔딩: 사육 루프":
            size 40
            color "#ffffff"
            xalign 0.5
            yalign 0.5

screen bad_ending_6_text():
    frame:
        background "#00000080"
        xfill True
        yfill True
        text "배드엔딩: 지워진 기억":
            size 40
            color "#ffffff"
            xalign 0.5
            yalign 0.5

screen bad_ending_5_1_text():
    frame:
        background "#00000080"
        xfill True
        yfill True
        text "배드엔딩: 망상 속의 평화":
            size 40
            color "#ffffff"
            xalign 0.5
            yalign 0.5

screen bad_ending_5_2_text():
    frame:
        background "#00000080"
        xfill True
        yfill True
        text "배드엔딩: 파괴된 자아":
            size 40
            color "#ffffff"
            xalign 0.5
            yalign 0.5

screen bad_ending_4_text():
    frame:
        background "#00000080"
        xfill True
        yfill True
        text "배드엔딩: 문 뒤의 존재":
            size 40
            color "#ffffff"
            xalign 0.5
            yalign 0.5

screen bad_ending_3_text():
    frame:
        background "#00000080"
        xfill True
        yfill True
        text "배드엔딩: 끝나지 않는 추격":
            size 40
            color "#ffffff"
            xalign 0.5
            yalign 0.5

screen bad_ending_2_text():
    frame:
        background "#00000080"
        xfill True
        yfill True
        text "배드엔딩: 통제 불능":
            size 40
            color "#ffffff"
            xalign 0.5
            yalign 0.5

label bad_ending_7:
    # 연출: 식판 떨어지는 소리, 괴물 손 등장, 화면 급전환
    # $ renpy.sound.play(sfx_plate_drop)  # 식판 떨어지는 소리 효과음
    # show monster_hand with dissolve(0.1) # 괴물 손 이미지를 빠르게 보여줍니다.
    n "놈의 손이 내 목을 짓눌러온다. 나는... 다시 시작점에 갇혔다."
    hide window
    show screen bad_ending_7_text with dissolve
    pause
    hide screen bad_ending_7_text with dissolve
    jump bad_ending_common

label bad_ending_6:
    # 6층 배드엔딩: 쪽지 찢기
    # $ renpy.sound.play(sfx_tear) # 종이 찢는 소리
    n "쪽지가 산산조각 났다. 내 기억의 조각들도 함께 사라져갔다."
    hide window
    show screen bad_ending_6_text with dissolve
    pause
    hide screen bad_ending_6_text with dissolve
    jump bad_ending_common

label bad_ending_5_1:
    # 5층 배드엔딩 1: 약물 망상
    # $ renpy.sound.play(sfx_monster_voice) # 괴물 목소리 효과음
    scene black with Dissolve(0.5) # 시야 왜곡 및 화면 붕괴 연출
    m "이제는... 안심해도 돼."
    n "괴물의 속삭임이 귓가에 맴돈다. 나는... 더 이상 두려움을 느끼지 않아."
    hide window
    show screen bad_ending_5_1_text with dissolve
    pause
    hide screen bad_ending_5_1_text with dissolve
    jump bad_ending_common

label bad_ending_5_2:
    # 5층 배드엔딩 2: 거울 파괴
    # $ renpy.sound.play(sfx_crack) # 거울 깨지는 소리
    n "거울을 깼다. 내 모습이 끔찍하게 산산조각 났다."
    hide window
    show screen bad_ending_5_2_text with dissolve
    pause
    hide screen bad_ending_5_2_text with dissolve
    jump bad_ending_common

label bad_ending_4:
    # 4층 배드엔딩: 문 뒤의 존재
    # $ renpy.sound.play(sfx_screech) # 괴물 등장 효과음
    n "숨겨진 문이 열린다. 차가운 손이 내 목을 움켜쥐었다."
    hide window
    show screen bad_ending_4_text with dissolve
    pause
    hide screen bad_ending_4_text with dissolve
    jump bad_ending_common

label bad_ending_3:
    # 3층 배드엔딩: 추격 루프
    # $ renpy.sound.play(sfx_screech) # 괴물 등장 효과음
    n "무거운 발소리가 내 등 뒤로 쫓아온다. 결국 나는 붙잡혔다."
    hide window
    show screen bad_ending_3_text with dissolve
    pause
    hide screen bad_ending_3_text with dissolve
    jump bad_ending_common

label bad_ending_2:
    # 2층 배드엔딩: 중간 배드엔딩
    n "갑자기 시스템이 충돌했다."
    n "화면이 깨지고, 괴물의 메시지가 등장한다."
    hide window
    show screen bad_ending_2_text with dissolve
    pause
    hide screen bad_ending_2_text with dissolve
    jump bad_ending_common

label bad_ending_common:
    scene black with fade
    return