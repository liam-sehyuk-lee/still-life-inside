define n = Character(None, what_prefix='"', what_suffix='"', what_color="#c8c8c8")
define m = Character('???', color="#888888", what_color="#888888")

label start:
    scene black with fade

    $ renpy.music.play("bgm_intro.ogg")

    "이젠 거의 리듬처럼 익숙해진다."
    "저 소리."
    "철문 바닥을 긁는 무거운 발소리,"
    "놈은 오늘도 온다. 나를 사육하기 위해."

    jump floor_7