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
    # (붉은 조명. 벽 가득 낙서. 쪽지가 바닥에 떨어져 있음)
    scene bg_6f_mental with dissolve
    
    "이전 층과는 다른, 끈적하고 비릿한 공기가 폐부를 찌른다. 벽은 온통 붉은 조명에 젖어 있고..."
    "마치 누군가 피 묻은 손으로 긁어낸 듯한 글씨들이 가득하다."
    "'놈들은 소리를 듣는다', '약을 믿지 마', '여기서 나가야 해'..."
    "익숙한 문장들. 이건... 인터넷 게시판에서 봤던 그 글인가? 아니, 그보다 훨씬 더..."

    "벽이 말을 걸고 있다."
    "기억 속 어딘가에서 본 듯한 문장들."
    "이건 내가 본 것이 아니라... 내가 쓴 것 같다."

    "그때, 바닥에 떨어진 종이 한 장이 눈에 들어왔다."

    # (바닥의 쪽지를 줍는다. 앞면 자동 노출)
    hide window
    show screen floor_6_note_front_screen with dissolve
    pause
    hide screen floor_6_note_front_screen with dissolve

    "낯설지 않다."
    "이 문장도... 이 종이의 질감도..."
    "모두 어디선가 느껴본 것 같다."
    
    "쪽지를 접어 올리려는 순간,"
    "손끝이 멈춘다."
    "이 쪽지... 정말, 끝까지 봐도 괜찮은 걸까? 이 얇은 종이 너머에 감당할 수 없는 진실이 숨어있을 것만 같다."

    menu:
        "뒷면까지 본다 (불길한 예감이 든다)":
            jump check_back_side_6
        "그냥 덮는다 (확신이 서지 않는다)":
            "괜히 건드리면 안 될 것 같았다."
            jump floor_5
        "찢어버린다 (위험해 보인다)":
            jump bad_ending_6

label check_back_side_6:
    "떨리는 손으로 쪽지를 뒤집었다. 하지만 그 순간, 글자들이 눈앞에서 조각나 흩어지는 것 같았다."
    "머리가 깨질 듯 아프다. 이 문장을... 내가 직접 완성해야만 해."

    # 조각난 문장 맞추기 미니게임 시작 (테스트용 분기)
    $ minigame_result = renpy.random.choice(["success", "fail"])

    if minigame_result == "success":
        hide window
        show screen floor_6_note_back_screen with dissolve
        pause
        hide screen floor_6_note_back_screen with dissolve

        "...왜 내 글씨로 쓰여 있는 거지?"

        $ renpy.sound.play(sfx_clue_gain)
        $ flag_clue_1 = True
        jump floor_5
    else:
        "머릿속에서 무언가 '툭'하고 끊어졌다. 쪽지의 글자도, 내 기억의 조각들도... 산산이 흩어져 사라져간다."
        jump bad_ending_6