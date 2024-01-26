from pathlib import Path
from profits_and_loss import process_and_print_profit_loss_data
from cash_on_hand import process_and_print_cash_on_hand_data
from overhead_expenses import process_and_print_highest_overhead_data


def main(): 
    print('  CASH ON HAND  ')
    process_and_print_cash_on_hand_data(Path.cwd() / "cash-on-hand-sgd D11-90.csv")
    print('  PROFIT AND LOSS  ')
    process_and_print_profit_loss_data(Path.cwd() / "profit-and-loss-sgd D11-90.csv")
    print('  OVERHEAD EXPENSE  ')
    process_and_print_highest_overhead_data(Path.cwd() / "overheads-day-90.csv")

main()

print("donuts")
print("lol")











   