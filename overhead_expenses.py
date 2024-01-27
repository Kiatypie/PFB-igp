import csv
from pathlib import Path

#This function reads and processes the CSV file
def read_csv_with_csv_module(file_path):
    '''
    - Read and parse CSV file for analysis
    '''
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)  

        overheads_data = []
        for row in reader:
            category, overhead = row
            overheads_data.append((category, float(overhead)))

    return header, overheads_data

#This function identifies the highest overhead expense category and the respective percentage
def analyze_highest_overhead(overheads_data):
    '''
    - Identifies higest overhead expense category expense and respective percentage
    '''
    total_overhead = sum(overhead for _, overhead in overheads_data)

    highest_overhead_category = None
    highest_overhead_amount = 0
    for category, overhead in overheads_data:
        if overhead > highest_overhead_amount:
            highest_overhead_category = category
            highest_overhead_amount = overhead

    highest_overhead_percentage = (highest_overhead_amount / total_overhead) * 100

    return highest_overhead_category, highest_overhead_percentage


#This function combies all the previous functions into one
def process_and_print_highest_overhead_data(file_path):
    '''
    - Combines all previous functions
    - Calculates the highest overhead expense 
    - identification of the overhead expense as well as its respective percentage value
    '''
    _, overheads_data = read_csv_with_csv_module(file_path)
    highest_overhead_category, highest_overhead_percentage = analyze_highest_overhead(overheads_data)
    return f"[HIGHEST OVERHEAD] EXPENSE: {highest_overhead_category}, PERCENTAGE: {highest_overhead_percentage}%\n"






