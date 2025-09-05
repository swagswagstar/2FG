import pandas as pd
import os

def calculate_two_point_stats(row):
    two_fgm = row['FGM'] - row['3PM']
    two_fga = row['FGA'] - row['3PA']
    two_pt_pct = (two_fgm / two_fga * 100) if two_fga > 0 else 0
    return pd.Series({
        "Player": row['Player'],
        "2FGM": two_fgm,
        "2FGA": two_fga,
        "2PT%": round(two_pt_pct, 2)
    })

def manual_entry():
    player = input("Enter player name: ")
    fgm = int(input("Enter total FGM: "))
    fga = int(input("Enter total FGA: "))
    three_pm = int(input("Enter 3PM: "))
    three_pa = int(input("Enter 3PA: "))

    stats = calculate_two_point_stats({
        'Player': player, 'FGM': fgm, 'FGA': fga, '3PM': three_pm, '3PA': three_pa
    })
    print("\n--- 2PT Stats ---")
    print(f"Player: {stats['Player']}")
    print(f"2FGM: {stats['2FGM']}")
    print(f"2FGA: {stats['2FGA']}")
    print(f"2PT%: {stats['2PT%']}%")

def file_import():
    file_path = input("Enter spreadsheet path: ").strip().strip('"')
    if not os.path.exists(file_path):
        print("File does not exist!")
        return
    
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.csv':
        df = pd.read_csv(file_path)
    elif ext in ['.xls', '.xlsx']:
        # use appropriate engine depending on file type
        engine = 'xlrd' if ext == '.xls' else 'openpyxl'
        df = pd.read_excel(file_path, engine=engine)
    else:
        print("Unsupported file type!")
        return
    
    results = df.apply(calculate_two_point_stats, axis=1)
    output_file = "2pt_leaderboard.csv"
    results.to_csv(output_file, index=False)
    print(f"✅ Saved results to {output_file}")

if __name__ == "__main__":
    choice = input("Choose mode:\n1. Manual entry\n2. Import spreadsheet\nEnter 1 or 2: ")
    if choice == '1':
        manual_entry()
    elif choice == '2':
        file_import()
    else:
        print("Invalid choice!")