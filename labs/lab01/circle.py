import math

def main():
    # checking input
    while True:
        try:
            #input radius
            radiusInput = input("Please enter the radius of your circle: ")
            radius = float(radiusInput)
            if radius < 0:
                print("The radius cannot be negative. Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive number.")

    #calculating area/perimeter
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius

    #print
    print(f"The circle with radius {radius} has an area of {area:.2f} and a perimeter of {perimeter:.2f}")

main()