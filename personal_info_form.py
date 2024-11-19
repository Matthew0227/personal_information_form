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
                phone_num = int(phone_num)
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
                break
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
