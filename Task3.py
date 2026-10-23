balance = 10000

print("Welcome to Kiran Bank")
print(f"Opening Balance: ₹{balance}")

while True:
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        print(f"Current Balance: ₹{balance}")

    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: "))

            if amount <= 0:
                print("Invalid amount. Please enter an amount greater than zero")
            else:
                balance += amount
                print("Deposit successful")
                print(f"Updated Balance: ₹{balance:.2f}")

        except ValueError:
            print("Invalid input. Please enter a valid number")

    elif choice == "3":
        try:
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Invalid amount. Please enter an amount greater than zero")
            elif amount > balance:
                print("Transaction failed: Insufficient balance")
                print(f"Current Balance: ₹{balance:.2f}")
            else:
                balance -= amount
                print("Withdrawal successful.")
                print(f"Updated Balance: ₹{balance:.2f}")

        except ValueError:
            print("Invalid input. Please enter a valid number")

    elif choice == "4":
        print("Thank you for banking with us. Goodbye")
        break

    else:
        print("Invalid choice. Please select an option from 1 to 4")
