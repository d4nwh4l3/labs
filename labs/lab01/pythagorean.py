import math

def main():
    #first side
    side1Input = input("Please enter the length for the first side of your triangle: ")

    #second side
    side2Input = input("Please enter the length for the second side of your triangle: ")

    #convert string inputs to float
    side1Number = float(side1Input)
    side2Number = float(side2Input)

    #calculate hypotenuse
    hypotenuse = math.sqrt(side1Number**2 + side2Number**2)

    #print
    print(f"The hypotenuse is {hypotenuse:.2f}")

main()