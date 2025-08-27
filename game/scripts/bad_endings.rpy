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
    $ renpy.music.play(bgm_ending_bad, fadein=1.0, loop=True)
    # 식판이 떨어지는 소리
    $ renpy.sound.play(sfx_plate_drop, loop=False)
    n "으아악! 들켰어...!"
    "놈의 발소리가 멈춘다. 나는 숨을 헐떡이며 몸을 웅크렸다. 모든 것이 끝났다고 생각했지만, 놈은 그저 식판을 문 아래로 밀어 넣을 뿐이었다."
    m "하하... 괜찮아. 넌 그저 놈들의 함정에 굴복했을 뿐이야. 다음에 또 기회가 올 거야. 넌 여기서 안전하니까. 이젠 정말로 괜찮아. 이 반복되는 고통이... 너를 완성할 거야."
    hide window
    show screen bad_ending_7_text with dissolve
    pause
    hide screen bad_ending_7_text with dissolve
    $ renpy.music.stop(fadeout=1.0)
    jump bad_ending_common

label bad_ending_6:
    # 지워진 기억: 슬프고 공허하며 허무한 분위기
    $ renpy.music.play(bgm_ending_bad, fadein=1.0, loop=True)
    # 쪽지 찢는 소리
    $ renpy.sound.play(sfx_tear, loop=False)
    "쪽지가 산산조각 났다. 내 기억의 조각들도 함께 사라져갔다."
    n "안 돼... 내 기억이...!"
    m "필요 없어. 그딴 기억의 조각들은. 놈들이 흩어놓은 가짜일 뿐이야. 네게 필요한 건 오직 나뿐이야. 네가 나를 잃는다면... 넌 모든 것을 잃는 거야. 그러니... 나를 믿어."
    hide window
    show screen bad_ending_6_text with dissolve
    pause
    hide screen bad_ending_6_text with dissolve
    $ renpy.music.stop(fadeout=1.0)
    jump bad_ending_common

label bad_ending_5_1:
    # 망상 속의 평화: 왜곡되고 느릿하며 기분 나쁜 평온함
    $ renpy.music.play(bgm_ending_bad, fadein=1.0, loop=True)
    # 괴물의 속삭임
    $ renpy.sound.play(sfx_monster_voice, loop=False)
    scene black with Dissolve(0.5)
    "온몸의 감각이 사라진다. 머릿속의 모든 소음이 멎고, 고통도 사라진다. 나는 약병을 쥐고 허공을 응시했다."
    n "마음이... 편안해져. 더는... 두렵지 않아."
    m "그래. 이제 아무도 널 해치지 못해. 이 방에 영원히... 우리만 있을 테니까. 진실도, 고통도, 공포도... 모두 사라졌어. 네가 원했던 평화가 바로 이것이야."
    "괴물의 속삭임이 귓가에 맴돈다. 나는... 더 이상 두려움을 느끼지 않아. 나는 이 망상 속에서 영원히 잠들었다."
    hide window
    show screen bad_ending_5_1_text with dissolve
    pause
    hide screen bad_ending_5_1_text with dissolve
    $ renpy.music.stop(fadeout=1.0)
    jump bad_ending_common

label bad_ending_5_2:
    # 파괴된 자아: 날카롭고 시끄러우며 부서지는 분위기
    $ renpy.music.play(bgm_ending_bad, fadein=1.0, loop=True)
    # 거울이 깨지는 소리
    $ renpy.sound.play(sfx_crack, loop=False)
    n "이 지옥을 끝내겠어!"
    "거울이 산산조각 났다. 그 조각들 속에서 비틀어진 내 모습이 수없이 흩어졌다. 산산조각 난 것은 거울이 아니었다. 내가 마주해야 했던 현실의 나 자신이었다."
    m "네가... 놈들의 진실을 부숴버렸어! 이젠 더 이상 놈들의 속임수에 넘어갈 일은 없을 거야...!"
    n "아... 내 모습이...!"
    "나는 바닥에 주저앉아 거울 조각들에 비친 내 모습을 바라봤다. 비명을 지르고 싶었지만, 소리가 나오지 않았다. 나는... 나 자신을 파괴했다. 그리고 `???`의 목소리만 남았다."
    hide window
    show screen bad_ending_5_2_text with dissolve
    pause
    hide screen bad_ending_5_2_text with dissolve
    $ renpy.music.stop(fadeout=1.0)
    jump bad_ending_common

label bad_ending_4:
    # 문 뒤의 존재: 갑작스럽고 충격적인 공포
    $ renpy.music.play(bgm_ending_bad, fadein=1.0, loop=True)
    # 괴물의 비명 소리
    $ renpy.sound.play(sfx_screech, loop=False)
    n "여기 숨겨진 문이 있었어!"
    m "안 돼! 그 문을 열지 마! 놈들이... 놈들이 이 문을 열게 만들었어!"
    "숨겨진 문이 열린다. 차가운 손이 내 목을 움켜쥐었다. 놈의 눈은 텅 비어 있었고, 그 안에는... 오직 나의 공포만이 비치고 있었다."
    n "으아악! 이게... 이게 너의 진짜 모습이야?"
    m "하하... 어쩔 수 없어. 결국 넌... 이 공포를 끝내지 못했군. 이 모든 건 놈들이 네게 바라는 거야. 내가... 놈들에게 굴복했어. 놈들은... 내가 널 배신하길 원했지. 하하하!"
    hide window
    show screen bad_ending_4_text with dissolve
    pause
    hide screen bad_ending_4_text with dissolve
    $ renpy.music.stop(fadeout=1.0)
    jump bad_ending_common

label bad_ending_3:
    # 끝나지 않는 추격: 긴박하고 숨 막히는 위협
    $ renpy.music.play(bgm_ending_bad, fadein=1.0, loop=True)
    # 괴물의 비명 소리
    $ renpy.sound.play(sfx_screech, loop=False)
    n "달려! 놈이 쫓아와!"
    m "봤지? 내가 숨자고 했잖아! 놈들에게 달아나는 것은 불가능해. 넌 결국... 놈들의 추격에서 벗어날 수 없어. 네가 나를 믿지 않고, 내 말을 듣지 않았기 때문에... 이 모든 것이 끝난 거야."
    "무거운 발소리가 내 등 뒤로 쫓아온다. 축축하고 비릿한 냄새가 내 코를 찔렀다. 결국 나는 붙잡혔다. 그리고 '그것'의 비명이 내 귓가를 찢었다."
    hide window
    show screen bad_ending_3_text with dissolve
    pause
    hide screen bad_ending_3_text with dissolve
    $ renpy.music.stop(fadeout=1.0)
    jump bad_ending_common

label bad_ending_2:
    # 통제 불능: 혼란스럽고 무질서한 분위기
    $ renpy.music.play(bgm_ending_bad, fadein=1.0, loop=True)
    # 방이 무너지는 소리
    $ renpy.sound.play(sfx_crack, loop=False)
    n "화면이... 갑자기 깨지고 있어. 이 방이... 무너지고 있어!"
    m "안 돼... 놈들이 시스템을 통제하고 있어... 이 방 자체가 무너지고 있어...! 놈들이... 놈들이 내 존재를 지우려 해! 내가... 사라져가고 있어!"
    "온몸의 감각이 뒤엉킨다. 모든 것이 무너지고, 나는 혼자 남았다. '???'의 목소리도 더 이상 들리지 않는다. 놈들은... 모든 것을 가져갔다."
    hide window
    show screen bad_ending_2_text with dissolve
    pause
    hide screen bad_ending_2_text with dissolve
    $ renpy.music.stop(fadeout=1.0)
    jump bad_ending_common

label bad_ending_common:
    scene black with fade
    return