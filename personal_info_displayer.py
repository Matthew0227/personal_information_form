def letters_only_input(prompt):
    while True:
        name_ = input(prompt)
        if any(char.isdigit() for char in name_):
            print("Please enter letter only")
        else:
            return name_

while True:
    print("-------------------")
    print("Data Information")
    print("-------------------")
    print("Enter the following to retrieve your information")
    surname = letters_only_input("Please enter your last name: ")
    first_name = letters_only_input("Please enter your first name: ")

    while True:
            age = input("Age: ")
            if age.isdigit():
                age = int(age)
                if 0 < age < 121:
                    age = str(age)
                    break
            else:
                print("Please enter your age (1-120 only).")

    file_data = f"./{surname}_{first_name}_{age}.txt"

    try:
        with open(file_data, "r") as file_txt:
            print(file_txt.read())
    except FileNotFoundError:
        print("The person does not exist in the data, would you like to try again?: ")

    try:
        retry = input("Try again?(y/n): ")
        if retry == "y" or "n":
            print()
    except:
        print("enter y/n: ")

    if retry == "y":
        print()
    elif retry == "n":
        break