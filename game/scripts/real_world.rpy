screen real_6_note:
    frame:
        background "#00000080"
        padding (100, 100)
        xalign 0.5
        yalign 0.5
        
        text "잊지 말고 꼭 챙겨먹으렴...":
            size 50
            color "#ffffff"

screen real_4_recorder_text:
    frame:
        background "#00000080"
        padding (100, 100)
        xalign 0.5
        yalign 0.5
        
        text """…괜찮아. 나 혼자라도 괜찮아…
문은 안 열면 돼…
그러면 안 들어오니까…""":
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

transform zoom_move(newzoom, newx, newy, t=1.0):
    linear t zoom newzoom xalign newx yalign newy

label real_world_7:
    # 모든 기억의 퍼즐을 맞춘 뒤, 시점은 천천히 '현실'의 방으로 돌아온다.
    # 망상 속 7층의 배경음악이 서서히 멎는다.
    stop music fadeout 2.0
    
    "나는... 정말로 문을 열었던 걸까?"
    "아니, 애초에... 밖으로 나간다는 선택지가 존재했던가?"
    "...모든 것을 다시 확인해야만 했다."

    # 화면이 암전되었다가, '현실의 방' 전체 모습이 천천히 드러난다.
    scene bg_reality_master with Dissolve(2)

    "이곳이 내 세상의 전부였다."
    "7개의 층으로 이루어진 거대한 감옥 따위는 없었다."
    "그저... 낡은 가구와 먼지가 전부인, 이 작은 방 하나뿐이었다."
    
    # 카메라는 방 중앙의 '방문'을 천천히 비춘다.
    show bg_reality_master at zoom_move(1.5, 0.4, 0.4, 1.0)
    
    "문은... 처음부터 굳게 닫혀 있었다."
    "내가 안에서 열지 않았고, 그 누구도 밖에서 들어오지 못했다."
    "이 문은 탈출구가 아니라, 나 스스로를 가둔 감옥의 벽이었다."

    jump real_world_6
    
label real_world_6:
    # 카메라는 7층에서 비추던 문에서, 그 아래 바닥으로 천천히 이동한다.
    # 그곳은 어머니가 항상 식판과 메모를 놓아두던 자리다.
    show bg_reality_master at zoom_move(2.0, 0.4, 0.8, 1.0)
    
    "문 아래, 이 차가운 바닥 위에서..."
    "나는 매일같이 괴물이 보낸 '암호'를 기다렸다."

    hide window
    show screen real_6_note with dissolve
    pause
    hide screen real_6_note with dissolve
    
    "망상 속에서는 섬뜩한 지시처럼 들렸던 그 문장."
    "사실은... 밖에서 문이 열리기만을 기다리던 엄마가 남긴, 그저 평범한 걱정의 메모였다."
    
    "나는 그 평범한 온기마저 두려워하며, 스스로를 더 깊은 어둠 속으로 몰아넣었다."
    
    jump real_world_5
    
label real_world_5:
    # 카메라는 문 앞에서부터 방의 오른쪽, 거울과 서랍장이 있는 곳으로 부드럽게 이동한다.
    show bg_reality_master at zoom_move(2.5, 0.65, 0.5, 1.0)

    "시선을 돌리자, 방 한쪽의 낡은 거울이 눈에 들어왔다."
    "망상 속에서 나를 비웃던 그 '눈'은..."
    "결국... 잠들지 못해 퀭하고, 초점을 잃은 채 흔들리던 내 눈이었다."

    "거울 속의 나는, 유령처럼 말라 있었다."
    "나는 나 자신을 괴물이라 여기며, 스스로를 얼마나 갉아먹고 있었던 걸까."

    # 카메라가 서랍장 위의 약으로 조금 더 다가간다.
    show bg_reality_master at zoom_move(3.0, 0.99, 0.6, 1.0)

    "그리고 그 옆... 내가 그토록 두려워하며 거부했던 약."
    "봉투에는 흐릿한 글씨로 이름이 적혀 있었다. '리스페리돈 1mg'."
    
    "괴물이 건네는 독이 아니었다. 나를 현실에 붙들어주던... 마지막 끈이었다."

    jump real_world_4
    
label real_world_4:
    # 카메라가 의자 위 작은 녹음기로 다가간다.
    show bg_reality_master at zoom_move(5.0, 0.675, 0.625, 1.0)

    "그리고 저 의자 위의 작은 녹음기."
    "망상 속에서, 나는 저 기계에서 흘러나오는 목소리를 항상 '괴물'의 것이라고 믿었다."
    "진실을 듣는 것이 두려워, 애써 외면하고 싶었던 그 목소리."

    hide window
    show screen real_4_recorder_text with dissolve
    pause
    hide screen real_4_recorder_text with dissolve

    "이제는 안다."
    "그건 괴물의 목소리가 아니었다. 겁에 질려 끊임없이 되뇌던, 바로 내 목소리였다."
    "누군가에게 보내는 구조 신호가 아니었다. 그저 이 방 안에서 고립된 내가, 나에게 들려주던 처절한 고백이었다."

    jump real_world_3
    
label real_world_3:
    # 카메라는 방의 왼쪽에서 다시 중앙, 방문 앞으로 이동하며 문틈 아래를 비춘다.
    show bg_reality_master at zoom_move(2.5, 0.4, 0.9, 1.0)

    "망상 속에서 나를 쫓아오던 그 무겁던 발소리..."
    "축축하게 끌리던 소리와 비릿한 냄새..."
    "그 모든 공포의 실체는, 사실 문틈 아래로 비치던 저 그림자였다."

    # 여기서 문틈 아래로 그림자가 나타났다가 사라지는 애니메이션을 추가하면 효과적입니다.
    # 예: show shadow_animation with dissolve ... hide shadow_animation with dissolve

    "나는 그날, 문을 열지 않았다."
    "엄마는 아무 말 없이 몇 분을 더 문 앞에 서 있었다."
    "문고리를 잡으려 망설이는 소리가 희미하게 들려왔지만, 결국... 발소리는 멀어졌다."
    
    "나는 무서웠다."
    "쫓아오던 괴물이 무서웠던 게 아니다."
    "문을 열었을 때 마주해야 할 현실이, 그리고 그 현실 속의 내가... 무서웠다."

    jump real_world_2

label real_world_2:
    # 카메라는 문 앞에서 방의 왼쪽, 컴퓨터 책상으로 이동하며 모니터를 비춘다.
    show bg_reality_master at zoom_move(3.0, 0.0, 0.65, 1.0)

    "그리고 이곳."
    "이 작은 모니터 앞에서, 나는 세상과 싸우고 있다고 믿었다."
    "존재하지 않는 괴물들과, 그리고... 결국엔 나 자신과."

    # 모니터 화면으로 조금 더 줌인
    show bg_reality_master:
        zoom 3
        crop (50, 650, 889, 500) # 모니터 부분만 잘라내어 확대
        size (1920, 1080)
        xalign 0 yalign 0.65
        linear 1.0
    
    "수많은 닉네임, 수많은 댓글들... 나는 그 안에서 위로를 찾고 연대감을 느꼈다."
    "하지만 그곳엔 대화 같은 건 없었다."
    "처음부터 끝까지, 오직 나 혼자만의 처절한 독백만이 화면을 채우고 있었을 뿐이다."

    jump real_world_1

label real_world_1:
    # 카메라는 컴퓨터 앞에서 방의 출입문으로 이동해, 문 전체를 정면으로 비춘다.
    # 모든 것을 깨달은 뒤 마주하는, 움직임 없는 마지막 장면.
    show bg_reality_master:
        zoom 1.5
        crop None
        size None
        xalign 0.4 yalign 0.4
        linear 1.0

    show bg_reality_master at zoom_move(1.0, 0.5, 0.5, 1.0)

    "결국... 모든 것은 이 방 안에서 시작되고, 이 방 안에서 끝났다."
    "망상 속에서 내가 열고자 했던 그 '탈출구'는..."
    "단 한 번도 열리지 않았던, 바로 이 방문이었다."

    "밖으로 나가지도, 괴물이 들어온 적도 없었다."
    "그저... 나는, 처음부터 여기 있었다."
    "스스로 만든 이 작은 감옥에서, 나 자신을 가둔 채로."

    jump true_ending
    
label true_ending:
    # 카메라는 1층의 문을 비춘 채 잠시 멈춘다. 그리고 천천히, 모든 것이 어둠 속으로 사라진다.
    scene black with Dissolve(3.0)

    # 어둠 속에서 주인공의 마지막 독백이 이어진다.
    "괴물을 피해 숨어들어온 이 방은, 사실 나를 지키던 마지막 요새였다."
    "괴물에게서 도망치려 했던 모든 순간은, 사실 현실의 나로부터 도망치려던 발버둥이었다."

    "이제는 알고 있다."
    "괴물은... 단 한 번도 내 밖에 있었던 적이 없었다."

    "괜찮아."
    "이제... 정말로 괜찮아."

    # 엔딩 테마 음악 시작. 화면 암전. 천천히 타이틀 출력
    hide window
    show screen true_ending_text with dissolve
    $ renpy.music.play(bgm_ending)

    pause 5.0
    hide screen true_ending_text with dissolve

    return