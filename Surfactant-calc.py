def calculate_surfactant_dose(weight_kg=None, gestational_age_weeks=None):
    # Check if either weight or gestational age is provided
    if weight_kg is None and gestational_age_weeks is None:
        raise ValueError("Please provide either weight or gestational age.")

    # Surfactant dose calculation based on weight
    if weight_kg is not None:
        if weight_kg < 0:
            raise ValueError("Weight cannot be negative.")
        elif weight_kg < 700:
            surfactant_dose = "100 mg/kg"
        elif 700 <= weight_kg <= 1000:
            surfactant_dose = "200 mg/kg"
        else:
            surfactant_dose = "Not recommended for weight > 1000 g"

    # Surfactant dose calculation based on gestational age
    elif gestational_age_weeks is not None:
        if gestational_age_weeks < 23 or gestational_age_weeks > 34:
            raise ValueError("Gestational age should be between 23 and 34 weeks.")
        elif 23 <= gestational_age_weeks <= 28:
            surfactant_dose = "100 mg/kg"
        else:
            surfactant_dose = "200 mg/kg"

    return surfactant_dose

# Input parameters from the user
try:
    weight_input = input("Enter the patient's weight in kilograms (press Enter to skip): ")
    gestational_age_input = input("Enter the patient's gestational age in weeks (press Enter to skip): ")

    # Convert inputs to float or None
    weight_kg = float(weight_input) if weight_input else None
    gestational_age_weeks = float(gestational_age_input) if gestational_age_input else None

    # Calculate surfactant dose
    surfactant_dose = calculate_surfactant_dose(weight_kg, gestational_age_weeks)

    # Display the result
    print(f"Recommended surfactant dose: {surfactant_dose}")

except ValueError as ve:
    print(f"Error: {ve}")
except KeyboardInterrupt:
    print("\nMeasurement aborted by the user.")

