## minigame_memory_puzzle.rpy

screen minigame_memory_puzzle():
    style_prefix "minigame_puzzle"
    
    # 게임 변수 설정
    # 순서대로 5개의 단서를 정의합니다. (실제 이미지 파일로 대체 필요)
    default clues = [
        "images/clue_1_note.png",
        "images/clue_2_gaze.png",
        "images/clue_3_recorder.png",
        "images/clue_4_heartbeat.png",
        "images/clue_5_ip.png"
    ]
    # 퍼즐 조각의 순서를 무작위로 섞습니다.
    default scrambled_clues = renpy.random.sample(clues, len(clues))
    default placed_clues = []
    default current_index = 0
    
    # 배경
    add minigame_bg
    
    # 퍼즐 조각
    frame:
        xalign 0.5
        yalign 0.3
        text "아래 조각들을 올바른 순서로 맞춰 기억을 완성하세요."
    
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        
        # for piece in scrambled_clues:
        #     button:
        #         idle piece
        #         hover Transform(piece, zoom=1.1)
        #         action [SetScreenVariable("placed_clues", placed_clues + [piece]), renpy.jump("check_puzzle_piece")]
    
    # 성공/실패 메시지
    if len(placed_clues) == 5:
        text "퍼즐이 완성되었다!" xalign 0.5 yalign 0.8
    elif len(placed_clues) > 0 and placed_clues[-1] != clues[len(placed_clues)-1]:
        text "무언가 잘못됐다... 다시 시작해야 해." xalign 0.5 yalign 0.8
        
    # 게임 메뉴 키로 종료 (실패)
    key "game_menu" action Return(False)

label check_puzzle_piece:
    if placed_clues[-1] == clues[len(placed_clues) - 1]:
        # 올바른 조각을 맞췄을 경우
        $ renpy.sound.play(sfx_puzzle_piece)
        if len(placed_clues) == 5:
            # 모든 조각을 올바르게 맞췄을 경우
            return True
        else:
            return
    else:
        # 잘못된 조각을 맞췄을 경우
        $ placed_clues = []
        $ renpy.sound.play(sfx_tear)
        return