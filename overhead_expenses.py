import csv
from pathlib import Path

# Function to read and parse the CSV file
def read_csv_with_csv_module(file_path):
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)  # Read header

        overheads_data = []
        for row in reader:
            category, overhead = row
            overheads_data.append((category, float(overhead)))

    return header, overheads_data

# Function to analyze the highest overhead category
def analyze_highest_overhead(overheads_data):
    total_overhead = sum(overhead for _, overhead in overheads_data)

    highest_overhead_category = None
    highest_overhead_amount = 0
    for category, overhead in overheads_data:
        if overhead > highest_overhead_amount:
            highest_overhead_category = category
            highest_overhead_amount = overhead

    highest_overhead_percentage = (highest_overhead_amount / total_overhead) * 100

    return highest_overhead_category, highest_overhead_percentage


# process_and_print_highest_overhead_data(fp)
def process_and_print_highest_overhead_data(file_path):
    _, overheads_data = read_csv_with_csv_module(file_path)
    highest_overhead_category, highest_overhead_percentage = analyze_highest_overhead(overheads_data)
    return f"[HIGHEST OVERHEAD] EXPENSE: {highest_overhead_category}, PERCENTAGE: {highest_overhead_percentage}%\n"






