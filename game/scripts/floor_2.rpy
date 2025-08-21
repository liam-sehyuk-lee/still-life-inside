screen floor_2_comment_screen:
    frame:
        background "#00000080"
        padding (100, 100)
        xalign 0.5
        yalign 0.5
        
        text """oymnipulator314: 나도 그들에게 사육당하고 있어.
restores3421: 여긴 ZONE 12. 누구 있나요?
sometime5134: 함께 저항합시다.""":
            size 50
            color "#ffffff"

label floor_2:
    # 낡은 방. 책상 위에 노트북이 켜져 있고, 화면에는 '피해자'들의 절규가 담긴 게시판이 떠 있다.
    scene bg_2f_mental with dissolve

    "복도 끝에서 새어 나오는 희미한 불빛. 그곳에는 문이 반쯤 열린 방이 있었다."
    "방 안에는 낡은 책상과 의자, 그리고... 켜져 있는 노트북 한 대가 놓여 있었다."
    "나는 홀린 듯이 화면 앞으로 다가갔다. 화면 가득한 것은 나와 같은 '피해자'들의 절규였다."

    hide window
    show screen floor_2_comment_screen with dissolve
    pause
    hide screen floor_2_comment_screen with dissolve
    
    "'나도 사육당하고 있어', '함께 저항합시다'... 드디어 찾았다. 혼자가 아니었어!"
    "하지만 안도감도 잠시, 댓글들을 읽어 내려갈수록 기묘한 위화감이 온몸을 감쌌다."
    "모든 댓글의 문체가... 기묘할 정도로 비슷하다. 마치 한 사람이 쓴 것처럼."
    
    m "익숙한 목소리가 들리는 것 같지 않아?"

    "생각해 보니 그랬다. 이건 단순한 위화감이 아니었다."
    "글자들을 눈으로 읽고 있는데도, 머릿속에서는 익숙한 누군가의 목소리가 자동으로 재생되는 듯한 기분."
    "이 섬뜩한 가설을... 확인해야만 한다."
    
    menu:
        "로그를 정렬한다 (작성자 정보를 확인한다)":
            jump check_logs_2
        "화면을 꺼버린다 (진실을 외면한다)":
            "아니야, 나는 혼자가 아니야. 더 이상 의심하지 않겠어."
            jump floor_1
        "글을 하나 더 쓴다 (동료를 찾는다)":
            jump bad_ending_2

label check_logs_2:
    "나는 떨리는 손으로 관리자 페이지에 접속했다."
    "마우스를 클릭하자, 화면의 로그들이 암호처럼 뒤섞이기 시작했다."
    "이 혼돈 속에서... 진실을 찾아내야 해. 같은 흔적을 모두 연결해야만 해."

    # 미니게임: IP 주소 추적
    call screen minigame_breath

    if _return:
        "모두... 나였다. IP 주소가... 전부 동일하다."
        "화면의 모든 닉네임이 내 이름으로 바뀌는 환상을 보았다. 위로도, 저항도, 모두 나 혼자만의 독백이었다."

        $ renpy.sound.play(sfx_clue_gain)
        $ flag_clue_5 = True
        jump floor_1
    else:
        "로그를 맞추려 할수록 화면은 더욱 심하게 깨져나갔다. 결국... 'ACCESS DENIED'라는 붉은 글씨만 남기고 화면이 꺼져버렸다."
        "진실을 확인할 방법이 사라졌다. 나는... 계속해서 동료가 있다고 믿을 수밖에 없게 되었다."
        jump floor_1