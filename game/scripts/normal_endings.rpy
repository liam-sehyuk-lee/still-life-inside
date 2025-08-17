label normal_ending:
    scene black with fade
    n "나는 이겼다... 라고 믿고 싶었다."
    n "문이 열리고 밖으로 나섰다. 붉은 빛이 내 눈을 찔러왔지만, 이제 모든 것이 끝난 것 같았다."
    n "일반 엔딩: 문 밖의 세계"
    return

label ending_flickering_memory:
    scene black with fade
    n "문 너머에 닿는 순간, 잊고 싶었던 기억의 한 조각이 스쳐 지나간다."
    n "하지만 나는 그 의미를 깨닫지 못했다."
    n "일반엔딩: 엇나간 기억"
    return

label ending_uncertain_realization:
    scene black with fade
    n "문이 열렸다. 나는 탈출했지만... 이 승리가 진짜인지 확신할 수 없었다."
    n "내가 본 진실은 과연 전부였을까?"
    n "일반엔딩: 불완전한 탈출"
    return

label ending_partial_truth:
    scene black with fade
    n "나는 문을 열고 밖으로 나섰다."
    n "내가 본 것은, 폐허가 된 병원이었다."
    n "진짜 괴물은 밖에 있었고, 나는... 그저 조종당했을 뿐이었다."
    n "일반엔딩: 감춰진 진실"
    return
    
screen end_text_normal():
    modal True
    vbox:
        yalign 0.5
        xalign 0.5
        text _("일반 엔딩: 문 밖의 세계") size 40