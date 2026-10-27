
from abc import ABC, abstractmethod


class Flight:
    def __init__(self, code, airline, source, destination, seats, fare):
        self.code = code
        self.airline = airline
        self.source = source
        self.destination = destination
        self.seats = seats
        self.fare = fare

    def display_flight(self):
        print(self.code, self.airline, self.source, "to",
              self.destination, "Seats:", self.seats,
              "Fare: Rs.", self.fare)

    def book_seats(self, tickets):
        if tickets <= self.seats:
            self.seats -= tickets
            return True
        return False


class Passenger(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_discount(self):
        pass

    @abstractmethod
    def get_type(self):
        pass


class RegularPassenger(Passenger):
    def get_discount(self):
        return 0

    def get_type(self):
        return "Regular"


class StudentPassenger(Passenger):
    def get_discount(self):
        return 0.10

    def get_type(self):
        return "Student"


class Booking:
    def __init__(self, booking_id, flight, passenger, tickets):
        self.booking_id = booking_id
        self.flight = flight
        self.passenger = passenger
        self.tickets = tickets

        self.subtotal = flight.fare * tickets
        self.discount = self.subtotal * passenger.get_discount()
        self.total = self.subtotal - self.discount

    def show_booking(self):
        print("\nBooking ID:", self.booking_id)
        print("Passenger:", self.passenger.name)
        print("Age:", self.passenger.age)
        print("Passenger Type:", self.passenger.get_type())
        print("Flight Code:", self.flight.code)
        print("Airline:", self.flight.airline)
        print("Route:", self.flight.source, "to",
              self.flight.destination)
        print("Tickets:", self.tickets)
        print("Base Fare:", self.flight.fare)
        print("Subtotal:", self.subtotal)
        print("Discount:", self.discount)
        print("Final Amount: Rs.", self.total)


class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("PN101", "Kiran Air", "Pune", "Delhi", 20, 4000),
            Flight("MB202", "Sky India", "Mumbai", "Bengaluru", 15, 5000),
            Flight("PN303", "Air Connect", "Pune", "Hyderabad", 25, 3500)
        ]

        self.bookings = []
        self.booking_number = 1001

    def view_flights(self):
        print("\nAvailable Flights")
        print("#" * 60)

        for flight in self.flights:
            flight.display_flight()

    def find_flight(self, code):
        for flight in self.flights:
            if flight.code == code.upper():
                return flight
        return None

    def calculate_fare(self, flight, passenger, tickets):
        subtotal = flight.fare * tickets
        discount = subtotal * passenger.get_discount()
        total = subtotal - discount
        return subtotal, discount, total

    def book_flight(self):
        self.view_flights()

        code = input("\nEnter flight code: ").strip()
        flight = self.find_flight(code)

        if flight is None:
            print("Invalid flight code.")
            return

        name = input("Enter passenger name: ").strip()

        try:
            age = int(input("Enter passenger age: "))
            passenger_type = input(
                "Passenger type (Regular/Student): "
            ).strip().lower()
            tickets = int(input("Enter number of tickets: "))
        except ValueError:
            print("Please enter valid numbers for age and tickets.")
            return

        if name == "":
            print("Passenger name cannot be blank.")
            return

        if age <= 0:
            print("Age must be greater than zero.")
            return

        if tickets <= 0:
            print("Tickets must be greater than zero.")
            return

        if passenger_type not in ["regular", "student"]:
            print("Invalid passenger type.")
            return

        if tickets > flight.seats:
            print("Not enough seats available.")
            return

        if passenger_type == "student":
            passenger = StudentPassenger(name, age)
        else:
            passenger = RegularPassenger(name, age)

        subtotal, discount, total = self.calculate_fare(
            flight, passenger, tickets
        )

        print("\nSubtotal: Rs.", subtotal)
        print("Discount: Rs.", discount)
        print("Final Fare: Rs.", total)

        confirm = input("Confirm booking? (yes/no): ").strip().lower()

        if confirm != "yes":
            print("Booking cancelled.")
            return

        if flight.book_seats(tickets):
            booking_id = "BK" + str(self.booking_number)

            booking = Booking(
                booking_id, flight, passenger, tickets
            )

            self.bookings.append(booking)
            self.booking_number += 1

            print("\nBooking confirmed!")
            booking.show_booking()
        else:
            print("Booking failed. Not enough seats.")

    def view_booking(self):
        if len(self.bookings) == 0:
            print("No confirmed bookings found.")
        else:
            self.bookings[-1].show_booking()

    def run(self):
        print("Welcome to Kiran Air Booking")

        while True:
            print("\n1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.view_flights()
            elif choice == "2":
                self.book_flight()
            elif choice == "3":
                self.view_booking()
            elif choice == "4":
                print("Thank you for using Kiran Air Booking!")
                break
            else:
                print("Invalid choice. Please try again.")


system = FlightBookingSystem()
system.run()
