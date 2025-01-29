#unit conversions
def unitConversions(value, unit):
    if unit == "cm":
        convertedValue = value / 2.54
        convertedUnit = "in"
    elif unit == "in":
        convertedValue = value * 2.54
        convertedUnit = "cm"
    elif unit == "yd":
        convertedValue = value * 0.9144
        convertedUnit = "m"
    elif unit == "m":
        convertedValue = value / 0.9144
        convertedUnit = "yd"
    elif unit == "oz":
        convertedValue = value * 28.349523125
        convertedUnit = "g"
    elif unit == "g":
        convertedValue = value / 28.349523125
        convertedUnit = "oz"
    elif unit == "lb":
        convertedValue = value * 0.45359237
        convertedUnit = "kg"
    elif unit == "kg":
        convertedValue = value / 0.45359237
        convertedUnit = "lb"
    #input verification
    else:
        raise ValueError("Unsupported unit")
    
    return convertedValue, convertedUnit

#input and output
def main():
    user_input = input("Please enter the value and unit: ")
    
    try:
        value_str, unit = user_input.split()
        value = float(value_str)
        
        convertedValue, convertedUnit = unitConversions(value, unit)
        
        print(f"{value} {unit} = {convertedValue:.2f} {convertedUnit}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print("Invalid input. Please enter a number followed by a unit.")

main()
