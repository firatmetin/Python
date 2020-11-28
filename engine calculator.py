import sys
import os
import math

# welcome message
print("Welcome to engine calculator 1.0 openBeta")
print("Please note the following functions will only work for naturally aspirated : \n"
      "1. Torque calculation. \n"
      "2. Horsepower calculation. \n"
      "\n"
      "--------------------\n"
      "Please choose an option below:\n"
      "")


# we will define the menu, then associated commands
def print_menu():
    print("1. Displacement calculation")
    print("2. Horsepower calculation")
    print("3. Torque calculation[under dev]")
    print("4. Gear ratio calculator[under dev]")
    print("5. Ideal car finder [under dev]")
    print("6. Conversions")
    print("7. Help")

def conv_menu():
    print("1. Newton Meters (nm) to Pound Foot (lb-ft) : ")
    print("2. Pound Foot (lb-ft) to Newton Meters (nm) : ")
    print("3. Kilometre to Mile conversion : ")
    print("4. Mile to Kilometre conversion : ")
    print("5. kiloWatt to Horsepower calculation : ")
    print("6. Horsepower to kiloWatt calcilation : ")

def help_menu():
    print("1. What does torque mean? : ")
    print("2. What does horsepower mean? : ")
    print("3. What is a bore/stroke in an engine? : ")

# displacement calculator start
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


# horsepower calculation start

def horsepower():
    print("You may use our ft-lb to nm calculator if you don't know your torque figure in newton-meters.")
    q = int(input("Would you like to use our lb-ft or newton meters ?\n"
                  "Input 0 for nm, 1 for lb-ft :"))
    while q != 0 and q != 1:
        q = int(input("Would you like to use our lb-ft or newton meters ?\n"
                      "Input 0 for no, 1 for yes :"))
    if q == 0:
        tq = float(input("Please enter the torque in nm: "))
        rpm = int(input("Please enter revolutions per minute (rpm) :"))
        hp = ((tq * rpm) / 7127)
        hp = "{:.1f}".format(hp)
        print("The engine with", tq, "nm torque has", hp, "horsepower")
    if q == 1:
        tq = float(input("Please enter torque in lb-ft"))
        rpm = int(input("Please enter revolutions per minute (rpm) :"))
        hp = ((tq * rpm) / 5252)
        hp = "{:.1f}".format(hp)
        print("The engine with", tq, "lb-ft torque has", hp, "horsepower")


# horsepower calculation end
# menu spawn starts  here
print_menu()
choice = input("Which calculation would  you like to carry out :")
if choice == '1':
    displacement()
elif choice == '2':
    horsepower()
elif choice == '3':
    print("The current function is currenltly unavailable")
elif choice == '4':
    print("The current function is currenltly unavailable")
elif choice == '5':
    print("The current function is currenltly unavailable")
elif choice == '6':
    print("The current function is currenltly unavailable")
elif choice == '7':
    print("The current function is currenltly unavailable")

