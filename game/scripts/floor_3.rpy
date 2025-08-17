label floor_3:
    scene bg_3f_mental with dissolve
    
    n "그게 다가오고 있다."
    n "숨소리는 거칠고, 발걸음은 무겁다."
    n "공기가 무겁게 짓누른다."
    n "이대로 가만히 있으면..."
    n "지나갈 수도 있을까?"
    n "아니면... 숨을 곳이 필요해."
    n "눈을 감고 싶다."
    n "아무것도 못 본 척하고 싶다."
    
    menu:
        "숨는다 (벽장 안으로 조용히 들어간다)":
            jump hide
        "달린다 (이대로 도망치는 수밖에 없어)":
            jump bad_ending_3
        "돌아본다 (놈의 정체를 직접 확인한다)" if flag_clue_1 and flag_clue_2 and flag_clue_3:
            jump turn_around

label hide:
    n "괴물이 지나갔다."
    n "심장이 터질 듯이 뛰고, 몸이 떨렸다."
    jump floor_2

label turn_around:
    n "흐릿한 형체가 엄마처럼 보였다."
    n "괴물이 잠시 멈칫하는 것을 보았다."
    n "이 순간을 놓치지 않고, 나는 재빨리 몸을 숨겼다."

    $ renpy.sound.play(sfx_clue_gain)
    $ flag_clue_4 = True
    jump floor_2