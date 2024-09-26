def calculate_bill(previous_reading, current_reading):
    # Ensure current reading is greater than previous reading
    if current_reading < previous_reading:
        raise ValueError("Current reading must be greater than previous reading.")
    
    # Calculate units consumed
    units_consumed = current_reading - previous_reading
    
    # Define the rates in Rupees (you can modify these as needed)
    if units_consumed <= 100:
        bill_amount = units_consumed * 5  # Rate per unit for first 100 units
    elif units_consumed <= 200:
        bill_amount = (100 * 5) + ((units_consumed - 100) * 7)  # Rate for next 100 units
    else:
        bill_amount = (100 * 5) + (100 * 7) + ((units_consumed - 200) * 10)  # Rate for more than 200 units

    return bill_amount

def main():
    previous_reading = 100  # Fixed previous reading
    try:
        current_reading = float(input("Enter current meter reading in units: "))
        bill = calculate_bill(previous_reading, current_reading)
        print(f"Total bill amount: ₹{bill:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
