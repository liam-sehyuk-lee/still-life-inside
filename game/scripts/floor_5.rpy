label floor_5:
    # (방은 차가운 푸른 조명. 중앙에는 거울, 옆 탁자에 약통)
    scene bg_5f_mental with dissolve
    
    "나를 보는 건... 나인가?"
    "아니야, 이건... 나 같은 형체일 뿐."

    "거울 속 눈동자가 나를 따라오지 않는다."
    "약... 저 약을 먹으면"
    "이 눈에서 벗어날 수 있을까?"
    
    m "먹어. 그러면... 너도 우리와 같아질 수 있어."
    
    "무릎이 떨린다."
    "심장은 빨라지는데, 머리는... 멈췄다."
    
    menu:
        "약을 먹는다 (더 이상 두려움을 느끼고 싶지 않다)":
            jump bad_ending_5_1
        "눈을 피한다 (거울에서 시선을 뗀다)":
            jump avoid_eyes
        "거울을 깨뜨린다 (이 지옥을 끝낸다)":
            jump bad_ending_5_2

label avoid_eyes:
    $ renpy.sound.play(sfx_clue_gain)
    $ flag_clue_2 = True
    
    "나는 아직... 괴물이 되고 싶지 않다."
    # (탁자에 손을 얹고 일어섬 → 다음 층)
    jump floor_4