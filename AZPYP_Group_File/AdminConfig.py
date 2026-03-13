from patient_dictionary import *

#For admin authentication 
def user_role_1():
    """This will ensure that the admin can only bypass it if they enter the correct password, 
    if not then they won't be able to access the system without the correct password"""
    #The function of 'while True' forces the user to repeat the input process and will only stop when a 'break' is called
    while True:
        print()
        admin_name = input("Enter your name! > ")
        #The line below will check if the admin name is in an alphabet or not, if yes then boolean True will be returned
        x = admin_name.isalpha()
        if x == True :
            print(f"Hello Administrator {admin_name}")
            while True: 
                """The block of code below will check if the admin has entered the correct password, 
                if not it will keep repeating until the correct password entered or not"""
                admin_input_pass = input("Enter the password here to verify yourself! ")
                if admin_input_pass == "admin12345":
                    print(f"Hello {admin_name}, Welcome back! ")
                    print()
                    break
                elif admin_input_pass == "exit":
                    print("Thank you! ")
                    exit()
                else: 
                    print("The password you have enter is incorrect please try again! ")
                    print("Enter 'exit' to exit the program ")
            break
        else:
            print("Your name must be in the alphabet letters")

#For Checking Insurance Policy contents
def check_insurance(Policy_holder_name, Policy_number):
    try:
        #The file handling syntax below automatically open and closes the file and it is called as a 'file'
        csv_file = "insurance_data.csv"
        with open(csv_file, "r") as file:
            rows = file.readlines()
        # Loop through rows to find a match
        for row in rows:
            data = row.strip().split(",")
            if data[0] == Policy_holder_name and data[1] == Policy_number:
                if data[2] == "Valid":
                    print("Insurance claim approved.")
                    return "approved"
                else:
                    print("Insurance claim not approved.")
                    return "not approved"
        # If no match is found
        print("Policy holder or number not found.")
        return "not found"
    except FileNotFoundError:
        print("The insurance data file does not exist.")
        return "error"

#For Roles file
def create_file_roles(file_name):
    #Create a new CSV file with headers
    try: 
        #The file handling syntax below automatically open and closes the file and it is called as a 'file'
        with open(file_name, 'w') as file:
            headers = input("Enter column headers separated by commas: ")
            file.write(headers + '\n')
        print(f"File '{file_name}' created successfully!")
        print()
    except FileExistsError:
        print(f"File '{file_name} has already been created!")
        print()

#For Roles file
def add_file_roles(file_name, new_header):
    #Add a new policy to the file
    try:
        #The file handling syntax below automatically open and closes the file and it is called as a 'file'
        with open(file_name, 'a') as file:
            file.write(new_header + '\n')
        print("Changes made successfully.")
        print()
    except FileNotFoundError:
        print(f"File '{file_name}' not found! Please create it first.")
        print()

#For Roles file
def update_file_roles(file_name):
    #Update a specific row in the CSV file
    try:
        #The file handling syntax below automatically open and closes the file and it is called as a 'file'
        with open(file_name, 'r') as file:
            rows = file.readlines()
        print("Existing rows:")
        row_index = 0
        for row in rows:
            print(f"{row_index}: {row.strip()}")
            row_index += 1
        #Allows the user to edit a specific selected row by entering an integer value
        try:
            row_number = int(input("Enter the row number to update (starting from 0): "))
            if 0 <= row_number < len(rows):
                print(f"Current data: {rows[row_number].strip()}")
                new_data = input("Enter new data for this row, separated by commas: ")
                rows[row_number] = new_data + '\n'

                with open(file_name, 'w') as file:
                    file.writelines(rows)
                print("Row updated successfully!")
                print()
            else:
                print("Invalid row number!")
        except ValueError:
            print()
            print("Please enter an integer value!")
    except FileNotFoundError:
        print(f"File '{file_name}' not found! Please create it first.")
        print()

#For Roles file
def delete_file_roles(file_name):
    #Delete a row from the CSV file
    try:
        #The file handling syntax below automatically open and closes the file and it is called as a 'file'
        with open(file_name, 'r') as file:
            rows = file.readlines()

        print("Existing rows:")
        row_index = 0
        for row in rows:
            print(f"{row_index}: {row.strip()}")
            row_index += 1

        row_number = int(input("Enter the row number to delete (starting from 0): "))

        if 0 <= row_number < len(rows):
            del rows[row_number]
            with open(file_name, 'w') as file:
                file.writelines(rows)
            print("Row deleted successfully!")
            print()
        else:
            print("Invalid row number!")

    except FileNotFoundError:
        print(f"File '{file_name}' not found! Please create it first.")
        print()

#For Roles file
def read_file_roles(file_name):
    #Read and display the contents of the CSV file
    try:
        #The file handling syntax below automatically open and closes the file and it is called as a 'file'
        with open(file_name, 'r') as file:
            rows = file.readlines()
            print("\nContents of the file:")
            for row in rows:
                print(row.strip())
            print()
    except FileNotFoundError:
        print(f"File '{file_name}' not found! Please create it first.")
        print()

#Select a specific roles file
def select_role():
    try:
        #A dictionary storage type that stores a key:value pair of each role files according to the number assigned as seen below
        roles = {
            "1": "Doctors.csv",
            "2": "Nurse.csv",
            "3": "Receptionist.csv"
        }
        print()
        print("Select Role:")
        print("1. Doctor")
        print("2. Nurse")
        print("3. Receptionist")

        choice = input("Enter your choice: ")
        return roles.get(choice, None)
    except ValueError:
        print("Please enter the value as instructed! ")

def get_role_specific_input(role):
    #Asks the user for a role-specific input based on the role
    if role == "Doctors.csv":
        print("Enter details in the format:Doctor_ID, Name, Specialization, Years of Experience, Contact Number, Available Hours")
    elif role == "Nurse.csv":
        print("Enter details in the format:Nurse_ID, Name, Department, Years of Experience, Contact Number, Shift Hours")
    elif role == "Receptionist.csv":
        print("Enter details in the format:Receptionist_ID, Name, Contact Number, Years of Experience, Office Hours")
    return input("Enter the new role details: ")


#For managing user accounts configuration
def admin_config_manage_user_accounts():
    #The function of 'while True' forces the user to repeat the input process and will only stop when a 'break' is called
    while True:
        print("-"*60)
        print("\nWhat would you like to do with the user account? ")
        print("Create (Type C)")
        print("Add (Type A)")
        print("Update (Type U)")
        print("Delete (Type D)")
        print("Read (Type R)")
        print("Exit (Type Exit)")
        print("-"*60)
        print()
        admin_manage_user_ans = input("Enter the action from the list above > ").lower()
        if admin_manage_user_ans in {"c", "a", "u", "d", "r"}:
            file_name = select_role()
            if file_name is None:
                print("The role selected is invalid, Please try again! ")
                continue
            if admin_manage_user_ans == "c":
                create_file_roles(file_name)
            elif admin_manage_user_ans == "a":
                new_data = get_role_specific_input(file_name)
                #new_header = input("Enter  new roles using the format above! \n>")
                add_file_roles(file_name, new_data)
            elif admin_manage_user_ans == "u":
                update_file_roles(file_name)
            elif admin_manage_user_ans == "d":
                delete_file_roles(file_name)
            elif admin_manage_user_ans == "r":
                read_file_roles(file_name)
            elif admin_manage_user_ans == "exit":
                break
        elif admin_manage_user_ans == "exit":
                break
        else:
            print("Please enter a valid option from the list above! ")
            print()

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

#For viewing Hospital statistics configuration
def admin_config_view_stats():
    while True:
        try:
            print("-"*60)
            print("Would you like to view the Hospital statistics")
            print("Yes (Type y)")
            print("No (Type n)")
            print("Exit (Type exit)")
            print("-"*60)
            print()
            admin_view_stats_ans = input("Enter the action from the list above > ").lower()
            file_name_resource = "hospital_resources.csv"
            file_name_roles = "Doctors.csv"
            if admin_view_stats_ans == "y":
                patients = [patient1_record, patient2_record, patient3_record, patient4_record, patient5_record]
                read_file_resources(file_name_resource)
                read_file_roles(file_name_roles)
                read_patient_content(patients)
                indexing_patient(patients)
                break
            elif admin_view_stats_ans == "n" or "exit":
                break
        except ValueError:
            print("Please enter either 'y' or 'n' in the options above")
    
#For generating files configuration 
def admin_config_gen_usage_occuprate():
    while True:
        try:
            input_filename = "hospital_resource.csv"
            output_filename = "hospital_data_output.csv"
            with open(input_filename, "r") as input_file:
                data = input_file.readlines()
            with open(output_filename, "w") as output_file:
                for line in data:
                    output_file.write(line)
            print(f"Data successfully written to {output_filename} from {input_filename}.")
        except FileNotFoundError:
            print(f"Error: The file {input_filename} was not found, Please create it first!")
        usage_ans = input("Would you like to generate a report on the usage and occupancy rate of the Hospital? (Yes or No) \n> ").lower()
        if usage_ans == "yes" or "y":
            generate_hospital_report(output_filename)
            break
        elif usage_ans == "no" or "n" or "exit":
            print("Thank you, exiting...")
            break

# Read the hospital data from the output CSV file and display a report
def generate_hospital_report(filename):
    print(f"{'Resource':<30} {'Total':<10} {'Occupied':<10} {'Available':<10} {'Under_Maintenance':<10}")
    print("-" * 80)
    try:
        with open(filename, "r") as file:
            # Skip the header row
            lines = file.readlines()[1:]
            for line in lines:
                columns = line.strip().split(",")
                resource = columns[0]
                total = columns[1] if len(columns) > 1 and columns[1] else "N/A"
                occupied = columns[2] if len(columns) > 2 and columns[2] else "N/A"
                available = columns[3] if len(columns) > 3 and columns[3] else "N/A"
                under_maintenance = columns[4] if len(columns) > 4 and columns[4] else "N/A"
                
                print(f"{resource:<30} {total:<10} {occupied:<10} {available:<10} {under_maintenance:<10}")
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")

#For Resources file
def create_file_resources(file_name):
    """Create a new CSV file with headers
    The error handling syntax below automatically open and closes the file and it is called as a 'file'"""
    try:
        with open(file_name, 'w') as file:
            headers = input("Enter column headers for resource separated by commas: ")
            file.write(headers + '\n')
        print(f"File '{file_name}' created successfully!")
        print()
    except FileExistsError:
        print(f"File {file_name} has already been created!")
        print()

#For Resources file
def read_file_resources(file_name):
    #Read and display the contents of the CSV file
    try:
        #The file handling syntax below automatically open and closes the file and it is called as a 'file'
        with open(file_name, 'r') as file:
            with open(file_name, "r") as file:
                resources = file.readlines()
                if len(resources) <= 1:  #Only if the header exists or file is empty
                    print("No resources available.")
                else:
                    print("\nCurrent Resources:")
                    counter = 1
                    for resource in resources[1:]:  #Skips the header and shows data below it
                        print(f"{counter}. {resource.strip()}")
                        counter += 1
    except FileNotFoundError:
        print(f"File '{file_name}' not found! Please create it first.")
        print()

#For Resources file
def add_file_resource(file_name, new_resource):
    #Adds a new resource to the file
    #The file handling syntax below automatically open and closes the file and it is called as a 'file'
    try:
        with open(file_name, 'a') as file:
            file.write(new_resource + '\n')
        print("Changes made successfully.")
        print()
    except Exception as e:
        print(f"An error occured while adding resource: {e}")

#For Resources file
def update_file_resource(file_name):
    #Update a specific row in the CSV file
    try:
        #The file handling syntax below automatically open and closes the file and it is called as a 'file'
        with open(file_name, 'r') as file:
            rows = file.readlines()
        print("Existing rows:")
        row_index = 0
        for row in rows:
            print(f"{row_index}: {row.strip()}")
            row_index += 1
        #Allows the user to edit a specific selected row by entering an integer value
        try:
            row_number = int(input("Enter the row number to update (starting from 0): "))
            if 0 <= row_number < len(rows):
                print(f"Current data: {rows[row_number].strip()}")
                new_data = input("Enter new data for this row, separated by commas: ")
                rows[row_number] = new_data + '\n'

                with open(file_name, 'w') as file:
                    file.writelines(rows)
                print("Row updated successfully!")
                print()
            else:
                print("Invalid row number!")
        except ValueError:
            print()
            print("Please enter an integer value!")
    except FileNotFoundError:
        print(f"File '{file_name}' not found! Please create it first.")
        print()

#For Resources file
def delete_file_resource(file_name):
    #Delete a row from the CSV file
    try:
        #The file handling syntax below automatically open and closes the file and it is called as a 'file'
        with open(file_name, 'r') as file:
            rows = file.readlines()
        print("Existing rows:")
        row_index = 0
        for row in rows:
            print(f"{row_index}: {row.strip()}")
            row_index += 1
        row_number = int(input("Enter the row number to delete (starting from 0): "))
        if 0 <= row_number < len(rows):
            del rows[row_number]
            with open(file_name, 'w') as file:
                file.writelines(rows)
            print("Row deleted successfully!")
            print()
        else:
            print("Invalid row number!")
    except FileNotFoundError:
        print(f"File '{file_name}' not found! Please create it first.")
        print()

#For managing resources configuration (not done)
def admin_config_manage_resources():
    while True:
        try:
            file_name = "hospital_resources.csv"
            print("-"*60)
            print("What would you like to do? ")
            print("Create (Type C)")
            print("Add (Type A)")
            print("Delete beds (Type D)")
            print("Update facility status (Type U)")
            print("Read (Type R)")
            print("Exit (Type exit)")
            print("-"*60)
            admin_manage_resources_ans = input("What action would you like to do? > ").lower()
            if admin_manage_resources_ans == "c":
                create_file_resources(file_name)
            elif admin_manage_resources_ans == "a":
                print("Resource, Total, Occupied, Available, Under_Maintenance")
                print("Enter the resource in the given format above!\n")
                new_resource = input("Enter a new resource you would like to add! \n> ")
                add_file_resource(file_name, new_resource)
            elif admin_manage_resources_ans == "d":
                delete_file_resource(file_name)
            elif admin_manage_resources_ans == "u":
                update_file_resource(file_name)
            elif admin_manage_resources_ans == "r":
                read_file_resources(file_name)
            elif admin_manage_resources_ans == "exit":
                break
        except ValueError:
            print("Please enter from the given option above! ")

#For Policies file
def read_policies(file_name):
    #Reads and displays all policies from the file
    try:
        #The file handling syntax below automatically open and closes the file and it is called as a 'file'
        with open(file_name, 'r') as file:
            policies = file.readlines()
            if not policies:
                print("No policies available.")
            else:
                print("\nCurrent Policies:")
                counter = 1
                for policy in policies:
                    print(f"{counter}. {policy.strip()}")
                    counter += 1
    except FileNotFoundError:
        print("No policy file found. Creating a policy file.")
        print()

#For Policies file
def add_policies(file_name, policy):
    """Add a new policy to the file,
    The file handling syntax below automatically open and closes the file and it is called as a 'file'"""
    with open(file_name, 'a') as file:
        file.write(policy + '\n')
    print("Policy added successfully.")
    print()

#For Policies file
def update_policy(file_name, policy_number, updated_policy):
    #Updates an existing policy
    try:
        #The file handling syntax below automatically open and closes the file and it is called as a 'file'
        with open(file_name, 'r') as file:
            policies = file.readlines()
        if 1 <= policy_number <= len(policies):
            policies[policy_number - 1] = updated_policy + '\n'
            with open(file_name, 'w') as file:
                file.writelines(policies)
            print("Policy updated successfully.")
        else:
            print("Invalid policy number.")
    except FileNotFoundError:
        print("Policy file does not exist. Unable to update.")
        print()

#For Policies file
def delete_policy(file_name, policy_number):
    #Deletes a policy from the file
    try:
        #The file handling syntax below automatically open and closes the file and it is called as a 'file'
        with open(file_name, 'r') as file:
            policies = file.readlines()

        if 1 <= policy_number <= len(policies):
            del policies[policy_number - 1]
            with open(file_name, 'w') as file:
                file.writelines(policies)
            print("Policy deleted successfully.")
        else:
            print("Invalid policy number.")
    except FileNotFoundError:
        print("Policy file does not exist. Unable to delete.")
        print()

#For Policies configuration
def admin_config_oper_rules():
    file_name = "Hospital_Policies.txt"
    #The function of 'while True' forces the user to repeat the input process and will only stop when a 'break' is called
    while True:
        print("-"*60)
        print("What would you like to do with the Operational Rules/Policies? ")
        print("Read (Type R)")
        print("Add (Type A)")
        print("Update (Type U)")
        print("Delete (Type D)")
        print("Exit (Type exit)")
        print("-"*60)
        admin_oper_rules_ans = input("What action would you like to do? > ").lower()
        if admin_oper_rules_ans == "r":
            read_policies(file_name)
        elif admin_oper_rules_ans == "a":
            policy = input("Enter the new policy: ")
            add_policies(file_name, policy)
        elif admin_oper_rules_ans == "u":
            try:
                #The line below allows the user to edit a specified row of the policy
                try: 
                    policy_number = int(input("Enter the policy number to update: "))
                except ValueError:
                    print()
                    print("Please enter an integer value!")
                #The line below allows the user to update the previous policy
                updated_policy = input("Enter the updated policy: ")
                update_policy(file_name, policy_number, updated_policy)
            except ValueError:
                print("Invalid input, please enter an integer value for the policy number.")
        elif admin_oper_rules_ans == "d":
            try:
                #The line below allows the user to delete a specified row of the policy
                policy_number = int(input("Enter the policy number to delete: "))
                delete_policy(file_name, policy_number)
            except ValueError:
                print("Invalid input. Please enter a numeric value for the policy number.")
        elif admin_oper_rules_ans == "exit":
            print("Exiting the program! ")
            break
        else:
            print("Invalid value, please enter from the options above! ")
            print()