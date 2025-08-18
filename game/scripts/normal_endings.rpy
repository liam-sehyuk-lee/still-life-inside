screen ending_normal_text():
    frame:
        background "#00000080"
        xfill True
        yfill True
        text "일반엔딩: 문 밖의 세계":
            size 40
            color "#ffffff"
            xalign 0.5
            yalign 0.5

screen ending_flickering_memory_text():
    frame:
        background "#00000080"
        xfill True
        yfill True
        text "일반엔딩: 엇나간 기억":
            size 40
            color "#ffffff"
            xalign 0.5
            yalign 0.5

screen ending_uncertain_realization_text():
    frame:
        background "#00000080"
        xfill True
        yfill True
        text "일반엔딩: 불완전한 탈출":
            size 40
            color "#ffffff"
            xalign 0.5
            yalign 0.5

screen ending_partial_truth_text():
    frame:
        background "#00000080"
        xfill True
        yfill True
        text "일반엔딩: 감춰진 진실":
            size 40
            color "#ffffff"
            xalign 0.5
            yalign 0.5

label ending_normal:
    # (붉은 빛, 폐허 속 탈출 연출)
    scene black with fade
    "나는 이겼다... 라고 믿고 싶었다."
    "문이 열리고 밖으로 나섰다. 붉은 빛이 내 눈을 찔러왔지만, 이제 모든 것이 끝난 것 같았다."
    hide window
    show screen ending_normal_text with dissolve
    pause
    hide screen ending_normal_text with dissolve
    return

label ending_flickering_memory:
    scene black with fade
    "문 너머에 닿는 순간, 잊고 싶었던 기억의 한 조각이 스쳐 지나간다."
    "하지만 나는 그 의미를 깨닫지 못했다."
    hide window
    show screen ending_flickering_memory_text with dissolve
    pause
    hide screen ending_flickering_memory_text with dissolve
    return

label ending_uncertain_realization:
    scene black with fade
    "문이 열렸다. 나는 탈출했지만... 이 승리가 진짜인지 확신할 수 없었다."
    "내가 본 진실은 과연 전부였을까?"
    hide window
    show screen ending_uncertain_realization_text with dissolve
    pause
    return

label ending_partial_truth:
    scene black with fade
    "나는 문을 열고 밖으로 나섰다."
    "내가 본 것은, 폐허가 된 병원이었다."
    "진짜 괴물은 밖에 있었고, 나는... 그저 조종당했을 뿐이었다."
    hide window
    show screen ending_partial_truth_text with dissolve
    pause
    hide screen ending_partial_truth_text with dissolve
    return