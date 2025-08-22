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
    # 사육 루프: 절망적이고 반복되는 분위기
    $ renpy.music.play(bgm_ending_bad, fadein=1.0, loop=False)
    $ renpy.sound.play(sfx_plate_drop)
    n "으아악! 들켰어...!"
    m "하하. 괜찮아. 넌 그저 놈들의 함정에 굴복했을 뿐이야. 다음에 또 기회가 올 거야. 넌 여기서 안전하니까. 이젠 정말로 괜찮아."
    hide window
    show screen bad_ending_7_text with dissolve
    pause
    hide screen bad_ending_7_text with dissolve
    $ renpy.music.stop(fadeout=1.0)
    jump bad_ending_common

label bad_ending_6:
    # 지워진 기억: 슬프고 공허하며 허무한 분위기
    $ renpy.music.play(bgm_ending_bad, fadein=1.0, loop=False)
    $ renpy.sound.play(sfx_tear)
    "쪽지가 산산조각 났다. 내 기억의 조각들도 함께 사라져갔다."
    n "안 돼... 내 기억이...!"
    m "필요 없어. 그딴 기억의 조각들은. 놈들이 흩어놓은 가짜일 뿐이야. 네게 필요한 건 오직 나뿐이야."
    hide window
    show screen bad_ending_6_text with dissolve
    pause
    hide screen bad_ending_6_text with dissolve
    $ renpy.music.stop(fadeout=1.0)
    jump bad_ending_common

label bad_ending_5_1:
    # 망상 속의 평화: 왜곡되고 느릿하며 기분 나쁜 평온함
    $ renpy.music.play(bgm_ending_bad, fadein=1.0, loop=False)
    $ renpy.sound.play(sfx_monster_voice)
    scene black with Dissolve(0.5)
    n "마음이... 편안해져. 두렵지 않아..."
    m "그래. 이제는... 안심해도 돼. 놈들의 공포는 사라졌어. 우리가 함께니까."
    "괴물의 속삭임이 귓가에 맴돈다. 나는... 더 이상 두려움을 느끼지 않아."
    hide window
    show screen bad_ending_5_1_text with dissolve
    pause
    hide screen bad_ending_5_1_text with dissolve
    $ renpy.music.stop(fadeout=1.0)
    jump bad_ending_common

label bad_ending_5_2:
    # 파괴된 자아: 날카롭고 시끄러우며 부서지는 분위기
    $ renpy.music.play(bgm_ending_bad, fadein=1.0, loop=False)
    $ renpy.sound.play(sfx_crack)
    n "이 지옥을 끝내겠어!"
    m "네가... 놈들의 진실을 부숴버렸어! 이젠 더 이상 놈들의 속임수에 넘어갈 일은 없을 거야...!"
    "거울을 깼다. 내 모습이 끔찍하게 산산조각 났다."
    n "아... 내 모습이...!"
    hide window
    show screen bad_ending_5_2_text with dissolve
    pause
    hide screen bad_ending_5_2_text with dissolve
    $ renpy.music.stop(fadeout=1.0)
    jump bad_ending_common

label bad_ending_4:
    # 문 뒤의 존재: 갑작스럽고 충격적인 공포
    $ renpy.music.play(bgm_ending_bad, fadein=1.0, loop=False)
    $ renpy.sound.play(sfx_screech)
    n "여기 숨겨진 문이 있었어!"
    m "안 돼! 그 문을 열지 마!"
    "숨겨진 문이 열린다. 차가운 손이 내 목을 움켜쥐었다."
    n "으아악! 이게... 이게 너의 진짜 모습이야?"
    m "하하... 어쩔 수 없어. 결국 넌... 이 공포를 끝내지 못했군. 이 모든 건 놈들이 네게 바라는 거야."
    hide window
    show screen bad_ending_4_text with dissolve
    pause
    hide screen bad_ending_4_text with dissolve
    $ renpy.music.stop(fadeout=1.0)
    jump bad_ending_common

label bad_ending_3:
    # 끝나지 않는 추격: 긴박하고 숨 막히는 위협
    $ renpy.music.play(bgm_ending_bad, fadein=1.0, loop=False)
    $ renpy.sound.play(sfx_screech)
    n "달려! 놈이 쫓아와!"
    m "봤지? 내가 숨자고 했잖아! 놈들에게 달아나는 것은 불가능해. 넌 결국... 놈들의 추격에서 벗어날 수 없어."
    "무거운 발소리가 내 등 뒤로 쫓아온다. 결국 나는 붙잡혔다."
    hide window
    show screen bad_ending_3_text with dissolve
    pause
    hide screen bad_ending_3_text with dissolve
    $ renpy.music.stop(fadeout=1.0)
    jump bad_ending_common

label bad_ending_2:
    # 통제 불능: 혼란스럽고 무질서한 분위기
    $ renpy.music.play(bgm_ending_bad, fadein=1.0, loop=False)
    n "화면이... 갑자기 깨지고 있어."
    m "안 돼... 놈들이 시스템을 통제하고 있어... 이 방 자체가 무너지고 있어...!"
    hide window
    show screen bad_ending_2_text with dissolve
    pause
    hide screen bad_ending_2_text with dissolve
    $ renpy.music.stop(fadeout=1.0)
    jump bad_ending_common

label bad_ending_common:
    scene black with fade
    return