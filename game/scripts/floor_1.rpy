label floor_1:
    # 거대한 금속문. 그 위에 'EXIT' 사인이 깜빡인다. 문 앞에는 피 묻은 손자국이 있다.
    scene bg_1f_mental with dissolve
    
    n "EXIT... 드디어 여기까지 왔어."
    m "그래. 이제 끝이야. 저 문만 열면 돼."
    
    "나는 지금까지 무엇을 보아온 걸까. 나를 속박하던 존재, 나를 비추던 존재, 나에게 말을 걸던 존재들..."
    "그 모든 것들이 정말... 내 밖에 있었던 걸까?"
    "손이 문고리 위에서 멈칫했다."
    n "무서워. 이 문 너머의 '일상'이, 방금까지 헤쳐온 '악몽'보다 더 낯설게 느껴져."
    m "두려워하지 마. 이 방이 우리를 지켜주는 곳이라니, 말도 안 돼. 우리가 함께 싸워 이겨낸 곳이야. 이 문을 열고 진짜 세상으로 나아가야 해."
    n "나는... 무엇을 선택해야 하는가. 나의 직감을 믿어야 할까, 아니면... 저 문 너머의 공포를 외면해야 할까?"
    menu:
        "이 문을 연다 (이것이 유일한 탈출구다)":
            "더는 생각하고 싶지 않아. 어떤 진실이든, 이 지옥보다는 나을 거야."
            m "좋아. 드디어 우리가 해냈어! 문을 열고 나가자!"
            jump ending_normal
        "되돌아본다 (...내가 본 건 진짜였을까?)":
            "아니. 도망치는 것은 의미가 없다."
            n "내가 본 것, 내가 느낀 것. 그 모든 것의 의미를 알아야만 한다."
            m "무슨 소리야? 빨리 나가야 해! 놈들이 눈치채기 전에! 놈들의 마지막 함정일지도 몰라!"
            jump turn_back_1

label turn_back_1:
    # 획득한 진엔딩 플래그의 총 개수를 확인
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

    if clue_count >= 5:
        jump memory_puzzle_minigame_1
    elif clue_count == 4:
        jump ending_partial_truth
    elif clue_count >= 2:
        jump ending_uncertain_realization
    elif clue_count == 1:
        jump ending_flickering_memory
    else:
        jump ending_normal

label memory_puzzle_minigame_1:
    n "모든 조각이 모였어. 이제... 이 끔찍한 기억을 내 손으로 완성해야만 해."
    m "안 돼! 제발 멈춰! 퍼즐을 맞추면 모든 것이 끝장나! 놈들이 원하는 게 그거야!"
    n "아니. 이게 마지막 기회야. 모든 것을 끝낼 마지막 기회."
    # 미니게임: 기억의 퍼즐 완성하기
    call screen minigame_puzzle

    if _return:
        "퍼즐이 맞춰졌다. 조각들이 하나가 되자, 온몸에 소름이 돋았다."
        n "그래... 이게... 바로 진실이었어."
        m "아니야... 말도 안 돼... 이럴 리가 없어...!"
        "놈이 발악하는 목소리를 뒤로 한 채, 나는 모든 것을 받아들였다."
        jump real_world_7
    else:
        "기억의 조각들이 손끝에서 흩어진다. 퍼즐이 완성되지 않았다."
        n "실패했어... 아직은 아닌가 봐..."
        m "다행이야... 놈들의 마지막 함정을 피한 것 같아. 어서 문을 열고 나가자!"
        jump ending_partial_truth