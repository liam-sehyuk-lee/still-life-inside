## minigame_note.rpy

screen minigame_note():
    style_prefix "minigame_note"

    # 게임 변수 설정
    # 쪽지 조각 텍스트와 올바른 순서
    default note_pieces = ["나는", "이 문을", "열었다.", "그리고", "사라졌다."]
    default puzzle_state = []
    default mistake_count = 0
    default max_mistakes = 3

    # 배경 이미지
    add minigame_bg

    # 게임 설명
    frame:
        xalign 0.5
        yalign 0.2
        text "쪽지 조각을 올바른 순서로 클릭해 문장을 완성하세요."
        
    # 쪽지 조각 버튼들
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        
        for piece in note_pieces:
            button:
                xalign 0.5
                text piece
                action [SetScreenVariable("puzzle_state", puzzle_state + [piece]), renpy.jump("check_puzzle")]

    # 실패 메시지
    if mistake_count > 0:
        text "틀렸습니다. 다시 시도하세요. (남은 기회: [max_mistakes - mistake_count])" xalign 0.5 yalign 0.7 color "#ff0000"

    # 게임 로직 (파이썬)
    # on "show":
    #     $ renpy.sound.play(sfx_note_drop, channel="minigame_sfx")
    
    python:
        # 퍼즐 상태 확인
        if len(puzzle_state) > 0:
            current_index = len(puzzle_state) - 1
            if puzzle_state[current_index] != note_pieces[current_index]:
                # 오답일 경우
                mistake_count += 1
                puzzle_state = []
                renpy.jump("check_fail")
            elif len(puzzle_state) == len(note_pieces):
                # 정답일 경우
                renpy.sound.stop(channel="minigame_sfx")
                renpy.hide_screen("minigame_note")
                renpy.jump("minigame_success_note")

label check_fail:
    if mistake_count >= max_mistakes:
        return False # 게임 실패
    return

label minigame_success_note:
    return True # 게임 성공