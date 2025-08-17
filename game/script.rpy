# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.

# 게임에서 사용할 캐릭터를 정의합니다.
define n = Character(None, what_prefix='"', what_suffix='"')
define m = Character('내 속의 목소리', color="#888888")

# 여기에서부터 게임이 시작합니다.
label start:
    scene black with fade  # 배경을 검정색으로 설정하고 페이드 효과를 적용합니다.

    # 배경음악이나 효과음이 있다면 여기에 추가
    # $ renpy.music.play("bgm_intro.ogg")

    n "이젠 거의 리듬처럼 익숙해진다."
    n "저 소리."
    n "철문 바닥을 긁는 무거운 발소리,"
    n "놈은 오늘도 온다. 나를 사육하기 위해."

    jump floor_7  # 7층 스크립트로 바로 이동