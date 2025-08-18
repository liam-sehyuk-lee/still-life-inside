label call_minigame(game_name):
    $ minigame_result = False

    # 7층: 숨소리 참기
    if game_name == "breath":
        call minigame_breath from _minigame_breath_return
        $ minigame_result = _return

    # 6층: 찢어진 쪽지 맞추기
    elif game_name == "note":
        call minigame_note from _minigame_note_return
        $ minigame_result = _return

    # 5층: 시선 피하기
    elif game_name == "gaze":
        call minigame_gaze from _minigame_gaze_return
        $ minigame_result = _return

    # 4층: 주파수 맞추기
    elif game_name == "frequency":
        call minigame_frequency from _minigame_frequency_return
        $ minigame_result = _return

    # 3층: 심장박동 숨기기
    elif game_name == "heartbeat":
        call minigame_heartbeat from _minigame_heartbeat_return
        $ minigame_result = _return

    # 2층: IP 주소 추적
    elif game_name == "ip_trace":
        call minigame_ip_trace from _minigame_ip_trace_return
        $ minigame_result = _return

    # 1층: 기억의 퍼즐 완성하기
    elif game_name == "memory_puzzle":
        call minigame_memory_puzzle from _minigame_memory_puzzle_return
        $ minigame_result = _return

    return minigame_result