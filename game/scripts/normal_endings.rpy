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
    # 일반엔딩: 약간의 불안감이 남는 희망적 분위기
    $ renpy.music.play(bgm_ending_normal, fadein=1.0, loop=False)
    scene black with fade
    n "우리가 이겼어. 드디어... 문이 열리고 밖으로 나왔어."
    m "그래. 드디어 자유야! 이 붉은 빛이 눈부시지만, 이보다 더 좋을 순 없어!"
    n "끝난 것... 같아. 정말로 끝난 걸까?"
    m "더 이상 의심하지 마. 넌 해냈어. 우린 이겼다고!"
    
    "나는 '???'의 말을 믿기로 했다. 끝없이 나를 지탱해 주었던 목소리. 그 목소리가 옳았을 것이다."
    "하지만 발걸음을 옮길 때마다, 심장이 불안하게 쿵쿵거렸다. 나는 이 승리가, 그리고 이 자유가... 진짜인지 확신할 수 없었다."
    
    hide window
    show screen ending_normal_text with dissolve
    pause
    hide screen ending_normal_text with dissolve
    $ renpy.music.stop(fadeout=1.0)
    return

label ending_flickering_memory:
    # 엇나간 기억: 몽환적이고 미스터리한 분위기
    $ renpy.music.play(bgm_ending_flickering, fadein=1.0, loop=False)
    scene black with fade
    "문 너머에 닿는 순간, 잊고 싶었던 기억의 한 조각이 스쳐 지나간다."
    "나는 그 의미를 알지 못했지만..."
    n "이건... 뭐지? 희미한 빛. 너무나... 그리운 기분이야."
    m "괜찮아. 과거는 신경 쓰지 마. 이제 우리의 앞날만 생각하자. 함께라면 괜찮아!"
    
    "그날 이후, 나는 종종 알 수 없는 기억의 잔상들을 보았다. 희미하게 떠오르는 누군가의 얼굴, 잊고 싶었던 목소리..."
    "나는 그 조각들을 외면했다. 그리고 '???'의 목소리는 나를 다독이며, 그 기억들은 모두 '놈들'이 만든 가짜라고 속삭였다."
    "나는 그렇게, 불완전한 평화 속에서 살아갔다."
    
    hide window
    show screen ending_flickering_memory_text with dissolve
    pause
    hide screen ending_flickering_memory_text with dissolve
    $ renpy.music.stop(fadeout=1.0)
    return

label ending_uncertain_realization:
    # 불완전한 탈출: 불안하고 긴장감이 유지되는 분위기
    $ renpy.music.play(bgm_ending_uncertain, fadein=1.0, loop=False)
    scene black with fade
    n "문이 열렸다. 나는 탈출했지만... 이 승리가 진짜인지 확신할 수 없어."
    m "왜 그래? 우린 해냈어! 이제 자유야! 불안해하지 마!"
    n "하지만... 내가 본 것들이 정말 전부였을까?"
    m "중요하지 않아. 중요한 건 우리가 여기 있다는 거야. 이제 아무것도 우리를 쫓아오지 않아. 정말 괜찮아."
    
    "나는 끊임없이 뒤를 돌아보았다. 언젠가 이 승리가 가짜였다는 것을, 내가 또 다른 감옥에 갇혔다는 것을 알게 될까 두려웠다."
    "끝나지 않은 악몽. 나는 영원히 이 불안감 속에서 살아가야 할 것이다."
    
    hide window
    show screen ending_uncertain_realization_text with dissolve
    pause
    hide screen ending_uncertain_realization_text with dissolve
    $ renpy.music.stop(fadeout=1.0)
    return

label ending_partial_truth:
    # 감춰진 진실: 음산하고 불길한 분위기
    $ renpy.music.play(bgm_ending_partial, fadein=1.0, loop=False)
    scene black with fade
    n "나는 문을 열고 밖으로 나섰다. 그리고... 내가 본 것은, 폐허가 된 병원이었다."
    m "봐. 드디어 알게 되었어! 모든 것은 놈들이 만든 가짜 감옥이었던 거야!"
    n "우리가... 우리가 여기서 벗어났구나. 정말로... 이게 진짜 세상이었구나."
    m "그래. 이제야 제대로 알게 되었어. 이 모든 것은 놈들이 만든 게임이었어. 하지만 우리는 끝까지 살아남았지!"
    
    "나는 '???'의 말을 믿었다. 하지만 '우리'라는 단어가 묘하게 거슬렸다. 나는 문밖의 폐허를 바라보며, 문득 생각했다."
    "이게 진실이라고 해도... 정말 온전한 진실일까? '놈들'은 사라졌지만, '???'는 여전히 내 안에 남아 있다."
    "나는 또 다른 감옥에 갇힌 것은 아닐까. 어쩌면 가장 깊은 감옥에."
    
    hide window
    show screen ending_partial_truth_text with dissolve
    pause
    hide screen ending_partial_truth_text with dissolve
    $ renpy.music.stop(fadeout=1.0)
    return