# PATIENT ROLE (TP080151 - VIONNA GAU)

from AdminConfig import check_insurance
def read_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            data = [line.strip().split(',') for line in lines]
        return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. \nCreating a new file.")
        write_data_to_file(filename, []) # Create a new file with empty content
        return [] # Return an empty list after creating the file

def write_data_to_file(filename, data):
    with open(filename, 'w') as file:
        for line in data:
            file.write(','.join(line) + '\n')
    print(f"Data written to '{filename}' successfully.")

def access_personal_medical_records():
    patient_id = input("\nEnter your patient ID [PXXXXX]: ").upper()
    records = read_data_from_file("medical_records.txt")
    patient_records = [record for record in records if record[0] == patient_id]

    if patient_records:
        print("\nYour Medical Records >>")
        for record in patient_records:
            print(f"Diagnosis: {record[1]} | Prescription: {record[2]}")
    else:
        print("No records found for the given patient ID.")

def view_upcoming_appointments():
    patient_id = input("\nEnter your patient ID [PXXXXX]: ").upper()
    appointments = read_data_from_file("appointments.txt")
    patient_appointments = [appointment for appointment in appointments if appointment[0] == patient_id]

    if patient_appointments:
        print("\nYour Upcoming Appointments >>")
        for appointment in patient_appointments:
            print(f"Name: {appointment[1]} | Date: {appointment[2]} | Time: {appointment[3]} | Doctor: {appointment[4]}")
    else:
        print("No upcoming appointments found.")

def patient_interaction():
    csv_file = "insurance_data.csv"
    with open(csv_file, "r") as file:
        rows = file.readlines()
        for row in rows:
            print(row.strip())
        print()
    print("Welcome to the hospital system.")
    print("Do you want to file an insurance claim? (yes/no)")
    claim_choice = input().strip().lower()
    
    if claim_choice == "yes" or claim_choice == "y":
        while True:
            print("Enter your policy holder name:")
            Policy_holder_name = input().strip()
            print("Enter your policy number:")
            Policy_number = input().strip()
            
            # Call the admin function of check_insurance to check insurance_data.csv content
            status = check_insurance(Policy_holder_name, Policy_number)
            
            if status == "approved":
                print("You can now get a queue number for your appointment.")
                break
            elif status == "not approved":
                print("Insurance claim is not approved. You can pay for yourself or cancel the visit.")
                print("Do you want to try again? (yes/no)")
                try_again = input().strip().lower()
                if try_again != "yes" or try_again != "y":
                    print("Visit canceled.")
                    break
            elif status == "not found":
                print("Invalid policy details. Try again or cancel the visit.")
                print("Do you want to try again? (yes/no)")
                try_again = input().strip().lower()
                if try_again != "yes" or try_again != "y":
                    print("Visit canceled.")
                    break
            elif status == "error":
                print("System error. Please contact administration.")
                break
    else:
        print("You have no insurance. You have to pay by yourself.")
        print("You can now get a queue number for your appointment.")

def schedule_appointment():
    patient_id = input("\nEnter your patient ID [PXXXXX]: ").upper()

    if not insurance_check(patient_id):
        print("Appointment scheduling canceled.")
        return

    try:
        with open("appointments.txt", "r") as file:
            existing_appointments = file.readlines()
    except FileNotFoundError:
        existing_appointments = []

    patient_id_exists = False
    existing_appointment_index = None
    for i, appointment in enumerate(existing_appointments):
        if patient_id in appointment:
            patient_id_exists = True
            existing_appointment_index = i
            break

    while patient_id_exists:
        if patient_id_exists:

            # If there's existing appointment (Patient_ID exists)
            if check_agreement_status(patient_id):
                print("\nStatus : Have Agreed to Queuing Policy")

                edit_appointment = input(f"\nPatient ID {patient_id} already has an appointment. \nDo you want to edit the existing appointment? (y/n): ")
                if edit_appointment.lower() == 'y':
                    # Existing appointment details
                    existing_appointment = existing_appointments[existing_appointment_index].strip().split(",")
                    print(f"\nYour current appointment >> \nName: {existing_appointment[1]} | Date: {existing_appointment[2]} | Time: {existing_appointment[3]} | Doctor: {existing_appointment[4]}")

                    new_date = input("Enter new appointment date [YYYY-MM-DD] / Press (ENTER) to keep the current data: ")
                    new_time = input("Enter new appointment time [HH:MM] / Press (ENTER) to keep the current data: ")
                    new_doctor = input(str("Enter new doctor's name / Press (ENTER) to keep the current data: "))

                    if new_date:
                        existing_appointment[2] = new_date
                    if new_time:
                        existing_appointment[3] = new_time
                    if new_doctor:
                        existing_appointment[4] = new_doctor

                    # Update appointment in the list
                    existing_appointments[existing_appointment_index] = ",".join(existing_appointment) + "\n"  # Add newline back

                    # Overwrite/Edit file with updated appointments
                    with open("appointments.txt", "w") as file:
                        file.writelines(existing_appointments)

                    print("Appointment updated successfully!")
                    return
                else:
                    print("Appointment scheduling canceled.")
                    return

            elif not check_agreement_status(patient_id):
                print("\nStatus : Have Not Agreed to Queuing Policy")

        # If there's no existing appointment (Patient_ID does not exist)
        # ADDITIONAL FEATURE 1 (QUEUING POLICY)
            display_queue_rules()

            if not get_user_agreement():
                print("You are not allowed to proceed.")
                return update_agreement_status(patient_id, False)

            else:
                print("You are allowed to proceed.")
                update_agreement_status(patient_id, True)
                return True

    # If there's no existing appointment (Patient_ID does not exist)
    # ADDITIONAL FEATURE 1 (QUEUING POLICY)
    display_queue_rules()

    if not get_user_agreement():
        print("You are not allowed to proceed.")
        return update_agreement_status(patient_id, False)

    else:
        print("You are allowed to proceed.")
        update_agreement_status(patient_id, True)

    name = input(str("\nEnter your name: "))
    date = input("Enter appointment date [YYYY-MM-DD]: ")
    time = input("Enter appointment time [HH:MM]: ")
    doctor = input(str("Enter doctor's name: "))

    new_appointment = [patient_id, name, date, time, doctor]

    with open("appointments.txt", "a") as file:
        file.write(",".join(new_appointment) + "\n")

    print("Appointment scheduled successfully!")

def delete_appointment():
    patient_id = input("\nEnter your patient ID [PXXXXX]: ").upper()

    with open("appointments.txt", "r") as file:
        appointments = file.readlines()

    updated_appointments = [appointment for appointment in appointments if patient_id not in appointment]

    with open("appointments.txt", "w") as file:
        file.writelines(updated_appointments)

    print("Appointment deleted successfully!")

def update_personal_information():
    patient_id = input("\nEnter your patient ID [PXXXXX]: ").upper()
    info = read_data_from_file("patient_info.txt")

    for i, record in enumerate(info):
        if record[0] == patient_id:
            print(f"\nYour Current Information >> \nAddress: {record[1]} | Contact: {record[2]} | Insurance: {record[3]}")

            new_address = input("Enter new address / Press (ENTER) to keep the current data: ")
            new_contact = input("Enter new contact number [0XX-XXXXXXX] / Press (ENTER) to keep the current data: ")
            new_insurance = input("Enter new insurance details / Press (ENTER) to keep the current data: ")

            if new_address:
                record[1] = new_address
            if new_contact:
                record[2] = new_contact
            if new_insurance:
                record[3] = new_insurance

            info[i] = record
            write_data_to_file("patient_info.txt", info)
            print("Information updated successfully!")
            return

    print("Patient ID not found.")

def request_specific_services():
    patient_id = input("\nEnter your patient ID [PXXXXX]: ").upper()

    try:
        with open("service_requests.txt", "r") as file:
            existing_requests = file.readlines()
    except FileNotFoundError:
        existing_requests = []

    patient_id_exists = False
    for request in existing_requests:
        if patient_id in request:
            patient_id_exists = True
            break

    if patient_id_exists:
        add_request = input(f"Patient ID {patient_id} already has a service request. \nWould you like to add another request? (y/n): ")
        if add_request.lower() != 'y':
            print("Request canceled.")
            return

    service_type = input(str("Enter service type (>> Consultation, Prescription refill, etc): "))
    service_detail = input("Enter details of your request: ")

    new_request = f"{patient_id},{service_type},{service_detail}\n"

    # Insert new request while maintaining order
    inserted = False
    for i, request in enumerate(existing_requests):
        if patient_id < request.split(",")[0]:
            existing_requests.insert(i, new_request)
            inserted = True
            break

    if not inserted:
        existing_requests.append(new_request)

    with open("service_requests.txt", "w") as file:
        file.writelines(existing_requests)

    print("Your request has been submitted.")

def access_billing_details():
    patient_id = input("\nEnter your patient ID [PXXXXX]: ").upper()
    billing_details = read_data_from_file("billing_details.txt")
    patient_billing = [detail for detail in billing_details if detail[0] == patient_id]

    if patient_billing:
        print("\nYour billing details >>")
        for detail in patient_billing:
            print(f"Insurance Provider: {detail[1]} | Outstanding Balance: {detail[2]}")
    else:
        print("No billing details found.")

def view_payment_history():
    patient_id = input("\nEnter your patient ID [PXXXXX]: ").upper()
    payment_history = read_data_from_file("payment_history.txt")
    patient_payment = [data for data in payment_history if data[0] == patient_id]

    if patient_payment:
        print("\nYour payment history >>")
        for data in patient_payment:
            print(f"Date: {data[1]} | Amount: {data[2]} | Payment Method: {data[3]}")
    else:
        print("No payment history found.")

def display_queue_rules():
    print("\nQueuing Rules >>")
    print("-"*80)
    print("1. Please maintain order and respect your queue number.")
    print("2. Avoid cutting the queue or attempting to bribe staff.")
    print("3. Patients are responsible for their own belongings.")
    print("4. If you need to leave your place in line temporarily, inform the staff.")
    print("5. Follow instructions from the staff at all times.")
    print("-"*80)

def get_user_agreement():
    while True:
        agreement = input("Do you agree to follow the queuing rules? (y/n): ").lower()
        if agreement == 'y':
            print("\nStatus : Queuing Policy Accepted")
            return True
        elif agreement == 'n':
            print("\nStatus : Queuing Policy Denied")
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
        break

def update_agreement_status(patient_id, agreed):
    try:
        with open("patient_agreements.txt", "r") as file:
            existing_agreements = file.readlines()
    except FileNotFoundError:
        existing_agreements = []

    found = False
    for i, line in enumerate(existing_agreements):
        if patient_id in line:
            existing_agreements[i] = f"{patient_id},{agreed}\n"
            found = True
            break

    if not found:
        existing_agreements.append(f"{patient_id},{agreed}\n")

    with open("patient_agreements.txt", "w") as file:
        file.writelines(existing_agreements)

def check_agreement_status(patient_id):
    agreements = read_data_from_file("patient_agreements.txt")
    for record in agreements:
        if record[0] == patient_id and len(record) > 1:
            return record[1] == "True"
    return False

def generate_reports():
    doctor_name = input("Enter doctor's name: ")

    with open("appointments.txt", "r") as file:
        appointments = file.readlines()

    doctor_appointments = [appointment for appointment in appointments if doctor_name in appointment]

    if doctor_appointments:
        print(f"\nAppointment Report for Dr. {doctor_name}:")
        for appointment in doctor_appointments:
            details = appointment.strip().split(",")
            print(f"Patient ID: {details[0]} | Name: {details[1]} | Date: {details[2]} | Time: {details[3]}")
    else:
        print(f"No appointment reports found for Dr. {doctor_name}.")

def insurance_check(patient_id):
    try:
        with open("patient_info.txt", "r") as file:
            patient_data = [line.strip().split(",") for line in file.readlines()]
    except FileNotFoundError:
        print("Error: Patient information file not found.")
        return False

    for patient in patient_data:
        if patient[0] == patient_id:
            insurance_company = patient[3]  # Insurance company is in the 4th column
            policy_number = input("Enter your insurance policy number: ")

            # Basic validation for policy number (adjust as needed)
            while not (8 <= len(policy_number) <= 10 and policy_number.isdigit()):
                print("Invalid policy number. Please enter an 8-10 digit number.")
                policy_number = input("Enter your insurance policy number: ")

            policy_holder_name = input("Enter policy holder name (uppercase): ").upper()

            # Simulate insurance company check (replace with actual API or integration)
            # This is a placeholder; replace with actual logic
            is_approved = True  # Replace with actual insurance company check

            if is_approved:
                print("Insurance claim approved.")
                return True
            else:
                print("Insurance claim not approved.")
                choice = input("Do you wish to proceed without insurance coverage? (y/n): ").lower()
                if choice == 'y':
                    return True  # Proceed without insurance
                else:
                    print("Appointment canceled.")
                    return False

    print("Patient ID not found.")
    return False

def patient_title():
    while True:
        print("\nPatient Menu >>")
        print("1. Access Personal Medical Records")
        print("2. View Upcoming Appointments")
        print("3. Schedule an Appointment")
        print("4. Delete an Appointment")
        print("5. Update Personal Information")
        print("6. Request Specific Services")
        print("7. Access Billing Details")
        print("8. View Payment History")
        print("9. Generate Doctor Appointment Reports")
        print("10. Request to claim insurance")
        print("11. Exit")

        choice = input(str("Enter your choice (1-10): "))
        while int(choice) > 11 or int(choice) < 1:
            print("Invalid choice. Please select a number from 1 to 10.")
            choice = input(str("Enter your choice (1-10): "))

        if choice == '1':
            access_personal_medical_records()
        elif choice == '2':
            view_upcoming_appointments()
        elif choice == '3':
            schedule_appointment()
        elif choice == '4':
            delete_appointment()
        elif choice == '5':
            update_personal_information()
        elif choice == '6':
            request_specific_services()
        elif choice == '7':
            access_billing_details()
        elif choice == '8':
            view_payment_history()
        elif choice == '9':
            generate_reports()
        elif choice == "10":
            patient_interaction()
        elif choice == '11':
            print("Exiting the Patient Title.")
            break
