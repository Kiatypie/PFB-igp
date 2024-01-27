from pathlib import Path
import csv


def read_csv_with_csv_module(file_path):
    '''
    - Read and parse the CSV file for analysis
    '''
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) 

        profits_and_loss = []
        for row in reader:
           
            profits_and_loss.append([row[0], row[1], row[2], row[3], row[4]])

    return profits_and_loss


def analyze_trend_basic_manual(net_profit_changes, data):
    '''
    - Analyses the trend in net profit changes to see if it has a 
      decreasing, increasing or fluctuating trend
    - Increasing or decreasing trend: States the trend with highest increase/decrease amount and the day 
    - Fluctuating trend: States the trend, highlighting the top 3 deficits.
    '''
    increasing = True
    decreasing = True

    for change in net_profit_changes:
        if change <= 0:
            increasing = False
        if change >= 0:
            decreasing = False

    if increasing:
        max_increase = max(net_profit_changes)
        day_index = net_profit_changes.index(max_increase)
        day_of_max_increase = data[day_index + 1][0]
        return f"Increasing trend. Highest increase: SGD {max_increase} on Day {day_of_max_increase}."
    elif decreasing:
        max_decrease = min(net_profit_changes)
        day_index = net_profit_changes.index(max_decrease)
        day_of_max_decrease = data[day_index + 1][0]
        return f"Decreasing trend. Highest decrease: SGD {max_decrease} on Day {day_of_max_decrease}."
    else:
        deficits = [(change, data[i+1][0]) for i, change in enumerate(net_profit_changes) if change < 0]
        for i in range(len(deficits)):
            for j in range(len(deficits)-i-1):
                if deficits[j][0] > deficits[j+1][0]:
                    deficits[j], deficits[j+1] = deficits[j+1], deficits[j]
        top_3_deficits = deficits[:3]
        return f"Fluctuating trend. Top 3 deficits (Amount in SGD, Day): {top_3_deficits}"


def list_deficits(net_profit_changes, data):
    '''
    - list all days and amounts when a deficit occurs
    '''
    output = ""
    for i, change in enumerate(net_profit_changes):
        if change < 0:
            day = data[i+1][0]  
            output += f"[CASH DEFICIT] DAY: {day}, AMOUNT: SGD {-change}\n"
    return output


def print_top_3_deficits(net_profit_changes, data):
    '''
    - Lists the top 3 deficits in an increasing order format
    '''
    deficits = [(change, data[i+1][0]) for i, change in enumerate(net_profit_changes) if change < 0]
    for i in range(len(deficits)):
        for j in range(len(deficits)-i-1):
            if deficits[j][0] > deficits[j+1][0]:
                deficits[j], deficits[j+1] = deficits[j+1], deficits[j]
    top_3_deficits = deficits[:3]

    output = ""
    deficit_labels = ["[HIGHEST CASH DEFICIT]", "[2ND HIGHEST CASH DEFICIT]", "[3RD HIGHEST CASH DEFICIT]"]
    for i, deficit in enumerate(top_3_deficits):
        output += f"{deficit_labels[i]} DAY: {deficit[1]}, AMOUNT: SGD {-deficit[0]}\n"
    return output


def process_and_print_profit_loss_data(file_path):
    '''
    - Combines all previous functions
    - Calculates the trend in net profit from profit and loss
    - FLuctuating: lists out the days it occurs and the top 3 days and amounts
    '''
    data = read_csv_with_csv_module(file_path)
    net_profit_changes = [int(data[i][4]) - int(data[i-1][4]) for i in range(1, len(data))]
    trend_result = analyze_trend_basic_manual(net_profit_changes, data)
    top_3_deficits = print_top_3_deficits(net_profit_changes, data)
    list_of_deficits = list_deficits(net_profit_changes, data)      
    return trend_result + "\n" + top_3_deficits + "\n" + list_of_deficits





