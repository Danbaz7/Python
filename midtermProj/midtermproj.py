'''
INF360 - Programming in Python

Assignment #Midterm Project
Author: Daniel Obazee
'''


"""
FREELANCE PORTFOLIO & EARNINGS MANAGER
This program tracks various freelance clients, their set hourly rates, 
and hours worked to provide a financial overview of a project portfolio.
"""

# Data Structure: { 'Client Name': [Hourly_Rate, Total_Hours_Worked] }
portfolio = {
    "Tech Corp": [55.0, 10],
    "Design Studio": [40.0, 5]
}

def show_summary():
    """Iterates through the dictionary to display clients and calculate totals."""
    print("\n--- CURRENT PORTFOLIO SUMMARY ---")
    grand_total = 0
    
    if not portfolio:
        print("Your portfolio is currently empty.")
    else:
        for client, data in portfolio.items():
            rate, hours = data
            earnings = rate * hours
            grand_total += earnings
            print(f"Client: {client} | Rate: ${rate}/hr | Hours: {hours} | Total: ${earnings:.2f}")
    
    print(f"---------------------------------")
    print(f"TOTAL PORTFOLIO VALUE: ${grand_total:.2f}")

def add_client():
    """Adds a new client or updates an existing one with input validation."""
    client_name = input("\nEnter the client or project name: ").strip().title()
    
    # Error handling for the hourly rate
    try:
        rate_input = input(f"Enter hourly rate for {client_name}: ")
        rate = float(rate_input)
        if rate <= 0:
            raise ValueError("Rate must be positive.")
    except ValueError:
        print(f"!! Error: '{rate_input}' is not a valid number.")
        print("Next Move: Please enter a numeric value (e.g., 25 or 50.50). Do not include '$'.")
        return

    # Error handling for hours
    try:
        hours_input = input(f"Enter initial hours worked for {client_name}: ")
        hours = float(hours_input)
        if hours < 0:
            raise ValueError("Hours cannot be negative.")
    except ValueError:
        print(f"!! Error: '{hours_input}' is not a valid hour count.")
        print("Next Move: Please enter a whole number or decimal (e.g., 8 or 1.5).")
        return

    # Store in the dictionary
    portfolio[client_name] = [rate, hours]
    print(f"Success: {client_name} added to portfolio.")

def update_hours():
    """Adds additional hours to an existing client's tally."""
    client_name = input("\nWhich client are you adding hours to? ").strip().title()
    
    if client_name in portfolio:
        try:
            new_hours_input = input(f"How many new hours to add for {client_name}? ")
            new_hours = float(new_hours_input)
            
            # Update the list index for hours
            portfolio[client_name][1] += new_hours
            print(f"Success: Added {new_hours} hours to {client_name}.")
            
        except ValueError:
            print(f"!! Error: '{new_hours_input}' is not a valid number.")
            print("Next Move: Please enter a numeric value for the hours worked.")
    else:
        print(f"!! Error: Client '{client_name}' not found.")
        print("Next Move: Use 'V' to view current clients or 'A' to add this client first.")

def main():
    """Main menu loop for the program."""
    print("Welcome to the Freelance Earnings Manager.")
    
    while True:
        print("\n[V]iew Summary | [A]dd/Set Client | [U]pdate Hours | [Q]uit")
        choice = input("Select an option: ").upper().strip()
        
        if choice == 'V':
            show_summary()
        elif choice == 'A':
            add_client()
        elif choice == 'U':
            update_hours()
        elif choice == 'Q':
            print("Exiting Manager. Have a productive day!")
            break
        else:
            print(f"!! '{choice}' is not a valid command.")
            print("Next Move: Please enter V, A, U, or Q.")

if __name__ == "__main__":
    main()