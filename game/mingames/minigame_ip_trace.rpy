## minigame_ip_trace.rpy

screen minigame_ip_trace():
    style_prefix "minigame_ip"

    # 게임 변수 설정
    default dots = [
        ("192.168.1.1", 1), ("192.168.1.2", 2), ("192.168.1.3", 3),
        ("192.168.1.1", 4), ("192.168.1.2", 5), ("192.168.1.3", 6),
    ]
    default positions = {
        1: (0.2, 0.3), 2: (0.4, 0.6), 3: (0.6, 0.4),
        4: (0.8, 0.7), 5: (0.1, 0.8), 6: (0.9, 0.2),
    }
    default selected_dot = None
    default connected_pairs = []
    
    # 배경 이미지
    add bg_minigame

    # IP 주소 텍스트와 연결점 (dot) 버튼
    # fixed:
    #     for ip, dot_id in dots:
    #         $ pos_x, pos_y = positions[dot_id]
    #         button:
    #             xalign pos_x
    #             yalign pos_y
    #             idle "gui/ip_trace_dot.png"
    #             hover "gui/ip_trace_dot_highlight.png"
    #             selected "gui/ip_trace_dot_highlight.png"
    #             selected_idle "gui/ip_trace_dot_highlight.png"
    #             action [If(selected_dot is None, SetScreenVariable("selected_dot", dot_id)), If(selected_dot is not None, Function(renpy.jump, "check_connection", dot_id))]
    #         text ip xalign pos_x yalign pos_y - 0.05
    
    # # 연결된 선 그리기
    # canvas:
    #     for dot1, dot2 in connected_pairs:
    #         $ x1, y1 = positions[dot1]
    #         $ x2, y2 = positions[dot2]
    #         line (x1 * 1920, y1 * 1080, x2 * 1920, y2 * 1080) color "#ffffff" width 5
            
    # 게임 메뉴 키로 미니게임 종료 (실패)
    key "game_menu" action Return(False)

label check_connection(new_dot_id):
    $ new_dot_ip = dots[new_dot_id-1][0]
    $ old_dot_ip = dots[selected_dot-1][0]
    
    # 이미 연결된 쌍인지 확인
    $ is_already_connected = False
    
    python:
        for p in connected_pairs:
            if (p[0] == selected_dot and p[1] == new_dot_id) or (p[1] == selected_dot and p[0] == new_dot_id):
                is_already_connected = True
                break
    
    if new_dot_ip == old_dot_ip and not is_already_connected:
        $ connected_pairs.append((selected_dot, new_dot_id))
        $ renpy.sound.play(sfx_line_match)
    
    $ selected_dot = None

    # 성공 조건 확인
    if len(connected_pairs) == len(dots) / 2:
        return True
    
    return