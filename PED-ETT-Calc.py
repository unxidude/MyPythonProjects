def calculate_et_tube_size_and_location(weight_kg):
    # Pediatric ETT size calculation
    if weight_kg < 5:
        et_size = "2.5"
        taping_location_cm = 8  # Example value, adjust as needed
    elif 5 <= weight_kg < 12:
        et_size = "3.0"
        taping_location_cm = 9  # Example value, adjust as needed
    elif 12 <= weight_kg < 20:
        et_size = "3.5"
        taping_location_cm = 10  # Example value, adjust as needed
    elif 20 <= weight_kg < 30:
        et_size = "4.0"
        taping_location_cm = 11  # Example value, adjust as needed
    elif 30 <= weight_kg < 50:
        et_size = "4.5"
        taping_location_cm = 12  # Example value, adjust as needed
    else:
        et_size = "5.0"
        taping_location_cm = 13  # Example value, adjust as needed

    return et_size, taping_location_cm

# Input weight from the user
try:
    weight_kg = float(input("Enter the patient's weight in kilograms: "))

    # Calculate ETT size and taping location
    et_size, taping_location_cm = calculate_et_tube_size_and_location(weight_kg)

    # Display the results
    print(f"Recommended ETT size: {et_size}")
    print(f"Recommended taping location at the gum: {taping_location_cm} cm at the gums")

except ValueError:
    print("Error: Please enter a valid numeric weight.")
except KeyboardInterrupt:
    print("\nMeasurement aborted by the user.")
# Written by Raul Ruiz, Jr. (How is this possible?), "Well, because I just can."(:
