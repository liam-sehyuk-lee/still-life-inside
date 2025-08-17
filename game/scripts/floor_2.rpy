label floor_2:
    scene bg_2f_mental with dissolve
    
    "나도 그들에게 사육당하고 있어."
    "여긴 ZONE 12. 누구 있나요?"
    "함께 저항합시다."
    
    n "익숙하다."
    n "너무 익숙해서..."
    n "마치 내가 쓴 것 같다."
    "마우스를 움직인다."
    n "IP 주소... 전부 동일하다."
    m "넌... 널 속이고 있었어."
    
    menu:
        "로그를 정렬한다 (진짜 누가 썼는지 본다)":
            jump check_logs
        "화면을 꺼버린다 (모른 척하고 넘어간다)":
            jump turn_off
        "글을 하나 더 쓴다 (누군가 나를 봐야 해)":
            jump bad_ending_2

label check_logs:
    n "댓글 작성자 모두 동일한 ID와 IP인 것을 확인했다."
    n "모두 나였다."

    $ renpy.sound.play(sfx_clue_gain)
    $ flag_clue_5 = True
    jump floor_1

label turn_off:
    n "아무 일도 없던 것처럼..."
    jump floor_1