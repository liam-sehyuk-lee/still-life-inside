define n = Character('나', what_prefix='"', what_suffix='"', what_color="#a0c0ff")
define m = Character('???', color="#b28cbe", what_color="#b28cbe")

label start:
    scene black with fade
    # 인트로 BGM
    $ renpy.music.play(bgm_intro)

    "이젠 거의 리듬처럼 익숙해진다."
    "저 소리."
    "철문 바닥을 긁는 무거운 발소리,"
    "놈은 오늘도 온다. 나를 사육하기 위해."
    
    n "또야... 오늘도 저 소리야."
    "그때, 내 머릿속에서 익숙한 목소리가 들려왔다."
    m "괜찮아. 내가 있잖아."
    n "..."
    m "두려워하지 마. 우리는 늘 함께였으니까. 이 공포도, 곧 끝날 거야."

    jump floor_7