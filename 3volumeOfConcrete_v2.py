"""This program calculates the amount of concrete required for the desired width
 and length of a residential or commercial building"""


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
print("Welcome to the Concrete Calculator. To end program and receive total "
      "concrete requirements, please enter building type as 'x'.")
print()

# get user input for building type, length, width
building_type = (building_checker("Building type - residential or commercial: ")
                 .lower())
building_length = integer_checker("Building length in metres: ")
building_width = integer_checker("Building width in metres: ")

# find appropriate depth
if building_type == "commercial":
    depth = 0.5

elif building_type == "residential":
    depth = 0.25
