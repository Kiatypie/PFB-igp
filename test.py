from pathlib import Path
from profits_and_loss import process_and_print_profit_loss_data
from cash_on_hand import process_and_print_cash_on_hand_data
from overhead_expenses import process_and_print_highest_overhead_data

def write_analysis_to_file(file_path, cash_on_hand_output, profit_loss_output, overhead_expense_output):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("CASH ON HAND\n")
        file.write(cash_on_hand_output + "\n")
        file.write("\nPROFIT AND LOSS\n")
        file.write(profit_loss_output + "\n")
        file.write("\nOVERHEAD EXPENSE\n")
        file.write(overhead_expense_output + "\n")

def main():
    cash_on_hand_output = process_and_print_cash_on_hand_data(Path.cwd() / "cash-on-hand-sgd D11-90.csv")
    profit_loss_output = process_and_print_profit_loss_data(Path.cwd() / "profit-and-loss-sgd D11-90.csv")
    overhead_expense_output = process_and_print_highest_overhead_data(Path.cwd() / "overheads-day-90.csv")

    write_analysis_to_file("analysis_output.txt", cash_on_hand_output, profit_loss_output, overhead_expense_output)

if __name__ == "__main__":
    main()
