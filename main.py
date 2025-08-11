from cox import Cox
from tob import Tob
from ge_prices import fetch_ge_prices
#from raids.cox import Cox
raid_select = input("Which raid you want to simulate:(1: CoX, 2: ToB) ")
# tob = Tob()
# n = input("Enter the number of tob completions to simulate: ").strip()
# n = int(n) if n.isdigit() else 100
# tob.roll_multiple_times(n)

def simulate_cox():
    user_input = input("Enter points: ")
    amounts_roll = input("enter total amount ")
    try:
        user_input = int(user_input)
        amounts_roll = int(amounts_roll)
        # Try converting to int
        cox = Cox(user_input)
        cox.roll_multiple_times(amounts_roll)
        cox.print_summary()
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
# tob.print_summary()

def simulate_tob():
    amounts_roll = input("Enter total amount ")
    try:
        amounts_roll = int(amounts_roll)
        # Try converting to int
        tob = Tob()
        tob.roll_multiple_times(amounts_roll)
        tob.print_summary()
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

match raid_select:
    case "1":
        simulate_cox()
    case "2":
        simulate_tob()
    case _:
        None
        
# while True:
#     user_input = input("Enter points: ")
#     amounts_roll = input("enter total amount ")
#     try:
#         user_input = int(user_input)
#         amounts_roll = int(amounts_roll)
#         # Try converting to int
#         cox = Cox(user_input)
#         cox.roll_multiple_times(amounts_roll)
#         cox.print_summary()
#         break  # Exit loop
#     except ValueError:
#         print("Invalid input. Please enter a valid integer.")
     
# fetch_ge_prices()
