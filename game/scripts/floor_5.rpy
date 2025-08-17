label floor_5:
    scene bg_5f_mental with dissolve
    
    n "나를 보는 건... 나인가?"
    n "아니야, 이건... 나 같은 형체일 뿐."
    n "거울 속 눈동자가 나를 따라오지 않는다."
    n "약... 저 약을 먹으면"
    n "이 눈에서 벗어날 수 있을까?"
    
    m "먹어. 그러면... 너도 우리와 같아질 수 있어."
    
    n "무릎이 떨린다."
    n "심장은 빨라지는데, 머리는... 멈췄다."
    
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
    
    n "나는 아직... 괴물이 되고 싶지 않다."
    jump floor_4