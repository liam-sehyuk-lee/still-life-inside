screen real_6_note:
    frame:
        background "#00000080"
        padding (100, 100)
        xalign 0.5
        yalign 0.5
        
        text "잊지 말고 꼭 챙겨먹으렴...":
            size 50
            color "#ffffff"

screen true_ending_text():
    frame:
        background "#00000080"
        xfill True
        yfill True
        text "트루엔딩: 마주하다":
            size 40
            color "#ffffff"
            xalign 0.5
            yalign 0.5

label real_world_7:
    scene bg_7f_reality with fade
    
    n "나는 그 문을 열 수 있었을까?"
    n "정말로 나가본 적이 있었을까?"
    n "...확인해야만 해."
    
    n "문은 잠겨 있었다."
    n "나는 안에서 나오지 않았고, 엄마는 밖에서 들어오지 못했다."
    
    jump real_world_6
    
label real_world_6:
    scene bg_6f_reality with fade
    
    n "이건... 내가 '암호'라고 착각했던 그 쪽지."
    n "사실은... 엄마가 남긴, 그저 평범한 메모였다."

    hide window
    show screen real_6_note with dissolve
    pause
    hide screen real_6_note with dissolve
    
    n "나는... 이걸 해석하려 들었지. 괴물의 지시처럼."
    
    jump real_world_5
    
label real_world_5:
    scene bg_5f_reality with fade
    
    n "이건 그 눈이었다."
    n "내가 보았던 괴물의 눈은, 결국 내 눈이었다."
    n "거울 속 나는, 말라 있었다."
    n "잠도 못 자고, 밥도 먹지 않고, 눈동자는 초점을 잃은 채였다."
    n "내가 무서워했던 약은... 사실 나를 보호하던 마지막 끈이었다."
    
    jump real_world_4
    
label real_world_4:
    scene bg_4f_reality with fade
    
    n "그 목소리는 항상 괴물의 것이었다."
    n "하지만 지금은 확실히 알 수 있다."
    n "그건 내 목소리였다."
    
    jump real_world_3
    
label real_world_3:
    scene bg_3f_reality with fade
    
    n "나는 그날, 문을 열지 않았다."
    n "엄마는 아무 말 없이 몇 분을 서 있었고,"
    n "결국... 돌아섰다."
    n "나는 무서웠다."
    n "밖이 아니라, 안에서부터."
    
    jump real_world_2

label real_world_2:
    scene bg_2f_reality with fade
    
    n "나는 여기서 싸웠다."
    n "존재하지 않는 괴물들과."
    n "그리고 나 자신과."
    n "댓글은 많았지만... 대화는 없었다."
    n "오직 나 혼자만, 혼잣말을 하고 있었다."
    
    jump real_world_1

label real_world_1:
    scene bg_1f_reality with fade
    
    n "문은 처음부터 열리지 않았다."
    n "밖으로 나가지 않은 것도, 괴물이 들어온 것도 없었다."
    n "그저... 나는, 여기 있었다."
    n "스스로 만든 감옥에서, 나를 가둔 채로."
    
    jump true_ending
    
label true_ending:
    scene black with fade
    n "이제는 알고 있다."
    n "괴물은, 밖에 있던 게 아니었다."
    n "...괜찮아. 지금은... 정말 괜찮아."
    
    hide window
    show screen true_ending_text with dissolve
    $ renpy.music.play(bgm_ending)
    
    pause
    hide screen true_ending_text with dissolve
    
    return