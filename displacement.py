import sys
import os
import math
def print_menu():
    print("1. Displacement calculation")
    print("2. Horsepower calculation")
    print("3. Torque calculation")
    print("4. Gear ratio calculator[under dev]")
    print("5. Ideal car finder [under dev]")
    print("6. Conversions")
    print("7. Help")

#displacement calculator start
def displacement():
    print("Please remember that wankel engines are not supported at the moment!")
    bore = float(input("Enter the bore in mm : "))
    stroke = float(input("Enter the stroke in mm :"))
    bore = bore / 2
    cyl = int(input("Enter the amount of cylinders : "))
    # Disp = stroke * 3.14 * math.pow(bore, 2) *cyl
    Disp = 3.14 * math.pow(bore, 2.0) * stroke * cyl
    Disp = (Disp / 1000)
    Disp = "{:.1f}".format(Disp)
    print("For a", cyl, "cylinder engine, the displacement is", Disp, "cm3")
# displacement calculator end

displacement()