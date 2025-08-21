# minigame_note.rpy

init python:
    # --- 퍼즐 설정 ---
    # 퍼즐을 구성하는 단어 조각들과 정답입니다.
    NOTE_PUZZLE_WORDS = ["나는", "이 문을", "열었다.", "그리고", "사라졌다."]
    NOTE_PUZZLE_SOLUTION = ["나는", "이 문을", "열었다.", "그리고", "사라졌다."]

    # 퍼즐의 현재 상태를 저장할 변수들입니다.
    note_word_bank = []      # 플레이어가 선택할 수 있는 단어 목록입니다.
    note_player_answer = []  # 플레이어가 순서대로 배치한 단어 목록입니다.

    # --- 퍼즐 관련 함수 ---
    def note_puzzle_start():
        """쪽지 퍼즐을 초기화하거나 재설정합니다."""
        # 원본 리스트를 수정하지 않기 위해 복사본을 만듭니다.
        # renpy.random.shuffle은 리스트를 직접 뒤섞습니다.
        shuffled_words = list(NOTE_PUZZLE_WORDS)
        renpy.random.shuffle(shuffled_words)

        # 섞인 단어들을 플레이어가 볼 수 있는 단어 목록에 할당합니다.
        store.note_word_bank = shuffled_words
        # 플레이어의 정답 칸을 비웁니다.
        store.note_player_answer = []

    def note_puzzle_add_word(word):
        """단어 목록에서 정답 칸으로 단어를 옮깁니다."""
        if word in store.note_word_bank:
            store.note_word_bank.remove(word)
            store.note_player_answer.append(word)

# 퍼즐 버튼과 영역을 위한 스타일 정의
style note_puzzle_frame:
    background Frame("gui/frame.png", 15, 15) # 기본 프레임을 사용 중입니다. 다른 프레임이 있다면 경로를 수정하세요.
    padding (15, 10)
    yminimum 80

style note_puzzle_button_text:
    size 32
    color "#40332b"
    hover_color "#6f5a4b"

# --- 미니게임 스크린 ---
screen minigame_note():
    """찢어진 쪽지 조각을 재배열하는 '클릭하여 배치' 방식의 퍼즐 스크린입니다."""
    modal True

    # 스크린이 처음 표시될 때, 퍼즐을 초기화합니다.
    on "show":
        action Function(note_puzzle_start)

    # --- UI 부분 ---
    # 미니게임 영역을 위한 배경 이미지를 추가하세요. (예: 책상 또는 종이)
    # add "minigame_note_bg.png"
    add Solid("#000000aa") # 지금은 어둡고 투명한 배경을 사용합니다.

    frame:
        style "game_menu_frame" # 전체 퍼즐을 감싸는 더 큰 프레임입니다.
        padding (40, 40)
        align (0.5, 0.5)

        vbox:
            spacing 20

            # 1. 안내 문구
            text "흩어진 조각들을 올바른 순서로 배열하세요." style "minigame_guide_text"

            # 2. 정답 영역 (문장이 만들어지는 곳)
            hbox:
                style "note_puzzle_frame"
                xalign 0.5
                spacing 10
                # 플레이어가 선택한 단어들을 표시합니다.
                for word in note_player_answer:
                    frame:
                        style "note_puzzle_frame"
                        text word style "note_puzzle_button_text"

            # 3. 단어 목록 영역 (선택할 수 있는 단어들)
            hbox:
                style "note_puzzle_frame"
                xalign 0.5
                spacing 10
                # 선택 가능한 단어 버튼들을 표시합니다.
                for word in note_word_bank:
                    textbutton word action Function(note_puzzle_add_word, word=word) style "note_puzzle_button"

            # 4. 조작 버튼
            hbox:
                xalign 0.5
                spacing 20
                textbutton "다시하기 (Reset)" action Function(note_puzzle_start) style "confirm_button"

                # '확인' 버튼은 플레이어의 정답과 실제 정답이 일치하는지 확인합니다.
                # 성공 시 True, 실패 시 False를 반환합니다.
                # 모든 단어가 배치되지 않으면 버튼이 비활성화됩니다.
                textbutton "확인 (Confirm)" action Return(note_player_answer == NOTE_PUZZLE_SOLUTION) sensitive (len(note_player_answer) == len(NOTE_PUZZLE_WORDS)) style "confirm_button"