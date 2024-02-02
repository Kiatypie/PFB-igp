from pathlib import Path 
from profits_and_loss import process_and_print_profit_loss_data 
from cash_on_hand import process_and_print_cash_on_hand_data 
from overhead_expenses import process_and_print_highest_overhead_data 
 
#This function runs the modularization of the individual programmes.
def main():  
    ''' 
    - Main function to process and print financial data. 
    - Processes data for each module: cash on hand, profit and loss, and overhead expenses 
    - Utilises modularisatio to run the consolidated function from each module 
    ''' 
    print('  CASH ON HAND  ') 
    process_and_print_cash_on_hand_data(Path.cwd() / "cash-on-hand-sgd D11-90.csv") 
    print('  PROFIT AND LOSS  ') 
    process_and_print_profit_loss_data(Path.cwd() / "profit-and-loss-sgd D11-90.csv") 
    print('  OVERHEAD EXPENSE  ') 
    process_and_print_highest_overhead_data(Path.cwd() / "overheads-day-90.csv") 
 
main() 
 
 
cash_on_hand_output =  process_and_print_cash_on_hand_data(Path.cwd() / "cash-on-hand-sgd D11-90.csv") 
profit_loss_output = process_and_print_profit_loss_data(Path.cwd() / "profit-and-loss-sgd D11-90.csv") 
overhead_expense_output = process_and_print_highest_overhead_data(Path.cwd() / "overheads-day-90.csv") 
def write_analysis_to_file(file_path, cash_on_hand_output, profit_loss_output, overhead_expense_output): 
    with open(file_path, 'w', encoding='utf-8') as file: 
        file.write("\nCASH ON HAND\n") 
        file.write(f"{cash_on_hand_output}") 
        file.write("\nPROFIT AND LOSS\n") 
        file.write(f"{profit_loss_output}") 
        file.write("\nOVERHEAD EXPENSES\n")
        file.write(f"{overhead_expense_output}") 
 
 
write_analysis_to_file("Summary_report.txt", cash_on_hand_output, profit_loss_output, overhead_expense_output) 