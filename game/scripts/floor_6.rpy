screen floor_6_note_front_screen:
    frame:
        background "#00000080"
        padding (100, 100)
        xalign 0.5
        yalign 0.5
        
        text "그들은 소리를 듣는다. 조용히 움직여라.":
            size 50
            color "#ffffff"

screen floor_6_note_back_screen:
    frame:
        background "#00000080"
        padding (100, 100)
        xalign 0.5
        yalign 0.5
        
        text "나는 이 문을 열었다. 그리고 사라졌다.":
            size 50
            color "#ffffff"

label floor_6:
    # 6층: 기괴하고 혼란스러운 분위기
    $ renpy.music.play(bgm_floor_6_creepy, fadein=1.0, loop=True)
    # 붉은 조명이 비추는 방.
    scene bg_6f_mental with dissolve
    
    "이전 층과는 다른, 끈적하고 비릿한 공기가 폐부를 찌른다. 벽은 온통 붉은 조명에 젖어 있고..."
    "마치 누군가 피 묻은 손으로 긁어낸 듯한 글씨들이 가득하다."
    n "이거... 뭐야. 벽에 글씨가 가득해."
    m "다른 생존자들이 남긴 경고야. 저 문장들... 모두 익숙하지 않아?"
    n "맞아... 인터넷 게시판에서 봤던 글 같아. '놈들은 소리를 듣는다', '약을 믿지 마', '여기서 나가야 해'..."
    m "그래, 우리가 항상 보던 그 글이야. 이건 틀림없어. 저건 우리가 쓴 거야."
    n "우리가 썼다고? 우리가 직접...?"
    "기억 속 어딘가에서 본 듯한 문장들. 이건 내가 본 것이 아니라... 내가 쓴 것 같다."
    "그때, 바닥에 떨어진 종이 한 장이 눈에 들어왔다."

    # (바닥의 쪽지를 줍는다. 앞면 자동 노출)
    hide window
    show screen floor_6_note_front_screen with dissolve
    pause
    hide screen floor_6_note_front_screen with dissolve
    
    n "낯설지 않아. 이 문장도... 이 종이의 질감도... 모두 어디선가 느껴본 것 같아."
    m "만지지 마! 그건 함정이야! 놈들이 네게 보여주려는 거짓말이라고! 제발... 내 말을 들어."
    "이 쪽지... 정말, 끝까지 봐도 괜찮은 걸까? 이 얇은 종이 너머에 감당할 수 없는 진실이 숨어있을 것만 같다."
    menu:
        "뒷면까지 본다 (불길한 예감이 든다)":
            n "아니. 이대로는 안 돼. 나는 진실을 봐야 해!"
            m "안 돼! 놈들은 네가 진실을 보길 원해! 함정에 빠지는 거라고! 제발, 멈춰!"
            jump check_back_side_6
        "그냥 덮는다 (확신이 서지 않는다)":
            n "괜히 건드리면 안 될 것 같아. 너무 불길해."
            m "그래... 네 판단이 옳을 거야. 때로는 진실을 덮어두는 것이 더 안전한 법이야."
            jump floor_5
        "찢어버린다 (위험해 보인다)":
            n "아니. 이건 위험해. 차라리 없애버리는 게 낫겠어."
            m "그래. 좋아. 놈들이 우리를 혼란에 빠뜨리기 위해 놓은 함정일 뿐이야. 모든 가짜 단서들을 없애버리고, 오직 우리 둘의 힘으로 나아가야 해."
            jump bad_ending_6

label check_back_side_6:
    "떨리는 손으로 쪽지를 뒤집었다. 하지만 그 순간, 글자들이 눈앞에서 조각나 흩어지는 것 같았다."
    "머리가 깨질 듯 아프다. 이 문장을... 내가 직접 완성해야만 해."
    # 미니게임: 찢어진 쪽지 맞추기
    call screen minigame_note

    if _return:
        hide window
        show screen floor_6_note_back_screen with dissolve
        pause
        hide screen floor_6_note_back_screen with dissolve
        
        n "이건... 내 글씨잖아?"
        m "말도 안 돼! 분명 다른 누군가 썼어! 놈들이 우리 기억을 조작하는 거야! 속으면 안 돼!"
        n "이 쪽지는 내가... 내가 쓴 거야. 왜지?"
        m "제발 믿지 마! 놈들의 함정이야! 우린 같이 탈출해야 해!"
        # 단서 획득 소리
        $ renpy.sound.play(sfx_clue_gain, loop=False)
        $ flag_clue_1 = True
        jump floor_5
    else:
        # 깨지는 소리
        $ renpy.sound.play(sfx_crack, loop=False)
        "머릿속에서 무언가 '툭'하고 끊어졌다. 쪽지의 글자도, 내 기억의 조각들도... 산산이 흩어져 사라져간다."
        m "젠장... 실패야. 중요한 단서를 놓쳤어."
        n "아...아니야... 내 기억...!"
        jump bad_ending_6