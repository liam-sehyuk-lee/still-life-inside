# minigame_memory_puzzle.rpy

init python:
    # --- 미니게임 설정 ---
    # 클루 이미지 정의 (floor_1.rpy에 정의된 것을 가정)
    # image clue_1_note = "images/minigame/clue_1_note.png"
    # image clue_2_gaze = "images/minigame/clue_2_gaze.png"
    # image clue_3_recorder = "images/minigame/clue_3_recorder.png"
    # image clue_4_heartbeat = "images/minigame/clue_4_heartbeat.png"
    # image clue_5_ip = "images/minigame/clue_5_ip.png"

    # --- 미니게임 변수 ---
    puzzle_pieces = []
    player_solution = []
    current_clue_images = []
    minigame_state = "playing" # "playing", "win", "lose"
    minigame_result = False

    def setup_puzzle():
        global puzzle_pieces, player_solution, current_clue_images, minigame_state, minigame_result

        # 퍼즐의 정답 순서를 설정
        puzzle_pieces = [
            "clue_1_note",
            "clue_2_gaze",
            "clue_3_recorder",
            "clue_4_heartbeat",
            "clue_5_ip"
        ]
        
        # 플레이어가 클릭할 이미지들을 무작위로 섞음
        current_clue_images = puzzle_pieces[:]
        renpy.random.shuffle(current_clue_images)
        
        player_solution = []
        minigame_state = "playing"
        minigame_result = False

    def click_piece(piece_name):
        global player_solution, current_clue_images, minigame_state, minigame_result
        
        if minigame_state != "playing":
            return
            
        # 선택한 조각을 정답 리스트에 추가하고, 클릭 가능 목록에서 제거
        player_solution.append(piece_name)
        current_clue_images.remove(piece_name)
        
        # 모든 조각을 선택했을 때만 정답을 확인
        if len(player_solution) == len(puzzle_pieces):
            if player_solution == puzzle_pieces:
                minigame_state = "win"
                minigame_result = True
            else:
                minigame_state = "lose"
                minigame_result = False
                
        renpy.restart_interaction()

screen minigame_puzzle():
    modal True
    
    on "show":
        action [
            Function(setup_puzzle)
        ]

    # 게임 상태에 따라 다른 동작을 실행하는 타이머
    timer 0.01 repeat True:
        if minigame_state == "win" or minigame_state == "lose":
            action Return(minigame_result)
        else:
            action NullAction()
            
    add "black" alpha 0.7
    vbox:
        align (0.5, 0.5)
        spacing 20
        
        # 퍼즐 조각을 배치할 공간
        hbox:
            align (0.5, 0.5)
            spacing 10
            for piece in player_solution:
                add piece at puzzle_piece_style
                
        text "기억의 조각을 올바른 순서로 맞춰보세요.":
            style "minigame_guide_text"

        # 플레이어가 클릭할 이미지들
        hbox:
            align (0.5, 0.5)
            spacing 10
            for piece in current_clue_images:
                button:
                    action Function(click_piece, piece)
                    add piece at shuffled_piece_style

transform puzzle_piece_style:
    size (150, 150)
    
transform shuffled_piece_style:
    size (150, 150)