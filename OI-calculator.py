def calculate_oxygen_index(map_value, fio2_value, pao2_value):
    try:
        # Check for non-negative values
        if map_value < 0 or fio2_value < 0 or pao2_value < 0:
            raise ValueError("Values cannot be negative.")

        # Calculate Oxygen Index
        oxygen_index = (map_value * fio2_value * 100) / pao2_value
        return oxygen_index

    except ZeroDivisionError:
        print("Error: Division by zero. Please ensure PaO2 is not zero.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Input values from the user
try:
    map_value = float(input("Enter Mean Airway Pressure (MAP): "))
    fio2_value = float(input("Enter Fraction of Inspired Oxygen (FiO2): "))
    pao2_value = float(input("Enter Partial Pressure of Oxygen (PaO2): "))

    # Calculate and display Oxygen Index
    result = calculate_oxygen_index(map_value, fio2_value, pao2_value)
    if result is not None:
        print(f"The Oxygen Index (OI) is: {result}")

except ValueError:
    print("Error: Please enter valid numeric values for MAP, FiO2, and PaO2.")
except KeyboardInterrupt:
    print("\nMeasurement aborted by the user.")
