screen floor_2_comment_screen:
    frame:
        background "#00000080"
        padding (100, 100)
        xalign 0.5
        yalign 0.5
        
        text """나도 그들에게 사육당하고 있어.
여긴 ZONE 12. 누구 있나요?
함께 저항합시다.""":
            size 50
            color "#ffffff"

label floor_2:
    scene bg_2f_mental with dissolve
    # @@@@@@@ 이미지변경 필요
    "익숙한 복도 끝, 낡은 방이 하나 있다."
    "안으로 들어가자, 전원이 켜진 채 빛을 내는 노트북 한대가 보인다."
    "나는 홀린 듯이 화면 앞으로 다가갔다."

    # (책상 위, 노트북 켜짐. 화면엔 게시판. 수많은 댓글들로 가득하다.)
    hide window
    show screen floor_2_comment_screen with dissolve
    pause
    hide screen floor_2_comment_screen with dissolve
    
    "익숙하다."
    "너무 익숙해서..."
    "마치 내가 쓴 것 같다."
    "마우스를 움직인다."
    "IP 주소... 전부 동일하다."
    m "넌... 널 속이고 있었어."
    
    menu:
        "로그를 정렬한다 (진짜 누가 썼는지 본다)":
            jump check_logs
        "화면을 꺼버린다 (모른 척하고 넘어간다)":
            jump turn_off
        "글을 하나 더 쓴다 (누군가 나를 봐야 해)":
            jump bad_ending_2

label check_logs:
    # (댓글 작성자 모두 동일한 ID/IP 확인) @@@@ 이미지 필요
    "모두 나였다."

    $ renpy.sound.play(sfx_clue_gain)
    $ flag_clue_5 = True
    jump floor_1

label turn_off:
    "아무 일도 없던 것처럼..."
    jump floor_1