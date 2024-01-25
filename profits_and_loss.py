from pathlib import Path
import csv

# Function to read and parse the CSV file using csv module and Path
def read_csv_with_csv_module(file_path):
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        profits_and_loss = []
        for row in reader:
            # Append the relevant data to the profits_and_loss list
            profits_and_loss.append([row[0], row[1], row[2], row[3], row[4]])

    return profits_and_loss

# Function to analyze the trend in net profit changes without using all(), sorted(), or lambda
def analyze_trend_basic_manual(net_profit_changes, data):
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
        return f"Fluctuating trend. Top 3 deficits: {top_3_deficits}"

# Function to list all days and amounts when a deficit occurs
def list_deficits(net_profit_changes, data):
    for i, change in enumerate(net_profit_changes):
        if change < 0:
            day = data[i+1][0]  # Day is in the next row (i+1) and first column
            print(f"[CASH DEFICIT] DAY: {day}, AMOUNT: SGD {-change}")

# Function to print the top 3 deficits in the specified format
def print_top_3_deficits(net_profit_changes, data):
    deficits = [(change, data[i+1][0]) for i, change in enumerate(net_profit_changes) if change < 0]
    for i in range(len(deficits)):
        for j in range(len(deficits)-i-1):
            if deficits[j][0] > deficits[j+1][0]:
                deficits[j], deficits[j+1] = deficits[j+1], deficits[j]
    top_3_deficits = deficits[:3]

    deficit_labels = ["[HIGHEST CASH DEFICIT]", "[2ND HIGHEST CASH DEFICIT]", "[3RD HIGHEST CASH DEFICIT]"]
    for i, deficit in enumerate(top_3_deficits):
        print(f"{deficit_labels[i]} DAY: {deficit[1]}, AMOUNT: SGD {-deficit[0]}")


def process_and_print_profit_loss_data(file_path):
    data = read_csv_with_csv_module(file_path)
    net_profit_changes = [int(data[i][4]) - int(data[i-1][4]) for i in range(1, len(data))]
    trend_result = analyze_trend_basic_manual(net_profit_changes, data)
    print(trend_result)
    print_top_3_deficits(net_profit_changes, data)
    list_deficits(net_profit_changes, data)





