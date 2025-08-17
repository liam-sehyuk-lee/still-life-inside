label floor_1:
    scene bg_1f_mental with dissolve
    
    n "이제 끝이다."
    n "문만 열면, 이 악몽에서 벗어날 수 있다."
    n "그런데... 왜 나는 두려운 거지?"
    
    m "진짜 너는 어디에 있지?"
    m "문을 열기 전에... 돌아봐야 할 게 있어."
    
    n "문이 열리기 직전, 주인공의 손이 멈춘다."
    
    menu:
        "문을 연다 (더는 견딜 수 없어)":
            jump ending_normal
        "되돌아본다 (...내가 본 건 진짜였을까?)":
            jump turn_back

label turn_back:
    # 획득한 진엔딩 플래그의 총 개수를 확인합니다.
    $ clue_count = 0
    if flag_clue_1:
        $ clue_count += 1
    if flag_clue_2:
        $ clue_count += 1
    if flag_clue_3:
        $ clue_count += 1
    if flag_clue_4:
        $ clue_count += 1
    if flag_clue_5:
        $ clue_count += 1

    if clue_count == 5:
        jump true_ending_route
    elif clue_count == 4:
        jump ending_partial_truth
    elif clue_count >= 2:
        jump ending_uncertain_realization
    elif clue_count == 1:
        jump ending_flickering_memory
    else:
        # 플래그가 0개일 경우, 일반 엔딩으로 갑니다.
        jump ending_normal
    
label true_ending_route:
    # 진엔딩 루트 해금
    jump real_world_7