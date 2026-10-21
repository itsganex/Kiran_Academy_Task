
import random

cab_rates = {
    1: ("Auto", 12),
    2: ("Sedan", 18),
    3: ("SUV", 25)
}

routes = {
    1: ("Pune Station", "Shivajinagar", 5),
    2: ("Pune Station", "Kothrud", 8),
    3: ("Pune Station", "Wakad", 10),
    4: ("Swargate", "Shivajinagar", 5),
    5: ("Swargate", "Kothrud", 8),
    6: ("Swargate", "Wakad", 10),
    7: ("Hinjawadi", "Shivajinagar", 5),
    8: ("Hinjawadi", "Kothrud", 8),
    9: ("Hinjawadi", "Wakad", 10)
}


def calculate_fare(rate, distance):
    return rate * distance


while True:
    print("\nWelcome to Your Cab")
    print("1. Book Ride")
    print("2. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nChoose Your Cab")

        for key, value in cab_rates.items():
            print(f"{key}. {value[0]} - Rs. {value[1]}/km")

        cab_choice = int(input("Enter cab choice: "))

        if cab_choice == 1:
            cab_name, rate = cab_rates[1]
        elif cab_choice == 2:
            cab_name, rate = cab_rates[2]
        elif cab_choice == 3:
            cab_name, rate = cab_rates[3]
        else:
            print("Invalid cab choice")
            continue

        print("\nAvailable Routes")

        for key, value in routes.items():
            source, destination, distance = value
            print(f"{key}. {source} to {destination} - {distance} km")

        route_choice = int(input("Enter route number: "))

        if route_choice == 1:
            source, destination, distance = routes[1]
        elif route_choice == 2:
            source, destination, distance = routes[2]
        elif route_choice == 3:
            source, destination, distance = routes[3]
        elif route_choice == 4:
            source, destination, distance = routes[4]
        elif route_choice == 5:
            source, destination, distance = routes[5]
        elif route_choice == 6:
            source, destination, distance = routes[6]
        elif route_choice == 7:
            source, destination, distance = routes[7]
        elif route_choice == 8:
            source, destination, distance = routes[8]
        elif route_choice == 9:
            source, destination, distance = routes[9]
        else:
            print("Invalid route choice")
            continue

        fare = calculate_fare(rate, distance)

        print("\nRide Details")
        print("Cab:", cab_name)
        print("Source:", source)
        print("Destination:", destination)
        print("Distance:", distance, "km")
        print("Rate: Rs.", rate, "/km")
        print("Total Fare: Rs.", fare)

        print("\n1. Confirm and Share OTP")
        print("2. Cancel Ride")

        booking_choice = int(input("Enter your choice: "))

        if booking_choice == 1:
            otp = random.randint(1000, 9999)

            print("Your OTP is:", otp)
            print("Cancellation is not allowed after OTP sharing")

            entered_otp = int(input("Enter your OTP: "))

            if entered_otp == otp:
                print("OTP verified successfully")
                print("Your ride is confirmed")
            else:
                print("Incorrect OTP")
                print("Booking verification failed")

        elif booking_choice == 2:
            print("Ride cancelled successfully")

        else:
            print("Invalid booking choice")

    elif choice == 2:
        print("Thanks for visiting. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
