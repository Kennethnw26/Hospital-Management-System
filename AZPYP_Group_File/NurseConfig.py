patientinfo = open("patient_vitals.txt", "r")
patientlist = patientinfo.read().replace("\n",",").split(",")
patientinfo.close()

from patient_dictionary import *

def dynamic_dynamic_whitespace():
    return 50

def authentication () :
    while True:
        # Ask the user to enter their name
        nurse_name = (input("Enter your name!\n"
                                 "> "))
        print(f"\nHello Nurse {nurse_name}\n")
        while True:
            # Ask the user to enter the correct password
            nurse_input_pass = input(f"Enter the password here to verify yourself! \n"
                                      f"Enter 'exit' to exit the program \n\n"
                                      f"> ")
            if nurse_input_pass == "nurse12345": # This is the correct password
                print()
                print(f"Hello {nurse_name}, Welcome back! ")
                print()
                break
            elif nurse_input_pass.lower() == "exit": # If the user wants to exit the program
                print("\nThank you! ")
                exit()
            else:
                print("Value inputted is invalid")
                print()# Print an error message if the password is not correct
        break
    return nurse_name


#To read patient content of each patient and the specific details
def read_patient_content(patient_record):
    keys_to_extract = ["patient_id", "name", "insurance"]
    for key in keys_to_extract:
        if key in patient_record:
            print(f"{key}: {patient_record[key]}")

#To show and Index patient number from patient record 1 to 5
def indexing_patient(patients):
    for idx in range(len(patients)):
        print(f"Patient {idx + 1} Details:")
        read_patient_content(patients[idx])
        print("\n" + "-" * 30 + "\n")

def nurse_config_access_list_of_patients(columns = (0, 1, 2, 3, 4)):
    patients = [patient1_record, patient2_record, patient3_record, patient4_record, patient5_record]
    read_patient_content(patients)
    indexing_patient(patients)
    


def show_specific_patient_list(index1, number_of_columns=6,column_titles=(),file="patient_vitals.txt"):
    with open(file, "r") as z: # Open file in read mode
        temp = z.read().replace("\n", "").split(",")

    # The width of each column
    column_width = dynamic_dynamic_whitespace()

    header = "|".join([title.center(column_width) for title in column_titles])
    separator = "|".join(["_" * column_width for _ in column_titles])
    print(f"|{header}|")
    print(f"|{separator}|")

    # The starting index for the patient data
    patient_start_index = index1 * number_of_columns
    if patient_start_index < len(temp):
        # extract the patient data based on the calculated index
        patient_data = temp[patient_start_index:patient_start_index + number_of_columns]
        # Print the patient row by centering each data element within the calculated width
        patient_row = "|".join([data.center(column_width) for data in patient_data])
        print(f"|{patient_row}|")

    print(f"|{separator}|")

def show_medical_emergencies(index1, number_of_columns=4,column_titles=(),file="medical_emergencies.txt"):
    with open(file, "r") as z: # Open file in read mode
        temp = z.read().replace("\n", "").split(",")

    # The width of each column
    column_width = dynamic_dynamic_whitespace()

    header = "|".join([title.center(column_width) for title in column_titles])
    separator = "|".join(["_" * column_width for _ in column_titles])
    print(f"|{header}|")
    print(f"|{separator}|")

    # The starting index for the patient data
    patient_start_index = index1 * number_of_columns
    if patient_start_index < len(temp):
        # extract the patient data based on the calculated index
        patient_data = temp[patient_start_index:patient_start_index + number_of_columns]
        # Print the patient row by centering each data element within the calculated width
        patient_row = "|".join([data.center(column_width) for data in patient_data])
        print(f"|{patient_row}|")

    print(f"|{separator}|")


def nurse_config_update_patient_vitals():
    def update_Temperature(): # This function is to update temperature
        Temperature = input("\nEnter the updated Temperature\n(Separate with commas for multiple values)\n> ").replace(
            ",", "|")
        Temperature_temp = Temperature.split("|")

        for idx, item in enumerate(Temperature_temp):
            Temperature_temp[idx] = item.strip()

        Temperature = "|".join(Temperature_temp)
        temp[index + 2] = Temperature.replace("|", "|".center(1, " "))

    def update_Heart_rate(): # This function is to update heart rate
        Heart_rate = input("\nEnter the updated Heart_rate\n(Separate with commas for multiple values)\n> ").replace(
            ",", "|")
        Heart_rate_temp = Heart_rate.split("|")

        for idx, item in enumerate(Heart_rate_temp):
            Heart_rate_temp[idx] = item.strip()

        Heart_rate = "|".join(Heart_rate_temp)
        temp[index + 3] = Heart_rate.replace("|", "|".center(1, " "))

    def update_Blood_pressure(): # This function is to update blood pressure
        Blood_pressure = input(
            "\nEnter the updated Blood_pressure\n(Separate with commas for multiple values)\n> ").replace(",", "|")
        Blood_pressure_temp = Blood_pressure.split("|")

        for idx, item in enumerate(Blood_pressure_temp):
            Blood_pressure_temp[idx] = item.strip()

        Blood_pressure = "|".join(Blood_pressure_temp)
        temp[index + 4] = Blood_pressure.replace("|", "|".center(1, " "))

    def update_Respiration_rate(): # This function is to update respiration rate
        Respiration_rate = input(
            "\nEnter the updated Respiration_rate\n(Separate with commas for multiple values)\n> ").replace(",", "|")
        Respiration_rate_temp = Respiration_rate.split("|")

        for idx, item in enumerate(Respiration_rate_temp):
            Respiration_rate_temp[idx] = item.strip()

        Respiration_rate = "|".join(Respiration_rate_temp)
        temp[index + 5] = Respiration_rate.replace("|", "|".center(1, " "))

    while True:
        try:
            # Ask user to enter their code or name or back
            name = input(
                "\nPlease enter the code or name of the patient whose record you would like to update\nPlease enter 'back' to exit this action\n> ").strip()
            if name.lower() == "back":
                print("\n")
                break

            # Open file in read mode
            with open("patient_vitals.txt", "r") as z:
                temp = z.read().replace("\n", "").split(",")
            index = temp.index(name)
            index = (index // 6) * 6
            print()
            # Call the function to show the updated patient's data
            show_specific_patient_list(index // 6,6,["ID", "Name", "Temperature", "Heart_rate", "Blood_pressure", "Respiration_rate"])

            while True:
                try:
                    # Ask the user to choose which data to update
                    choice = input(
                        "\nWould you like to update:\n1. Temperature\n2. Heart_rate\n3. Blood_pressure\n4. Respiration_rate\nPlease enter your choice (1, 2, 3, or 4): ").strip()
                    if choice == "1":
                        update_Temperature()
                    elif choice == "2":
                        update_Heart_rate()
                    elif choice == "3":
                        update_Blood_pressure()
                    elif choice == "4":
                        update_Respiration_rate()
                    else:
                        print("Invalid choice. Please select 1, 2, 3, or 4.")
                        break

                    # Open file in write mode
                    with open("patient_vitals.txt", "w") as open_write_file:
                        y = 0
                        for x in range(len(temp)):
                            if x == len(temp) - 1:
                                open_write_file.write(temp[x].strip())
                            elif y == 6:
                                open_write_file.write("\n")
                                open_write_file.write(temp[x].strip() + ",")
                                y = 1
                            else:
                                open_write_file.write(temp[x].strip() + ",")
                                y += 1
                    # Call the function to show the updated patient's data
                    show_specific_patient_list(index // 6,6,["ID", "Name", "Temperature", "Heart_rate", "Blood_pressure", "Respiration_rate"])
                    break
                except ValueError:
                    print("Value inputted is invalid")
                except KeyboardInterrupt:
                    print("\nExiting")
                    break
        except ValueError:
            print("Value inputted is invalid")


def nurse_config_prepare_room():
    while True:
        try:
            # Ask user to enter the room number
            room_number = int(input("Enter the room number to prepare: "))
            while True:
                # Ask user to enter whether the room is clean or not
                is_clean = input(
                    "Is the room clean or not? (if the room is clean, enter yes) (if the room is not clean, enter no): ").strip().lower()
                # The valid answer is only between yes or no
                if is_clean in ["yes", "no"]:
                    break
                else:
                    print("Invalid input for cleanliness. Please enter 'yes' or 'no'.")

            while True:
                # Ask user to enter whether the room have the necessary equipment or no
                has_equipment = input(
                    "Does the room have the necessary equipment? (If the room does, enter yes) (if the room does not, enter no): ").strip().lower()
                # The valid answer is only between yes or no
                if has_equipment in ["yes", "no"]:
                    break
                else:
                    print("Invalid input for equipment. Please enter 'yes' or 'no'.")
            if is_clean == "yes":
                print(f"Room {room_number} is clean!!!")
            elif is_clean == "no":
                print(f"Please wait.....(Cleaning room {room_number})")
                print(f"Room {room_number} is now clean.")
            if has_equipment == "yes":
                print(f"Room {room_number} has the necessary equipment.")
            elif has_equipment == "no":
                print(f"Please wait.....(Adding necessary equipment to room {room_number})")
                print(f"Room {room_number} is now equipped with necessary items.")
            print(f"Thank you for waiting!!!\nRoom {room_number} is now ready for treatment or surgical procedure.\n\n")
            break
        except ValueError:
            print("Invalid Room Number. Please input the room only using number!")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Let's try again.")


def nurse_config_manage_medication_log(columns = (0, 1, 2, 3, 4, 5)):
    number_of_columns = len(columns)
    row1 = 0
    row2 = 0
    # Open the file in read mode
    var1 = open("medication.txt", "r")
    # Read the file content, replace newlines with commas, and split by commas
    list1 = var1.read().replace("\n",",").split(",")
    var1.close()
    # Open the file again in read mode to count the number of rows
    temp_var_2 = open("medication.txt", "r")
    for lines in temp_var_2.readlines():
        row1 += 1
    temp_var_2.close()
    print()
    while row2 < row1:
        for column in columns:
            print("|", end="")
            # Check if the element at the current position is an underscore
            if list1[(number_of_columns * row2) + column] == "_":
                # Center the element with underscores
                print(list1[(number_of_columns * row2) + column].strip().center((dynamic_dynamic_whitespace()),
                                                                                        "_"), end="")
            else:
                # Center the element with spaces
                print(list1[(number_of_columns * row2) + column].strip().center((dynamic_dynamic_whitespace()),
                                                                                        " "), end="")
        print("|")
        row2 += 1
    print()

def nurse_config_report_medical_emergencies(columns = (0, 1, 2, 3)):
    def update_medical_emergencies(): # This function is to update medical emergencies
        medical_emergencies = input(
            "\nEnter the updated medical_emergencies\n(Separate with commas for multiple values)\n> ").replace(
            ",", "|")
        medical_emergencies_temp = medical_emergencies.split("|")

        for idx, item in enumerate(medical_emergencies_temp):
            medical_emergencies_temp[idx] = item.strip()

        medical_emergencies = "|".join(medical_emergencies_temp)
        temp[index + 3] = medical_emergencies.replace("|", "|".center(1, " "))

    while True:
        try:
            name = input(
                "\nPlease enter the code or name of the patient whose record you would like to update\nPlease enter 'back' to exit this action\n> ").strip()
            if name.lower() == "back":
                print("\n")
                break

            with open("medical_emergencies.txt", "r") as z:
                temp = z.read().replace("\n", "").split(",")
            index = temp.index(name)
            index = (index // 4) * 4
            print()
            # Call the function to show the updated patient's data
            show_medical_emergencies(index // 4,4,("Doctor","ID","Name","Medical emergencies"),"medical_emergencies.txt")

            while True:
                try:
                    # Ask the user to enter their choice
                    choice = input(
                        "\nWould you like to update the medical emergencies?(yes = 1)(no = 2):").strip()
                    if choice == "1":
                        update_medical_emergencies()
                    elif choice == "2":
                        break
                    else:
                        print("Invalid choice. Please type 1 or 2")
                        break

                    # Open file in write mode
                    with open("medical_emergencies.txt", "w") as open_write_file:
                        y = 0
                        for x in range(len(temp)):
                            if x == len(temp) - 1:
                                open_write_file.write(temp[x].strip())
                            elif y == 4:
                                open_write_file.write("\n")
                                open_write_file.write(temp[x].strip() + ",")
                                y = 1
                            else:
                                open_write_file.write(temp[x].strip() + ",")
                                y += 1
                    # Call the function to show the updated patient's data
                    show_medical_emergencies(index // 4,4,("Doctor","Id","Name","Medical emergencies"),"medical_emergencies.txt")

                except ValueError:
                    print("Value inputted is invalid")
                except KeyboardInterrupt:
                    print("\nExiting")
                    break
        except ValueError:
            print("Value inputted is invalid")