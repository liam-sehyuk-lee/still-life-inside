label floor_3:
    # (긴 복도, 어둠 속 끝에서 흐릿한 형체가 보임. 발자국 소리, 점점 커짐)
    scene bg_3f_mental with dissolve
    
    "그게 다가오고 있다."
    "숨소리는 거칠고, 발걸음은 무겁다."
    "공기가 무겁게 짓누른다."

    "이대로 가만히 있으면..."
    "지나갈 수도 있을까?"
    "아니면... 숨을 곳이 필요해."
    
    "눈을 감고 싶다."
    "아무것도 못 본 척하고 싶다."
    
    menu:
        "숨는다 (벽장 안으로 조용히 들어간다)":
            jump hide
        "달린다 (이대로 도망치는 수밖에 없어)":
            jump bad_ending_3

label hide:
    "괴물이 지나갔다."
    "심장이 터질 듯이 뛰고, 몸이 떨렸다."
    
    menu:
        "그대로 나아간다 (숨을 고르고, 다음 층으로 간다)":
            jump floor_2
        "돌아본다 (놈의 정체를 직접 확인한다)" if flag_clue_1 and flag_clue_2 and flag_clue_3:
            jump turn_around

label turn_around:
    "복도 끝에 흐릿한 형체가 보인다."
    "등을 돌리고 있는 모습은... 낯익은 그림자였다."
    "괴물이 잠시 멈칫하는 것을 보았다."

    $ renpy.sound.play(sfx_clue_gain)
    $ flag_clue_4 = True
    jump floor_2