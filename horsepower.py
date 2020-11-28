import sys
import os
import math
while True:
    def print_menu():
        print("1. Displacement calculation")
        print("2. Horsepower calculation")
        print("3. Torque calculation")
        print("4. Gear ratio calculator[under dev]")
        print("5. Ideal car finder [under dev]")
        print("6. Conversions")
        print("7. Help")
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
            print("The engine with", tq, "lb-ft torque has", hp, "horsepower\n"
                  "\n"
                  "-----------------\n"
                  "")
        choice = int(input("\nWould you like to make another process?\n"
                  "1. I would like to calculate another horsepower\n"
                  "2. I would like to use a conversion\n"
                  "3. I would like to perform another operation"))
        while choice < 1 and choice > 4:
            choice = int(input("Would you like to make another process? \n"
                               "1. I would like to calculate another horsepower: \n"
                               "2. I would like to use a conversion :\n"
                               "3. I would like to perform another operation :\n"
                               "choice: "))
            if choice == 1:
                horsepower()
            elif choice == 2:
                print_menu() # this to be replaced by help_menu()
            elif choice == 3:
                print_menu()
            if choice == 4:
                break