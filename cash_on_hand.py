from pathlib import Path
import csv

# Function to read and parse the CSV file using csv module and Path
def read_csv_with_csv_module(file_path):
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        cash_on_hand = []
        for row in reader:
            cash_on_hand.append([row[0], row[1]])  # Assuming Cash-On-Hand is the 2nd column

    return cash_on_hand

# Function to compute the difference in Cash-On-Hand
def compute_cash_on_hand_changes(cash_on_hand):
    changes = []
    for i in range(1, len(cash_on_hand)):
        change = int(cash_on_hand[i][1]) - int(cash_on_hand[i-1][1])
        changes.append(change)
    return changes

# Function to analyze the trend in Cash-On-Hand
def analyze_cash_on_hand_trend(changes, cash_on_hand):
    increasing = True
    decreasing = True

    for change in changes:
        if change <= 0:
            increasing = False
        if change >= 0:
            decreasing = False

    if increasing:
        max_increase = max(changes)
        day_of_max_increase = cash_on_hand[changes.index(max_increase) + 1][0]
        return f"Increasing trend. Highest increase: SGD {max_increase} on Day {day_of_max_increase}."
    elif decreasing:
        max_decrease = min(changes)
        day_of_max_decrease = cash_on_hand[changes.index(max_decrease) + 1][0]
        return f"Decreasing trend. Highest decrease: SGD {max_decrease} on Day {day_of_max_decrease}."
    else:
        deficits = [(change, cash_on_hand[i + 1][0]) for i, change in enumerate(changes) if change < 0]
        for i in range(len(deficits)):
            for j in range(len(deficits)-i-1):
                if deficits[j][0] > deficits[j+1][0]:
                    deficits[j], deficits[j+1] = deficits[j+1], deficits[j]
        top_3_deficits = deficits[:3]
        return f"Fluctuating trend. Top 3 deficits: {top_3_deficits}"

# Function to print the top 3 deficits in the specified format
def print_top_3_deficits(cash_on_hand_changes, cash_on_hand):
    deficits = [(change, cash_on_hand[i + 1][0]) for i, change in enumerate(cash_on_hand_changes) if change < 0]
    for i in range(len(deficits)):
        for j in range(len(deficits)-i-1):
            if deficits[j][0] > deficits[j+1][0]:
                deficits[j], deficits[j+1] = deficits[j+1], deficits[j]
    top_3_deficits = deficits[:3]

    deficit_labels = ["[HIGHEST CASH DEFICIT]", "[2ND HIGHEST CASH DEFICIT]", "[3RD HIGHEST CASH DEFICIT]"]
    for i, deficit in enumerate(top_3_deficits):
        print(f"{deficit_labels[i]} DAY: {deficit[1]}, AMOUNT: SGD {-deficit[0]}")

# Function to list all days and amounts when a deficit occurs
def list_deficits(changes, cash_on_hand):
    for i, change in enumerate(changes):
        if change < 0:
            day = cash_on_hand[i+1][0]  # Day is in the next row (i+1) and first column
            print(f"[CASH DEFICIT] DAY: {day}, AMOUNT: SGD {-change}")

def process_and_print_cash_on_hand_data(file_path):
    cash_on_hand_data = read_csv_with_csv_module(file_path)
    cash_on_hand_changes = compute_cash_on_hand_changes(cash_on_hand_data)
    cash_on_hand_result = analyze_cash_on_hand_trend(cash_on_hand_changes, cash_on_hand_data)
    print(cash_on_hand_result)
    print_top_3_deficits(cash_on_hand_changes, cash_on_hand_data)
    list_deficits(cash_on_hand_changes, cash_on_hand_data)


