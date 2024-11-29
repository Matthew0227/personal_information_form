personal_informations_datas = {}

def letters_only_input(prompt,error):
    while True:
        name_ = input(prompt)
        if any(char.isdigit() for char in name_):
            print(error)
        else:
            return name_

def phone_numbers_input(prompt1,error1):
    while True:
        phone_num = input(prompt1)
        if len(phone_num) == 11:
            if phone_num.isdigit():
                phone_num = str(phone_num)
                return phone_num
        else:
            print(error1)

while True:
    first_name = letters_only_input("First name: ", "Please your name correctly (letters and symbols only).")
    middle_name = letters_only_input("Middle name: ", "Please your name correctly (letters and symbols only).")
    surname = letters_only_input("Surname: ", "Please your name correctly (letters and symbols only).")
    
    while True:
        age = input("Age: ")
        if age.isdigit():
            age = int(age)
            if 0 < age < 121:
                age = str(age)
                break
            else:
                print("Please enter your age (1-120 only).")
        else:
            print("Please enter your age (1-120 only).")

    while True:
        birthdate = input("birthdate (mm/dd/yyyy): ")
        if any(char.isalpha() for char in birthdate):
            print("Please enter the correct format (no letters).")

        else:
            if len(birthdate) == 10:
                break
            print("Please enter the correct format.")

    nationality = letters_only_input("Nationality: ", "Please your nationality (letters only).")
    occupation = letters_only_input("Occupation: ", "Please your occupation (letters only).")
    address = input("Address: ")
    telephone_number = phone_numbers_input("Telephone number: ", "Please enter your telephone number (11 digits only).")
    phone_number = phone_numbers_input("Phone number: ", "Please enter your phone number (11 digits only).")
    gmail = input("Gmail: ")


    personal_informations_datas[surname+"_"+first_name+"_"+age] = {
        "First name" : first_name,
        "Middle name" : middle_name,
        "Surname name" : surname,
        "Age" : age,
        "Birthdate" : birthdate,
        "Nationality" : nationality,
        "Occupation" : occupation,
        "Address" : address,
        "Telephone number" : telephone_number,
        "Phone number" : phone_number,
        "Gmail" : gmail,
    }

    with open(f"./{surname}_{first_name}_{age}.txt", "w") as file_txt:
        file_txt.write("-------------------\n")
        file_txt.write("Personal Data Form\n")
        file_txt.write("-------------------\n")
        file_txt.write("First name: ")
        file_txt.write(first_name)
        file_txt.write("\n")
        file_txt.write("Middle name: ")
        file_txt.write(middle_name)
        file_txt.write("\n")
        file_txt.write("Last name: ")
        file_txt.write(surname)
        file_txt.write("\n")
        file_txt.write("-------------------\n")
        file_txt.write("Age: ")
        file_txt.write(age)
        file_txt.write("\n")
        file_txt.write("Birthdate: ")
        file_txt.write(birthdate)
        file_txt.write("\n")
        file_txt.write("Nationality: ")
        file_txt.write(nationality)
        file_txt.write("\n")
        file_txt.write("Occupation: ")
        file_txt.write(occupation)
        file_txt.write("\n")
        file_txt.write("Address: ")
        file_txt.write(address)
        file_txt.write("\n")
        file_txt.write("Telephone number: ")
        file_txt.write(telephone_number)
        file_txt.write("\n")
        file_txt.write("Phone number: ")
        file_txt.write(phone_number)
        file_txt.write("\n")
        file_txt.write("Gmail: ")
        file_txt.write(gmail)
        file_txt.write("\n")
        
    try:
        retry = input("add another person?(y/n): ")
        if retry == "y" or "n":
            print()
    except:
        print("enter y/n: ")

    if retry == "y":
        print()
    elif retry == "n":
        break