def black_flag():
    pirating_lasts_days = int(input())
    plunder_for_day = int(input())
    expected_plunder = float(input())
    total_plunder = 0

    for day in range(1, pirating_lasts_days + 1):
        total_plunder += plunder_for_day

        if day % 3 == 0:
            total_plunder += (plunder_for_day / 2)

        if day % 5 == 0:
            total_plunder -= (total_plunder * 0.3)

    if total_plunder >= expected_plunder:
        print(f"Ahoy! {total_plunder:.2f} plunder gained.")
    else:
        percent_of_plunder = (total_plunder / expected_plunder) * 100
        print(f"Collected only {percent_of_plunder:.2f}% of the plunder.")


black_flag()
