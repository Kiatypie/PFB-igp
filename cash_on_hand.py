from pathlib import Path
import csv


def read_csv_with_csv_module(file_path):
    '''
    - Read and parse CSV file for analysis
    '''
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        cash_on_hand = []
        for row in reader:
            cash_on_hand.append([row[0], row[1]])  

    return cash_on_hand


def compute_cash_on_hand_changes(cash_on_hand):
    '''
    - Computes the difference in cash on hand each day
    '''
    changes = []
    for i in range(1, len(cash_on_hand)):
        change = int(cash_on_hand[i][1]) - int(cash_on_hand[i-1][1])
        changes.append(change)
    return changes

def analyze_cash_on_hand_trend(changes, cash_on_hand):
    '''
     - Analyses the trend in cash on hand to see if it has a 
      decreasing, increasing or fluctuating trend
    - Increasing or decreasing trend: States the trend with highest increase/decrease amount and the day 
    - Fluctuating trend: States the trend, highlighting the top 3 deficits.
    '''
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
        return f"Fluctuating trend. Top 3 deficits (Amount in SGD, Day): {top_3_deficits}"


def print_top_3_deficits(cash_on_hand_changes, cash_on_hand):
    '''
    - Lists the top 3 deficits in an increasing order format
    '''
    deficits = [(change, cash_on_hand[i + 1][0]) for i, change in enumerate(cash_on_hand_changes) if change < 0]
    for i in range(len(deficits)):
        for j in range(len(deficits) - i - 1):
            if deficits[j][0] > deficits[j + 1][0]:
                deficits[j], deficits[j + 1] = deficits[j + 1], deficits[j]
    top_3_deficits = deficits[:3]

    deficit_labels = ["[HIGHEST CASH DEFICIT]", "[2ND HIGHEST CASH DEFICIT]", "[3RD HIGHEST CASH DEFICIT]"]
    output = ""
    for i, deficit in enumerate(top_3_deficits):
        output += f"{deficit_labels[i]} DAY: {deficit[1]}, AMOUNT: SGD {-deficit[0]}\n"
    return output


def list_deficits(changes, cash_on_hand):
    '''
    - list all days and amounts when a deficit occurs
    '''
    output = ""
    for i, change in enumerate(changes):
        if change < 0:
            day = cash_on_hand[i+1][0]  
            output += f"[CASH DEFICIT] DAY: {day}, AMOUNT: SGD {-change}\n"
    return output

def process_and_print_cash_on_hand_data(file_path):
    '''
    - Combines all previous functions
    - Calculates the trend in cash on hand
    - FLuctuating: lists out the days it occurs and the top 3 days and amounts
    '''
    cash_on_hand_data = read_csv_with_csv_module(file_path)
    cash_on_hand_changes = compute_cash_on_hand_changes(cash_on_hand_data)
    cash_on_hand_result = analyze_cash_on_hand_trend(cash_on_hand_changes, cash_on_hand_data)
    top_3_deficits = print_top_3_deficits(cash_on_hand_changes, cash_on_hand_data) 
    list_of_deficits = list_deficits(cash_on_hand_changes, cash_on_hand_data)       
    return cash_on_hand_result + "\n" + top_3_deficits + "\n" + list_of_deficits


