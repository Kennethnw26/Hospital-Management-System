def Recept_auth() : #This serves as a security measure
    try:
        Receptname = str(input("Enter your name: "))

        print("Hello Receptionist",Receptname)
        RPass = input("Enter the password here to verify yourself! or enter 'exit' to exit the program: ")
        if RPass == "receptionist12345":#This is to compare the user's input and the value given
            print()
            print("Hello",Receptname, "Welcome back! ")
            print()
        elif RPass.lower() == "exit":
            exit()
        else:
            print("Value inputted is invalid") 
    except:
        print()
        print("Error You should try again!")
        print()

def Recept_choice(Receptname): #This is the Receptionists menu
    print(f"Welcome Receptionist {Receptname}. Please select an action you would like to proceed to\n"
            f"Register new patient or update existing patient information.......................(1)\n"
            f"Schedule and manage appointments for doctors......................................(2)\n"
            f"Display the hospital's information................................................(3)\n"
            f"Check-in/out patients.............................................................(4)\n"
            f"Generate Billing..................................................................(5)\n"
            f"Exit..............................................................................(6)\n")

def readPinfo():  #This function is to read patient_data.txt and make it a list
    with open("patient_data.txt", "r") as O_PatientInfo:
        O_PatientInfo = O_PatientInfo.readlines()
        PatientList = [line.strip().split(",") for line in O_PatientInfo]
    return PatientList

def writePinfo(PatientList): #This is to write the data inside to a list
    with open("patient_data.txt", "w") as O_PatientInfo:
        for row in PatientList:
            O_PatientInfo.write(",".join(row) + "\n")

def addPatient(): #This function is to add patient info
    PatientList = readPinfo()
    Patient_ID = input("Enter the new patient ID: ").upper() #The whole code is just to get user input 
    name = input("Enter the new patient's name: ") 
    while True:
        try:
            age = int(input("Enter the new patient's age: "))
            break
        except:
            print()
            print("Error You should try again!")
            print()
    birth_date= input("Enter the new patient's date of birth: ")
    address= input ("Enter the new patient's address: ")
    contact_number= input ("Enter the new patient's contact number: ")
    insurance= input ("Enter the new patient's insurance plan: ")
    #The code below is to put the user input inside a list and print out the list
    new_patient= [Patient_ID, name, str(age), birth_date, address, contact_number, insurance]
    print(new_patient) 
    PatientList.append(new_patient)
    writePinfo(PatientList)
    print("Data updated successfully!")

def editPatient():#This function is to edit the patient data in the patient_data.txt
    while True:
        try: #To compare the patient id from user and the one from file
            PatientList = readPinfo() 
            for patientD in PatientList:
                print(patientD)
            print("\n")
            Patient_ID = input("Enter the patient ID to edit: ").upper()
            for patientData in PatientList:
                if patientData[0] != Patient_ID:
                    if PatientList.index(patientData) == len(PatientList)-1:
                        print("patient ID does not exist")
                    else:
                        pass
                elif patientData[0] == Patient_ID: #Print queries to get the new data from user and put them in a list
                    print(f"Current information for {Patient_ID}: {patientData}")
                    name = input(f"Enter the new name (current: {patientData[1]}): ") or patientData[1]
                    age = input(f"Enter the new age (current: {patientData[2]}): ") or patientData[2]
                    birth_date = input(f"Enter the new date of birth (current: {patientData[3]}): ") or patientData[3]
                    address = input(f"Enter the new address (current: {patientData[4]}): ") or patientData[4]
                    contact_number = input(f"Enter the new contact number (current: {patientData[5]}): ") or patientData[5]
                    insurance = input(f"Enter the new insurance plan (current: {patientData[6]}): ") or patientData[6]
                    patientData[1] = name
                    patientData[2] = age
                    patientData[3] = birth_date
                    patientData[4] = address
                    patientData[5] = contact_number
                    patientData[6] = insurance
                    #The code below writes the list in the text file and also print it out
                    writePinfo(PatientList) 
                    print(patientData)
                    print("Patient information updated successfully!")
                    break
        except:
            print()
            print("Error You should try again!")
            print()
            break

def patient_info_change(): #This act as a new branch of menu from the main one
    while True:
        print("1.\tRegister new patient data","\n2.\tUpdate previous patient data", "\n3.\tExit")
        choice_1_1 = input("Please pick the number that is correlated to your choice: ")
        if choice_1_1 == "1":
            addPatient()
        elif choice_1_1 == "2":
            editPatient()
        elif choice_1_1 == "3":
            break
        else:
            print("please pick the numbers between 1-3")

def readAinfo():  #This function is to read appointments.txt and make it a list
    with open("appointments.txt", "r") as O_AppointmentInfo:
        O_AppointmentInfo = O_AppointmentInfo.readlines()
        AppointmentList = [line.strip().split(",") for line in O_AppointmentInfo]
    return AppointmentList

def writeAinfo(AppointmentList):  #This function is to write the data inside to a list
    with open("appointments.txt", "w") as O_AppointmentInfo:
        for row in AppointmentList:
            O_AppointmentInfo.write(",".join(row) + "\n")

def add_appointment(): 
    while True:
        print() #Asks for user input to add to the lists
        newAppointment = input("Enter new appointment (code, date, time, Dr's name) or type 'exit' to exit: ")
        if newAppointment == "exit":
            break
        else: #
            print("You entered:", newAppointment)
            x = input("Is this correct? (yes/no): ").lower()
            if x == "yes":
                try: #Updates the list with the user input
                    AppointmentList = readAinfo()
                    newlist = newAppointment.split(",")
                    AppointmentList.append(newlist)
                    with open("appointments.txt", "w") as O_AppointmentInfo:
                        for row in AppointmentList: 
                            O_AppointmentInfo.write(",".join(row) + "\n")
                    print("Appointment added successfully!")
                    for Appointment in AppointmentList:
                        print(Appointment, "\n")
                except:
                    print()
                    print("Error You should try again!")
                    print()
                    break
            elif x == "no":
                continue

def appointment_change(): #Change the appointment date for user input patient codes that are the same as the one on the list
    AppointmentList = readAinfo()
    for item in AppointmentList:
        print(item, "\n")
    x = input("Enter the patient code you want to change: ")
    for item in AppointmentList:
        if item[0] == x:
            print("Current Information: ", item)
            new_date = input("Enter the new date: ")
            new_time = input("Enter the new time: ").upper()
            new_doctor = input("Enter the new doctor's name: ")
            item[1] = new_date
            item[2] = new_time 
            item[3] = new_doctor
            writeAinfo(AppointmentList)
            print("Appointment updated successfully!")
            return

def schedule_change(): #This act as a new branch of menu from the main one and also give the output needed
    while True:
        print("1.\tAdd a new appointment", "\n2.\tManage appointments","\n3.\tExit")
        try: #
            choice_1_2 = input("Please pick the number that is correlated to your choice: ")
            if choice_1_2 == "1":
                add_appointment()
            elif choice_1_2 == "2":
                appointment_change()
            elif choice_1_2 == "3":
                break
            else:
                print("please pick the numbers between 1-3")
        except:
            print()
            print("Error You should try again!")
            break

def readPcheck():
    while True:  #This function is to read checkioutn.txt and make it a list
        with open("checkioutn.txt", 'r') as O_checkinout:
            lines = O_checkinout.readlines()
            data = [line.strip().split(', ') for line in lines]
        return data

def checkstatus(data, PCode, status): #Check the value of item inside a list in a text file
    for item in data:
        if item[0] == PCode:
           item[1] = status
           return item

def writePcheck(): #Gets the code from the text file and comparing them with the user's input 
    data = readPcheck()
    PCode = input("Enter the Patient Code to check: ").upper()
    Status= None
    for item in data:
        if item[0] == PCode:
            Status= item
    while True:
        #Depending on the user's input it may update the list or not
        if Status:
            print("Status: ",Status)
            newPstatus = input("Enter the new status (check-in/check-out): ")
            updated_item = checkstatus(data, PCode, newPstatus)
            print("New Status: ",updated_item)
            x= input("Is this correct? (yes/no): ").lower()
            try:
                if x== "yes":
                    print("Status Updated!")
                    break
                elif x=="no":
                    continue
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                    continue
            except:
                print("Error!, reverting to previous choice")
        else:
            print(PCode,"is not in the list.")
            continue
        with open("checkioutn.txt", "w") as file: #Write the list to the txt file
            for item in data:
                file.write(', '.join(item) + '\n')

def check_patient(): #This act as a new branch of menu from the main one and also give the output needed
    while True:
        print("1.\tCheck In/Out Patient", "\n2.\tExit")
        try:
            choice_1_3 = input("Please pick the number that is correlated to your choice: ")
            if choice_1_3 == "1":
                writePcheck()
            elif choice_1_3 == "2":
                break
            else:
                print("please pick the numbers between 1-3")
        except:
            print()
            print("Error You should try again!")
            break

def readHInfo(): #This function is to read hospital_info.txt and make it a list
    with open("Hospital_info.txt", "r") as O_HInfo:
        O_HInfo= O_HInfo.readlines()
        HospitalList = [line.strip().split(",") for line in O_HInfo]
    return HospitalList

def info(): #This act as a new branch of menu from the main one
    while True:
        print("1.\tHospital services", "\n2.\tDoctors","\n3.\tDepartments", "\n4.\tExit")
        choice_1_4 = input("Pick your choice: ")
        try: #The code below is comparing the user input and also print out the data from the 
            if choice_1_4 == "1":
                list= readHInfo()
                for x in list:
                    print()                    
                    print(x[0])
            elif choice_1_4 == "2":
                list= readHInfo()
                for x in list:
                    print()                    
                    print(x[1])
            elif choice_1_4 == "3":
                list= readHInfo()
                for x in list:
                    print()
                    print(x[2])
            elif choice_1_4 =="4":
                break
            else:
                print("please pick the numbers between 1-3")
                break
        except:
            print("Error You should try again!")
            break

def readBilling(): #This function is to read billing_details.txt and make it a list
    with open("billing_details.txt", "r") as O_BInfo: 
        O_BInfo= O_BInfo.readlines()
        HospitalList = [line.strip().split(",") for line in O_BInfo]
    return HospitalList

def infoBilling(): #This function is to print out billing
    list_billing = readBilling()
    PCode = input("Enter the patient code, you want to see the billing of: ")
    for item in list_billing:
        try:
            if item[0] == PCode: #This code is to compared the user input patient code and the patient code in the text file
                print()
                print("Billing details of Patient", PCode, ":", item)
                break
            else: #To catch code that isn't in txt file
                print()
                print("Patient code", PCode, "not found.")
        except: #To catch error
            print()
            print("Error please try again!")