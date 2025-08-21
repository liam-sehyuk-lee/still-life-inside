# minigame_ip_trace.rpy

init python:
    # --- 미니게임 설정 ---
    IP_TIME_LIMIT = 20.0
    WRONG_CLICK_PENALTY = 3.0 # 오답 클릭 시 시간 페널티 (초)
    COMMENTS_PER_ROW = 3      # 한 줄에 표시할 댓글 수
    TOTAL_COMMENTS = 9        # 전체 댓글 수 (3x3 그리드)
    
    # --- 미니게임 변수 ---
    ip_comments = [{'text': '', 'ip': '', 'is_target': False, 'is_clicked': False} for _ in range(TOTAL_COMMENTS)]
    target_ip = ""
    found_count = 0
    total_target_count = 0
    ip_timer = 0.0
    minigame_state = "playing" # "playing", "win", "lose"
    minigame_result = False
    
    def setup_comments():
        global ip_comments, target_ip, total_target_count, found_count, minigame_state
        
        ip_comments = []
        target_ip = ""
        total_target_count = 0
        found_count = 0
        minigame_state = "playing"
        
        # IP 주소 생성 방식 수정: 19x.16x.x.x 형식으로 생성
        def generate_ip_parts_list():
            return [
                f"19{renpy.random.randint(1,9)}",
                f"16{renpy.random.randint(1,9)}",
                f"{renpy.random.randint(1,9)}",
                f"{renpy.random.randint(1,9)}"
            ]
        
        target_ip_parts = generate_ip_parts_list()
        target_ip = '.'.join(target_ip_parts)

        # 정답 개수를 3 또는 4개로 고정
        TARGET_IP_COUNT = renpy.random.randint(3, 4)
        
        comment_texts = [
            "나는 괜찮아... 괜찮다고 했잖아...",
            "여긴 ZONE 12. 누구 있나요?",
            "함께 저항합시다.",
            "나도 그들에게 사육당하고 있어.",
            "마치 모두의 목소리처럼 들리지만...",
            "어떤 소리가 들린다면 도망쳐.",
            "기억을 잃은 사람들이 많아.",
            "새로운 시작은 언제나 달콤해.",
            "이곳의 규칙은 절대 바뀌지 않아."
        ]
        
        ip_list = [target_ip] * TARGET_IP_COUNT
        
        # 오답 IP 생성 및 추가
        while len(ip_list) < TOTAL_COMMENTS:
            
            new_ip_parts = target_ip_parts[:]
            
            change_part_index = renpy.random.choice([0, 1, 2, 3])
            
            new_digit = str(renpy.random.randint(1, 9))
            
            while new_digit == new_ip_parts[change_part_index][-1]:
                new_digit = str(renpy.random.randint(1, 9))
            
            new_ip_parts[change_part_index] = new_ip_parts[change_part_index][:-1] + new_digit
            new_ip = '.'.join(new_ip_parts)
            
            if new_ip not in ip_list:
                ip_list.append(new_ip)
        
        renpy.random.shuffle(ip_list)
        
        total_target_count = ip_list.count(target_ip)
        
        for i in range(TOTAL_COMMENTS):
            is_target = (ip_list[i] == target_ip)
            ip_comments.append({
                'text': comment_texts[i % len(comment_texts)],
                'ip': ip_list[i],
                'is_target': is_target,
                'is_clicked': False
            })

    def minigame_ip_update():
        global ip_timer, minigame_state, minigame_result

        if minigame_state != "playing":
            return

        dt = 0.01
        ip_timer -= dt

        if ip_timer <= 0:
            minigame_result = False
            minigame_state = "lose"
            
        renpy.restart_interaction()

    def click_comment(index):
        global found_count, ip_timer, minigame_state, minigame_result
        
        if minigame_state != "playing":
            return
            
        comment = ip_comments[index]
        if comment['is_clicked']:
            return

        if comment['is_target']:
            comment['is_clicked'] = True
            found_count += 1
            if found_count >= total_target_count:
                minigame_state = "win"
                minigame_result = True
        else:
            ip_timer -= WRONG_CLICK_PENALTY
            if ip_timer < 0:
                ip_timer = 0
            
            setup_comments()
            
        renpy.restart_interaction()

screen minigame_ip():
    modal True
    
    on "show":
        action [
            Function(setup_comments),
            SetVariable("ip_timer", IP_TIME_LIMIT),
            SetVariable("minigame_state", "playing"),
            SetVariable("minigame_result", False)
        ]
    
    timer 0.01 repeat True action Function(minigame_ip_update)
    
    timer 0.01 repeat True:
        if minigame_state == "win" or minigame_state == "lose":
            action Return(minigame_result)
        else:
            action NullAction()
            
    add "black" alpha 0.7
    vbox:
        align (0.5, 0.5)
        spacing 20
        
        if minigame_state == "playing":
            text "모든 댓글 중 동일한 IP 주소를 사용하는 댓글들을 찾아 클릭하세요.":
                style "minigame_guide_text"
            text f"찾아야 할 IP: {target_ip}":
                style "minigame_guide_text"
            text f"남은 시간: [max(0, ip_timer):.1f]s":
                align (1.0, 0.5)
                style "minigame_timer_text"
        
        if minigame_state == "playing":
            grid 3 3:
                for i in range(TOTAL_COMMENTS):
                    vbox:
                        $ bg_color = "#222222" if ip_comments[i]['is_clicked'] else "#444444"
                        button:
                            background bg_color
                            padding (10, 10)
                            xsize 250
                            ysize 100
                            action Function(click_comment, i)
                            text ip_comments[i]['text']:
                                color "#ffffff"
                                size 24
                        text f"IP: {ip_comments[i]['ip']}":
                            color "#999999"
                            size 20