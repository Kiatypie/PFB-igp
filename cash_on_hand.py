from pathlib import Path
import csv
#This function reads and processes the CSV file 
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
#This function computes the difference in cash on hand on each day
def compute_cash_on_hand_changes(cash_on_hand):
    '''
    - Computes the difference in cash on hand each day
    '''
    changes = []
    for day_index in range(1, len(cash_on_hand)):
        daily_change = int(cash_on_hand[day_index][1]) - int(cash_on_hand[day_index - 1][1])
        changes.append(daily_change)
    return changes
#This functon analyses the trend of cash on hand pointing out the prominent days of data
def analyze_cash_on_hand_trend(changes, cash_on_hand):
    '''
     - Analyses the trend in cash on hand to see if it has a 
      decreasing, increasing or fluctuating trend
    - Increasing or decreasing trend: States the trend with highest increase/decrease amount and the day 
    - Fluctuating trend: States the trend, highlighting the top 3 deficits.
    '''
    increasing = True
    decreasing = True

    for daily_change in changes:
        if daily_change <= 0:
            increasing = False
        if daily_change >= 0:
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
        deficits = [(daily_change, cash_on_hand[day_index + 1][0]) for day_index, daily_change in enumerate(changes) if daily_change < 0]
        
        for deficit_index in range(len(deficits)):
            for next_index in range(len(deficits) - deficit_index - 1):
                if deficits[next_index][0] > deficits[next_index + 1][0]:
                    
                    deficits[next_index], deficits[next_index + 1] = deficits[next_index + 1], deficits[next_index]
        top_3_deficits = deficits[:3]
        return f"Fluctuating trend. Top 3 deficits (Amount in SGD, Day): {top_3_deficits}"
#This function lists the top 3 deficits in accordance to the fluctuating trend
def print_top_3_deficits(cash_on_hand_changes, cash_on_hand):
    '''
    - Lists the top 3 deficits in an increasing order format
    '''
    deficits = [(daily_change, cash_on_hand[day_index + 1][0]) for day_index, daily_change in enumerate(cash_on_hand_changes) if daily_change < 0]
    
    for deficit_index in range(len(deficits)):
        for next_index in range(len(deficits) - deficit_index - 1):
            if deficits[next_index][0] > deficits[next_index + 1][0]:
                deficits[next_index], deficits[next_index + 1] = deficits[next_index + 1], deficits[next_index]
    top_3_deficits = deficits[:3]

    deficit_labels = ["[HIGHEST CASH DEFICIT]", "[2ND HIGHEST CASH DEFICIT]", "[3RD HIGHEST CASH DEFICIT]"]
    output = ""
    for deficit_rank, deficit in enumerate(top_3_deficits):
        output += f"{deficit_labels[deficit_rank]} DAY: {deficit[1]}, AMOUNT: SGD {-deficit[0]}\n"
    return output
#This function adds the lisiting of all days and amounts when the deficit occurs, also in accordamce with the fluctuating trend
def list_deficits(changes, cash_on_hand):
    '''
    - list all days and amounts when a deficit occurs
    '''
    output = ""
    for day_index, daily_change in enumerate(changes):
        if daily_change < 0:
            deficit_day = cash_on_hand[day_index + 1][0]  
            output += f"[CASH DEFICIT] DAY: {deficit_day}, AMOUNT: SGD {-daily_change}\n"
    return output
#This function combines all previous to return all the outputs of the functions in the code
def process_and_print_cash_on_hand_data(file_path):
    '''
    - Combines all previous functions
    - Calculates the trend in cash on hand
    - Fluctuating: lists out the days it occurs and the top 3 days and amounts
    '''
    cash_on_hand_data = read_csv_with_csv_module(file_path)
    cash_on_hand_changes = compute_cash_on_hand_changes(cash_on_hand_data)
    cash_on_hand_result = analyze_cash_on_hand_trend(cash_on_hand_changes, cash_on_hand_data)
    top_3_deficits_output = print_top_3_deficits(cash_on_hand_changes, cash_on_hand_data) 
    list_of_deficits_output = list_deficits(cash_on_hand_changes, cash_on_hand_data)       
    return cash_on_hand_result + "\n" + top_3_deficits_output + "\n" + list_of_deficits_output


