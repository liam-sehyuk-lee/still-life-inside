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
    scene bg_6f_mental with dissolve
    
    n "벽이 말을 걸고 있다."
    n "기억 속 어딘가에서 본 듯한 문장들."
    n "이건 내가 본 것이 아니라... 내가 쓴 것 같다."

    "바닥의 쪽지를 줍는다."

    hide window
    show screen floor_6_note_front_screen with dissolve
    pause
    hide screen floor_6_note_front_screen with dissolve

    n "낯설지 않다."
    n "이 문장도... 이 종이의 질감도..."
    n "모두 어디선가 느껴본 것 같다."
    n "쪽지를 접어 올리려는 순간,"
    n "손끝이 멈춘다."
    n "이 쪽지... 정말, 끝까지 봐도 괜찮은 걸까?"

    menu:
        "뒷면까지 본다 (불길한 예감이 든다)":
            jump check_back_side
        "그냥 덮는다 (확신이 서지 않는다)":
            jump cover_it
        "찢어버린다 (위험해 보인다)":
            jump bad_ending_6

label check_back_side:
    hide window
    show screen floor_6_note_back_screen with dissolve
    pause
    hide screen floor_6_note_back_screen with dissolve

    n "...왜 내 글씨로 쓰여 있는 거지?"

    $ renpy.sound.play(sfx_clue_gain)
    $ flag_clue_1 = True
    jump floor_5

label cover_it:
    n "괜히 건드리면 안 될 것 같았다."
    jump floor_5