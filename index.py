def create_football_table():
    teams = ["نوید", "رامیار", "فرشید", "مهیار"]
    schedule = [
        ("نوید", "رامیار"),
        ("نوید", "فرشید"),
        ("نوید", "مهیار"),
        ("رامیار", "فرشید"),
        ("رامیار", "مهیار"),
        ("فرشید", "مهیار"),
    ]
    results = {}
    points = {team: 0 for team in teams}
    goal_difference = {team: 0 for team in teams}
    goals_scored = {team: 0 for team in teams}

    def input_results():
        print("\n--- جدول بازی ها ---")
        for i, match in enumerate(schedule):
            while True:
                try:
                    result_input = input(
                        f"بازی {i+1}: {match[0]}  vs  {match[1]} - نتیجه را وارد کنید (مثال: 3-1 برای برد {match[0]}): "
                    )
                    team1_goals, team2_goals = map(int, result_input.split("-"))
                    results[match] = (team1_goals, team2_goals)
                    break
                except ValueError:
                    print("فرمت نتیجه بازی اشتباه است. لطفا دوباره وارد کنید (مثال: 3-1).")

    def calculate_points():
        for match, result in results.items():
            team1, team2 = match
            team1_goals, team2_goals = result

            goals_scored[team1] += team1_goals
            goals_scored[team2] += team2_goals

            goal_difference[team1] += team1_goals - team2_goals
            goal_difference[team2] += team2_goals - team1_goals

            if team1_goals > team2_goals:
                points[team1] += 3
            elif team2_goals > team1_goals:
                points[team2] += 3
            else:
                points[team1] += 1
                points[team2] += 1

    def display_ranking():
        ranked_teams = sorted(
            teams,
            key=lambda team: (points[team], goal_difference[team], goals_scored[team]),
            reverse=True,
        )
        print("\n--- جدول رده بندی ---")
        print("{:<10} {:<8} {:<15} {:<15} {:<10}".format("رتبه", "تیم", "امتیاز", "تفاضل گل", "گل زده"))
        for rank, team in enumerate(ranked_teams, 1):
            print(
                "{:<10} {:<8} {:<15} {:<15} {:<10}".format(
                    rank, team, points[team], goal_difference[team], goals_scored[team]
                )
            )

    def display_schedule_table():
        print("\n--- جدول بازی ها ---")
        for i, match in enumerate(schedule):
            print(f"بازی {i+1}: {match[0]}  vs  {match[1]}")
        print("\nلطفا نتایج بازی ها را در جدول زیر وارد کنید:")


    display_schedule_table()
    input_results()
    calculate_points()
    display_ranking()

create_football_table()
