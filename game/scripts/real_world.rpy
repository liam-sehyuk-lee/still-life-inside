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
    # (문 앞. 화면 멈춤. 소리 없음. 주변 어두워지고 내레이션 등장)
    
    "나는 그 문을 열 수 있었을까?"
    "정말로 나가본 적이 있었을까?"
    "...확인해야만 해."

    # (좁은 원룸 침대, 방문 앞 식판. 어머니의 목소리가 들려옴)
    scene bg_7f_reality with fade
    
    "문은 잠겨 있었다."
    "나는 안에서 나오지 않았고, 엄마는 밖에서 들어오지 못했다."
    
    jump real_world_6
    
label real_world_6:
    # (방문 앞 식판 클로즈업)
    scene bg_6f_reality with fade
    
    "이건... 내가 '암호'라고 착각했던 그 쪽지."
    "사실은... 엄마가 남긴, 그저 평범한 메모였다."

    hide window
    show screen real_6_note with dissolve
    pause
    hide screen real_6_note with dissolve
    
    "나는... 이걸 해석하려 들었지. 괴물의 지시처럼."
    
    jump real_world_5
    
label real_world_5:
    # (옷장 옆 거울. 탁자 위 약봉지. 조명이 매우 현실적)
    scene bg_5f_reality with fade
    
    "이건 그 눈이었다."
    "내가 보았던 괴물의 눈은, 결국 내 눈이었다."

    "거울 속 나는, 말라 있었다."
    "잠도 못 자고, 밥도 먹지 않고, 눈동자는 초점을 잃은 채였다."
    
    # (약봉지 확대)
    # [약봉지 라벨]  
    # “리스페리돈 1mg. 1일 1회 복용.”
    
    "내가 무서워했던 약은... 사실 나를 보호하던 마지막 끈이었다."
    
    jump real_world_4
    
label real_world_4:
    # (작은 욕실. 의자 위 녹음기. 플레이어가 조용히 눌러 재생)
    scene bg_4f_reality with fade

    # [녹음기 음성]  
    # “…괜찮아. 나 혼자라도 괜찮아… 문은 안 열면 돼… 그러면 안 들어오니까…”
    
    "그 목소리는 항상 괴물의 것이었다."
    "하지만 지금은 확실히 알 수 있다."
    "그건 내 목소리였다."
    "누구에게 들려주기 위한 것도, 구해달라는 외침도 아니었다."
    
    "그저… 내 안에서 끊임없이 돌고 있던 고백."

    jump real_world_3
    
label real_world_3:
    # (문 틈 아래로 보이는 슬리퍼. 그림자가 멈춰 있음)
    scene bg_3f_reality with fade
    
    "나는 그날, 문을 열지 않았다."
    "엄마는 아무 말 없이 몇 분을 서 있었고,"
    "결국... 돌아섰다."

    # (잠시 정적. 손이 문고리에 닿았다가 멈춘다.)

    "나는 무서웠다."
    "밖이 아니라, 안에서부터."
    
    jump real_world_2

label real_world_2:
    # (노트북 화면. 포럼 창. 댓글: “괴물들은 우리를 지켜보고 있어.”)
    scene bg_2f_reality with fade
    
    "나는 여기서 싸웠다."
    "존재하지 않는 괴물들과."
    "그리고 나 자신과."

    # (마우스를 움직이면, 모든 게시글의 작성자가 ‘guest1’로 되어 있음)

    "댓글은 많았지만... 대화는 없었다."
    "오직 나 혼자만, 혼잣말을 하고 있었다."
    
    jump real_world_1

label real_world_1:
    # (현관문 클로즈업. 열려 있지 않음. 아무도 없다)
    scene bg_1f_reality with fade
    
    "문은 처음부터 열리지 않았다."
    "밖으로 나가지 않은 것도, 괴물이 들어온 것도 없었다."

    "그저... 나는, 여기 있었다."
    "스스로 만든 감옥에서, 나를 가둔 채로."

    jump true_ending
    
label true_ending:
    # (카메라 천천히 뒤로 물러남. 주인공의 뒷모습. 화면 정적)
    scene black with fade
    "이제는 알고 있다."
    "괴물은, 밖에 있던 게 아니었다."
    
    "...괜찮아. 지금은... 정말 괜찮아."
    
    # (엔딩 테마 음악 시작. 화면 암전. 천천히 타이틀 출력)
    hide window
    show screen true_ending_text with dissolve
    $ renpy.music.play(bgm_ending)
    
    pause
    hide screen true_ending_text with dissolve
    
    return