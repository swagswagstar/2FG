def calculate_two_point_stats(fgm, fga, three_pm, three_pa):
    two_fgm = fgm - three_pm
    two_fga = fga - three_pa
    two_pt_pct = (two_fgm / two_fga) * 100 if two_fga > 0 else 0
    return {
        "2FGM": two_fgm,
        "2FGA": two_fga,
        "2PT%": round(two_pt_pct, 2)
    }


if __name__ == "__main__":
    fgm = int(input("Enter total FGM: "))
    fga = int(input("Enter total FGA: "))
    three_pm = int(input("Enter 3PM: "))
    three_pa = int(input("Enter 3PA: "))

    stats = calculate_two_point_stats(fgm, fga, three_pm, three_pa)
    print("\n--- 2PT Stats ---")
    print(f"2FGM: {stats['2FGM']}")
    print(f"2FGA: {stats['2FGA']}")
    print(f"2PT%: {stats['2PT%']}%")
