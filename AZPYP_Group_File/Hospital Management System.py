#This serves as the only password that is acceptable to the machine and once the correct password is inputted, they can configure the data
admin_pass = "admin12345"

from AdminConfig import *
from patient_dictionary import *

def menu_list():
    #The function of 'while True' forces the user to repeat the input process and will only stop when a 'break' is called
    while True:
        try:  
                print("""
*********** MENU ***********
What are you signing in as?
1. Administrator
2. Doctor
3. Nurse
4. Receptionist
5. Patient
Exit (Type Exit)
""", end = "")
                user_role_ans = input("Enter the value as instructed above!  > ")
                #If the user enters any answer in the option section then the loop will terminate itself and proceed to the next command
                if user_role_ans == "1":
                    menu_continuation_admin(user_role_ans)
                elif user_role_ans == "2":
                    pass
                elif user_role_ans == "3":
                    pass
                elif user_role_ans == "4":
                    pass
                elif user_role_ans == "5":
                    pass
                elif user_role_ans.lower() == "exit":
                    print("Thank you! ")
                    exit()
                else:
                    print()
                    print("Invalid option! ")
        except ValueError:
            print("Invalid option! ")

def menu_continuation_admin(user_role_ans):
    #this is a sub menu for the administrator role, which will give options on what configuration the admin would like make
    try:
        if user_role_ans == "1":
            user_role_1()
            #The function of 'while True' forces the user to repeat the input process and will only stop when a 'break' is called
            while True:
                print("""
******** Lists of Functions *********
1. Manage user accounts 
2. View Hospital Statistics 
3. Generate Hospital usage and Occupancy rates 
4. Manage hospital resources 
5. Operational Rules or Policies for the Hospital System 
6. Manage Insurance Policy
                """)
                admin_config_ans = input("What configuration would you like to do? (Enter the number as given) > ")
                print()
                options = ["1","2","3","4","5"]
                if admin_config_ans in options:
                    break
                elif admin_config_ans.lower() == "exit":
                    exit()
                else: 
                    print("PLease enter a valid option from the list above!")
            #if the admin configuration answer is from the given options then it will call a function to each specific action
            if admin_config_ans == "1":
                admin_config_manage_user_accounts()
            elif admin_config_ans == "2":
                admin_config_view_stats()
            elif admin_config_ans == "3":
                admin_config_gen_usage_occuprate()
            elif admin_config_ans == "4":
                admin_config_manage_resources()
            elif admin_config_ans == "5":
                admin_config_oper_rules()
            elif admin_config_ans == "6":
                check_insurance()
            else: 
                print("Please enter a valid option from the list above! ") 
    #this will act as a validation if the value inputted is from the list above or not   
    except ValueError:
        print("The value you entered is invalid, please try again! ")

menu_list()
