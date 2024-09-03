def gallons_to_liters(gallons):
    LITERS_PER_GALLON = 3.785
    return gallons * LITERS_PER_GALLON

def main():
    while True:

        gallons = float(input("Enter the amount of gasoline in gallons (enter a negative number to quit): "))

        if gallons < 0:
            print("Negative gallon amount entered. Program terminating.")
            break

        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallons is {liters:.2f} liters.")

main()
