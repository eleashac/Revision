"""
This program calculates the amount of concrete required for the desired width
 and length of a residential or commercial building
v3 fixes the problem with depth calculations by placing the variables into the
loop and changes the while loop so that it includes a 'break' to break the loop
 replacing 'x' with 'while True' to finish the program. Corrects the order so
the loop first checks if the user entered 'x' before proceeding with the rest
of the calculations (still does not work)
 """


# integer checker
def integer_checker(question):
    error = "\nPlease enter an integer"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


# building type checker
def building_checker(question):
    error = "\nPlease enter either 'residential' or 'commercial' "
    _type = ""
    while _type != "residential" and _type != "commercial":
        _type = input(question).lower()
        if _type != "residential" and _type != "commercial":
            print(error)
    return _type


# welcome user
print("\nWelcome to the Concrete Calculator. To end program and receive total "
      "concrete requirements, please enter building type as 'x'.\n")

# initialize total volume variable
total_concrete_volume = 0

# main routine
# get user input for building type
building_type = (
    building_checker("Building type - residential or commercial: ")
    .lower())

# run the program until the user enters 'X' for building type
while True:

    # adds depth variable
    RESIDENTIAL_DEPTH = 0.25
    COMMERCIAL_DEPTH = 0.5

    # get user input for building length, width
    building_length = integer_checker("Building length in metres: ")
    building_width = integer_checker("Building width in metres: ")

    # find appropriate depth
    if building_type == "commercial":
        depth = COMMERCIAL_DEPTH

    elif building_type == "residential":
        depth = RESIDENTIAL_DEPTH

    # calculate the volume of concrete needed
    concrete_volume = building_length * building_width * depth

    # output the statement with the calculated volume
    print(f"The volume of concrete required for a slab with a length of "
          f"{building_length} and width of {building_width} and a depth of "
          f"{depth} is {concrete_volume} cubic meters.\n")

    # update the total volume
    total_concrete_volume += concrete_volume

    # get new inputs for the next building
    building_type = building_checker("Building type - residential or "
                                     "commercial: ")

    # If the user entered 'X', break out of the loop
    if building_type.lower() == "x":
        break


# print farewell thank you message
print(f"\nThe total amount of concrete needed for the day is "
      f"{total_concrete_volume} cubic meters.")
print("Thank you for using Concrete Calculator!\n")
