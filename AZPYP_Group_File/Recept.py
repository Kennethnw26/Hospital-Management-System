
def ReceptMenu(): #Menu as a function to be imported
    import ReceptConfig
    Receptname = ReceptConfig.Recept_auth()
    while True:
        ReceptConfig.Recept_choice(Receptname)
        try:
            choice = input("-> ")
            if choice == "1" :
                ReceptConfig.patient_info_change()
            elif choice == "2" :
                ReceptConfig.schedule_change()
            elif choice == "3" :
                ReceptConfig.check_patient()
            elif choice == "4" :
                ReceptConfig.info()
            elif choice == "5" :
                ReceptConfig.infoBilling()
            elif choice == "6" or choice.lower() == "exit":
                print()
                exit()
            else :
                print("Invalid input")
        except ValueError :
            print("Invalid input")

            