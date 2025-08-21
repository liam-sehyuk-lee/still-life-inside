label call_minigame(game_name):

    # 7층: 숨소리 참기
    if game_name == "breath":
        call screen minigame_breath
        return _return

    # 6층: 찢어진 쪽지 맞추기
    elif game_name == "note":
        call screen minigame_note
        return _return

    # 5층: 시선 피하기
    elif game_name == "gaze":
        call screen minigame_gaze
        return _return

    # 4층: 주파수 맞추기
    elif game_name == "frequency":
        call screen minigame_frequency
        return _return

    # 3층: 심장박동 숨기기
    elif game_name == "heartbeat":
        call screen minigame_heartbeat
        return _return

    # 2층: IP 주소 추적
    elif game_name == "ip_trace":
        call screen minigame_ip_trace
        return _return

    # 1층: 기억의 퍼즐 완성하기
    elif game_name == "memory_puzzle":
        call screen minigame_memory_puzzle
        return _return

    return False