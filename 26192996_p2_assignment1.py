import random
user_list = [["ahmad", "1234"]]
num_rows = 3
num_cols = 5
seats = [['O' for _ in range(num_cols)] for _ in range(num_rows)]


def display_seating_chart():
    print("Seating Chart:")
    for row in range(num_rows):
        for col in range(num_cols):
            print(seats[row][col], end=' ')
        print()


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in user_list:
        if user[0] == username and user[1] == password:
            print("Login successful!")
            return True

    print("Invalid username or password.")
    return False


def signup():
    username = input("Enter a new username: ")
    password = input("Enter a password: ")
    user_list.append([username, password])
    print("Sign up successful!")


def book_flight():
    print("HERE ARE THE AVAILABLE FLIGHTS")
    for idx, flight in enumerate(flightlist):
        print(idx, flight)

    while True:
        try:
            choice = int(input("Enter the number for the flight you want to choose: "))
            if 0 <= choice < len(flightlist):
                break
            else:
                print("Invalid flight number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    selected_flight = flightlist[choice]
    print(selected_flight)
    display_seating_chart()

    while True:
        try:
            row = int(input("Enter row number (1 to {}): ".format(num_rows))) - 1
            col = int(input("Enter seat number (1 to {}): ".format(num_cols))) - 1

            if 0 <= row < num_rows and 0 <= col < num_cols:
                if seats[row][col] == 'O':
                    booking_number = random.randint(1000, 9999)
                    seats[row][col] = 'X'

                    with open("bookings.txt", "a") as file:
                        file.write(f"Booking Number: {booking_number}\n")
                        file.write(f"Flight: {selected_flight}\n")
                        file.write(f"Row: {row + 1}\n")
                        file.write(f"Seat: {col + 1}\n\n")

                    print(f"Seat booked successfully! Your Booking Number is: {booking_number}")
                    return
                else:
                    print("Seat is already booked. Please select another seat.")
            else:
                print("Invalid row or column number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter valid row and column numbers.")

def cancel_flight():
    booking_number = input("Enter your booking number: ")

    with open("bookings.txt", "r") as file:
        lines = file.readlines()

    with open("bookings.txt", "w") as file:
        for i in range(0, len(lines), 5):
            if booking_number.strip() == lines[i].split(": ")[1].strip():
                flight = lines[i + 1].split(": ")[1].strip()
                row = int(lines[i + 2].split(": ")[1].strip()) - 1
                seat = int(lines[i + 3].split(": ")[1].strip()) - 1

                if seats[row][seat] == 'X':
                    seats[row][seat] = 'O'
                    print(f"Booking {booking_number} for Flight {flight} has been canceled.")
                else:
                    print(f"Error: Booking {booking_number} not found in the seating plan.")

            else:
                file.write(lines[i])
                file.write(lines[i + 1])
                file.write(lines[i + 2])
                file.write(lines[i + 3])
                file.write(lines[i + 4])

    with open("seating_plan.txt", "w") as plan_file:
        for row in seats:
            plan_file.write(" ".join(row) + "\n")


def show_flights():
    for x in range (len(flightlist)):
        print(flightlist[x])
        display_seating_chart()
        
                    

flightlist = ["Flight A", "Flight B", "Flight C"]

for _ in range(100):
    print("WELCOME TO DAR AIRLINES")
    print("Please log in or sign up for an account to get started.")
    print("1. LOG IN")
    print("2. SIGN UP")
    choice = input("Enter your option: ")

    if choice == "1":
        if login():
            print("WELCOME")
            print("1. Book a flight")
            print("2. Cancel a booking")
            print("3. Show available seats")
            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                book_flight()
            elif sub_choice == "2":
                cancel_flight()
            elif sub_choice == "3":
                show_flights()

    elif choice == "2":
        signup()
    else:
        continue


