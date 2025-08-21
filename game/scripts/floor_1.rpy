label floor_1:
    # 거대한 금속문. 그 위에 'EXIT' 사인이 깜빡인다. 문 앞에는 피 묻은 손자국이 있다.
    scene bg_1f_mental with dissolve
    
    "EXIT."
    "깜빡이는 붉은 글씨 아래, 거대한 금속문이 서 있다. 모든 것의 끝이자 시작."
    "차가운 문고리에 손을 뻗었다. 삐걱이는 소리와 함께 육중한 문이 조금씩 열리며, 눈부신 빛이 틈새로 쏟아져 들어왔다."

    "이제 끝이다."
    "문만 열면, 이 악몽에서 벗어날 수 있다."
    "그런데... 왜 나는 두려운 거지? 이 문 너머의 '일상'이, 방금까지 헤쳐온 '악몽'보다 더 낯설게 느껴진다."

    m "정말... 그 문을 여는 게 '탈출'이라고 생각해?"
    
    "나는 지금까지 무엇을 보아온 걸까. 나를 속박하던 존재, 나를 비추던 존재, 나에게 말을 걸던 존재들..."
    "그 모든 것들이 정말... 내 밖에 있었던 걸까?"

    "손이 문고리 위에서 멈칫했다."
    "나는... 무엇을 선택해야 하는가."
    
    menu:
        "이 문을 연다 (이것이 유일한 탈출구다)":
            "나는 눈을 감았다. 더는 생각하고 싶지 않았다."
            "어떤 진실이든, 이 지옥보다는 나을 것이다."
            jump ending_normal
        "되돌아본다 (...내가 본 건 진짜였을까?)":
            "아니. 도망치는 것은 의미가 없다."
            "내가 본 것, 내가 느낀 것. 그 모든 것의 의미를 알아야만 한다."
            jump turn_back_1

label turn_back_1:
    # (카메라 뒤로 전환, 방 안을 다시 보기 시작)

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

    if clue_count == 5:
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
    "모든 조각이 모였다. 이제... 이 끔찍한 기억을 내 손으로 완성해야만 한다."
    
    # 미니게임: 기억의 퍼즐 완성하기
    call screen minigame_puzzle

    if _return:
        "퍼즐이 맞춰졌다. 그래... 이게 바로 진실이었어."
        jump real_world_7
    else:
        "기억의 조각들이 손끝에서 흩어진다. 진실을 마주할 준비가... 아직 되지 않은 모양이다."
        jump ending_partial_truth