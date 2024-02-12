"""
This program calculates the amount of concrete required for the desired width
 and length of a residential or commercial building
 v2 calculates total volume and inputs a loop broken by inputting 'x'
 also changes depth to variables and adds thank you message
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


# adds depth variable
RESIDENTIAL_DEPTH = 0.25
COMMERCIAL_DEPTH = 0.5

# welcome user
print("\nWelcome to the Concrete Calculator. To end program and receive total "
      "concrete requirements, please enter building type as 'x'.\n")

# get user input for building type, length, width
building_type = (building_checker("Building type - residential or commercial: ")
                 .lower())
building_length = integer_checker("Building length in metres: ")
building_width = integer_checker("Building width in metres: ")

# find appropriate depth
if building_type == "commercial":
    depth = COMMERCIAL_DEPTH

elif building_type == "residential":
    depth = RESIDENTIAL_DEPTH

# initialize total volume variable
total_concrete_volume = 0

# run the program until the user enters 'X' for building type
while building_type.lower() != "x":
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
    building_length = integer_checker("Building length in metres: ")
    building_width = integer_checker("Building width in metres: ")

    # if the user entered 'X', print the total concrete needed and end program
    if building_type.lower() == "x":
        print(f"\nThe total amount of concrete needed for the day is "
              f"{total_concrete_volume} cubic meters.")

# print farewell thank you message
print("Thank you for using Concrete Calculator!\n")
