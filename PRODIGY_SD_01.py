def convert_temperature(value, unit):
    unit = unit.lower()

    if unit == "c":
        c = value
        f = (c * 9/5) + 32
        k = c + 273.15
    elif unit == "f":
        f = value
        c = (f - 32) * 5/9
        k = c + 273.15
    elif unit == "k":
        k = value
        c = k - 273.15
        f = (c * 9/5) + 32
    else:
        print("Invalid unit! Please enter C, F, or K.")
        return

    print("\nConverted Temperatures:")
    print(f"Celsius: {c:.2f} °C")
    print(f"Fahrenheit: {f:.2f} °F")
    print(f"Kelvin: {k:.2f} K")


# User Input
try:
    temp_value = float(input("Enter temperature value: "))
    temp_unit = input("Enter unit (C for Celsius, F for Fahrenheit, K for Kelvin): ")

    convert_temperature(temp_value, temp_unit)

except ValueError:
    print("Please enter a valid numeric temperature.")