import NurseConfig
def NurseMenu():
    while True:
        try:
            nurse_name = NurseConfig.authentication()
            choice = input(f"Welcome Nurse {nurse_name}. Please select an action you would like to proceed to\n"
                        f"Access a daily list of patients and their required care.......................(1)\n"
                        f"Update patient vitals and record observations.................................(2)\n"
                        f"Assist doctors by preparing rooms for treatment or surgical procedures........(3)\n"
                        f"Manage medication logs and ensure timely administration of medications........(4)\n"
                        f"Report any medical emergencies to the assigned doctor.........................(5)\n"
                        f"Exit..........................................................................(6)\n"
                        f"> ")
            if choice == "1" :
                NurseConfig.nurse_config_access_list_of_patients()
                break
            elif choice == "2" :
                NurseConfig.nurse_config_update_patient_vitals()
            elif choice == "3" :
                NurseConfig.nurse_config_prepare_room()
            elif choice == "4" :
                NurseConfig.nurse_config_manage_medication_log()
            elif choice == "5" :
                NurseConfig.nurse_config_report_medical_emergencies()
            elif choice == "6" or choice == "exit":
                print()
                break
            else :
                print("Invalid input")
        except ValueError :
            print("Invalid input")
