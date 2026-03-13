ColumnHeadersFile1 = ("ID","Name","Diagnosis","Prescriptions","Appointments","status","Assigned Doctor")
number_of_columns = len(ColumnHeadersFile1)

temp_var_1 = open("Doctor'sData.txt", "r")
temp_list_1 = temp_var_1.read().replace("\n", ",").split(",")
temp_var_1.close()

def DoctorMenu () :
    fix_data_1()
    fix_data_2()
    doctor_name=authentication()
    while True :
        try :
            # show options
            choice = input(f"\nWelcome Doctor {doctor_name}. Please select an action you would like to proceed to\n"
                      f"(Type the number associated to the action)\n"
                      f"{"View personal patient list":{"."}<80}(1)\n"
                      f"{"Update patient records with diagnosis, prescriptions, and treatment plans":{"."}<80}(2)\n"
                      f"{"Schedule follow-up appointments for patients":{"."}<80}(3)\n"
                      f"{"View medical history and treatment logs of assigned patients":{"."}<80}(4)\n"
                      f"{"Issue discharge approvals or recommend further hospital stay as needed":{"."}<80}(5)\n"
                      f"{"Exit":{"."}<80}(6)\n"
                      f"> ")
            # cases for option pick
            if choice == "1" :
                view_patient_list((0,1,2,3,6))
                choose_specific_patient_list()
            elif choice == "2" :
                update_patient_data()
            elif choice == "3" :
                add_appointment_schedule()
            elif choice == "4" :
                show_history()
            elif choice == "5" :
                status_set()
            elif choice == "6" or choice == "exit":
                print()
                break
            else :
                print("Value inputted is invalid")
        except ValueError :
            print("Value inputted is invalid")

def write_into_file (file,new_list) :
    # opens the same file twice
    temp_var2 = open(file,"r")
    number_of_columns3 = 0
    garbage_can = []
    # one to count number of lines
    for columns in temp_var2.readline().split(",") :
        number_of_columns3 += 1
        garbage_can.append(columns)
    temp_var2.close()
    open_write_file = open(file, "w")
    column_count = 0
    # write data into file
    for x in range(len(new_list)):
        # if it's the last data then print only data with no formatting
        if x == len(new_list) - 1:
            open_write_file.write(new_list[x].strip())
        # if it's the last data in a row then print new line
        elif column_count == (number_of_columns3 - 1) and x != (len(new_list) - 1):
            open_write_file.write(new_list[x].strip() + "\n")
            column_count = 0
        # if other data then print with coma
        elif x != len(new_list) and column_count != number_of_columns3:
            open_write_file.write(new_list[x].strip() + ",")
            column_count += 1
    open_write_file.close()

def fix_data_1 () :
    # get rid of any extra empty lines in a file
    temp_var_7 = open("appointments.txt", "r")
    temp_list_7 = temp_var_7.read().replace("\n", ",").split(",")
    temp_var_7.close()
    count = 0
    # check for any empty data in list
    for element in temp_list_7 :
        if element == "" :
            count += 1
    # pop last element since last element is always emtpy line
    for x in range(count) :
            temp_list_7.pop()
    write_into_file("appointments.txt",temp_list_7)

def fix_data_2 () :
    # open connecting files into 2 lists
    temp_var_8 = open("appointments.txt", "r")
    temp_list_8 = temp_var_8.read().replace("\n", ",").split(",")
    temp_var_8.close()
    temp_var_9 = open("Doctor'sData.txt", "r")
    temp_list_9 = temp_var_9.read().replace("\n", ",").split(",")
    temp_var_9.close()
    # copy data from file of different role onto doctor files
    for element1 in range(0,len(temp_list_8),5) :
        temp_list_9[14+((element1//5)*7)] = temp_list_8[element1]
    for element1 in range(1,len(temp_list_8),5) :
        temp_list_9[15+((element1//5)*7)] = temp_list_8[element1]
    for element1 in range(2,len(temp_list_8),5) :
        temp_list_9[18+((element1//5)*7)] = (temp_list_8[element1] + " | " + temp_list_8[element1 + 1])
    for element1 in range(4,len(temp_list_8),5) :
        temp_list_9[20+((element1//5)*7)] = temp_list_8[element1]
    write_into_file("Doctor'sData.txt",temp_list_9)


def dynamic_dynamic_whitespace (file = "Doctor'sData.txt") :
    #transfer file into list
    #find length of the longest word in list
    temp_var_ws = open(file, "r")
    temp_list_ws = temp_var_ws.read().replace("\n", ",").split(",")
    temp_var_ws.close()
    length = len(max(temp_list_ws,key = len))
    if length % 2 != 0 :
        length += 3
    elif length % 2 == 0 :
        length += 2
    return length
dynamic_dynamic_whitespace()

def authentication () :
    while True:
        #ask for username
        doctor_name = (input("Enter your name!\n"
                             "> "))
        print(f"\nHello Doctor {doctor_name}\n")
        while True:
            #ask for password
            doctor_input_pass = input(f"Enter the password here to verify yourself! \n"
                                      f"Enter 'exit' to exit the program \n\n"
                                      f"> ")
            if doctor_input_pass == "doctor12345":
                print()
                print(f"Hello {doctor_name}, Welcome back! ")
                break
            elif doctor_input_pass.lower() == "exit":
                print("\nThank you! ")
                exit()
            else:
                print("Value inputted is invalid")
                print()
        break
    #returns name of user logging in
    return doctor_name

def choose_specific_patient_list () :
    while True:
        #ask for ID of patient that will be viewed
        view_choice = input(f"Please enter the name or ID of the row you would like to view\n"
                            f"Please enter 'exit' to exit this action\n"
                            f"> ")
        try:
            #find position of that patient in the list
            index = temp_list_1.index(view_choice)
            print()
            # call function to show only that specific patient
            show_specific_patient_list("Doctor'sData.txt",index)
        except ValueError:
            if view_choice.lower() == "exit":
                print()
                break
            else:
                print("Value inputted is invalid")

def show_column_names (file, columns, number_of_columns1 = number_of_columns) :
    temp_var_show = open(file, "r")
    temp_list_show1 = temp_var_show.read().replace("\n", ",").split(",")
    temp_var_show.close()
    temp_list_show2 = []
    #append first 2 rows of header and separator
    for column2 in range(number_of_columns1 * 2):
        temp_list_show2.append(temp_list_show1[column2])
    #print first 2 rows of header and separator
    for count in range(2):
        for column2 in columns:
            print("|", end="")
            if temp_list_show2[(number_of_columns1 * count) + column2] == "_":
                print(temp_list_show2[(number_of_columns1 * count) + column2].strip().center((dynamic_dynamic_whitespace(file)),"_"),end="")
            else:
                print(temp_list_show2[(number_of_columns1 * count) + column2].strip().center((dynamic_dynamic_whitespace(file))," "),end="")
        print("|")

def show_specific_patient_list (file,index1,columns = (0, 1, 2, 3),number_of_columns1 = number_of_columns) :
    temp_var_specific = open(file, "r")
    temp_list_specific = temp_var_specific.read().replace("\n", ",").split(",")
    temp_var_specific.close()
    print()
    show_column_names(file, columns,number_of_columns1)
    #if name of patient is inputted, change index gotten to index of code
    if (index1 - 1) % number_of_columns1 == 0:
        index1 -= 1
    #print row of selected patient
    for column1 in columns:
        print("|", end="")
        print(temp_list_specific[index1 + column1].strip().center((dynamic_dynamic_whitespace(file)), " "), end="")
    print("|")
    #print last separator
    for x in range(-1, -(len(columns) + 1), -1):
        print("|", end="")
        print(temp_list_specific[x].strip().center((dynamic_dynamic_whitespace(file)), "_"), end="")
    print("|")

def view_patient_list (columns = (0, 1, 2, 3)) :
    count1 = 0
    count2 = 0
    garbage_bin = []
    temp_var_2 = open("Doctor'sData.txt", "r")
    # count how many rows of data is in the txt file
    for lines in temp_var_2.readlines():
        count1 += 1
        garbage_bin.append(lines)
    temp_var_2.close()
    print()
    # while there are still rows print
    while count2 < count1:
        for column in columns:
            # print starting separator
            print("|", end="")
            # if data is _ then print a separator
            if temp_list_1[(number_of_columns * count2) + column] == "_":
                print(temp_list_1[(number_of_columns * count2) + column].strip().center((dynamic_dynamic_whitespace()),"_"),end="")
            else:
            # print each data in cells
                print(temp_list_1[(number_of_columns * count2) + column].strip().center((dynamic_dynamic_whitespace())," "), end="")
        # print ending separator and next line
        print("|")
        count2 += 1
    print()

def update_patient_data (number_of_columns1 = number_of_columns) :
    def check_old_data (title, pos):
        # asks for new data
        change = input(f"\nEnter the updated {title}\n"
                       f"(Separate with commas for multiple values)\n"
                       f"> ").replace(",", "|")
        # fix spacing of words
        change_temp_list_1 = change.split("|")
        # find the longest word in data with multiple values
        length = len(max(change_temp_list_1, key=len))
        length //= 2
        index_check_old_data = 0
        # print spacing for left and right of data
        for things in change_temp_list_1:
            change_temp_list_1[index_check_old_data] = (" " * int(length)) + things + (" " * int(length))
            index_check_old_data += 1
        change = "|".join(change_temp_list_1)
        old = temp_list_1[index + pos]
        # find old data
        for value in range(index,index+number_of_columns1):
            # replace data when old data is found
            if temp_list_1[value] == old:
               temp_list_1[value] = change.replace("|","|".center(1," "))
    while True:
        try:
            index = 0
            name = input(f"\nPlease enter code or name of the patient whose record you would like to update\n"
                         f"Please enter 'exit' to exit this action\n"
                         f"> ")
            print()
            if name.lower() == "exit" :
                print()
                break
            else :
                # find index of patient id
                index = temp_list_1.index(name)
                if (index - 1) % number_of_columns1 == 0:
                    index -= 1
                show_specific_patient_list("Doctor'sData.txt",index)
            break
        except ValueError:
            print("Value inputted is invalid")
    while True:
        try:
            if name.lower() == "exit":
                print()
                break
            else :
                # ask which data is to be changed
                update_choice = input(f"\nWhich data of the selected patient would you like to change?\n"
                                          f"(Type the number associated to the data)\n"
                                          f"Please enter 'exit' to exit this action\n"
                                          f"{"Name":{"."}<80}(1)\n"
                                          f"{"Diagnosis":{"."}<80}(2)\n"
                                          f"{"Prescriptions":{"."}<80}(3)\n"
                                          f"> ")
                if update_choice == "1":
                    check_old_data("name", 1)
                elif update_choice == "2":
                    check_old_data("diagnosis", 2)
                elif update_choice == "3":
                    check_old_data("prescriptions", 3)
                elif update_choice.lower() == "exit" :
                    print()
                    break
                else:
                    print("Value inputted is invalid")
                write_into_file("Doctor'sData.txt",temp_list_1)
                show_specific_patient_list("Doctor'sData.txt",index)
        except ValueError:
            print("Value inputted is invalid")

def add_appointment_schedule (number_of_columns1 = number_of_columns) :
    index1 = 0
    temp_var_6 = open("appointments.txt", "r")
    temp_list_6 = temp_var_6.read().replace("\n", ",").split(",")
    temp_var_6.close()
    while True:
        try:
            # ask for id from user
            name = input(f"\nPlease enter code or name of the patient whose appointments you would like to update\n"
                         f"Please enter 'exit' to exit this action\n"
                         f"> ")
            if name.lower() == "exit" :
                index = 0
                print()
                break
            else :
                # format index into id index if name is given
                index = temp_list_1.index(name)
                index1 = temp_list_6.index(name)
                if (index - 1) % number_of_columns1 == 0:
                    index -= 1
                if (index1 - 1) % 5 == 0:
                    index1 -= 1
                show_specific_patient_list ("Doctor'sData.txt",index,(0,1,4))
                print()

            break
        except ValueError :
            print("Value inputted is invalid")
    while True :
        try :
            if name.lower() == "exit":
                break
            else :
                while True :
                    try :
                        # ask for year
                        year = int(input(f"Enter the year of the new appointment\n"
                                     f"(Enter only the year using numbers)\n"
                                     f"(Max appointment date is 1 year into the future\n"
                                     f"> "))
                        # check for validity of year inputted
                        if 2023 < year < 2026:
                            break
                        elif year > 2025 :
                            print("\nYear inputted is too far\n")
                        elif year < 2023 :
                            print("\nYear inputted is in the past\n")
                        else :
                            print("\nValue inputted is invalid\n")
                    except ValueError:
                        print("\nValue inputted is invalid")
                while True :
                    try :
                        # ask for month
                        month = int(input(f"\nEnter the month of the new appointment\n"
                                      f"(Enter only the month using numbers)\n"
                                      f"> "))
                        # check for validity of month inputted
                        if 13 > month > 0:
                            break
                        else:
                            print("\nValue inputted is invalid\n")
                    except ValueError :
                        print("\nValue inputted is invalid")
                while True :
                    month_list_31 = [1,3,5,7,8,10,12]
                    month_list_30 = [4,6,9,11]
                    february = [2]
                    leap = ""
                    try :
                        # ask for date
                        date = int(input(f"\nEnter the date of the new appointment\n"
                                     f"(Enter only the date using numbers)\n"
                                     f"> ").strip())
                        # check for validity of date inputted by using list of months with 31 days 30 days or february
                        if month in month_list_31 :
                            if 0 < date < 32 :
                                break
                            else :
                                print("\nValue inputted is invalid\n")
                        elif month in month_list_30 :
                            if 0 < date < 31 :
                                break
                            else :
                                print("\nValue inputted is invalid\n")
                        # if month inputted is february check year to check for leap years
                        elif month in february :
                            if year % 4 == 0 :
                                if year % 100 == 0 :
                                    if year % 400 :
                                        leap = "true"
                                else :
                                    leap = "true"
                            if leap == "true" :
                                if 0 < date < 30:
                                    break
                                else:
                                    print("\nValue inputted is invalid\n")
                            else :
                                if 0 < date < 29:
                                    break
                                else:
                                    print("\nValue inputted is invalid\n")
                        else:
                            print("\nValue inputted is invalid\n")
                    except ValueError :
                        print("\nValue inputted is invalid")
                while True :
                    try :
                        # ask for time
                        hour = input(f"\nEnter the time of the new appointment\n"
                                     f"(Enter only the time using numbers) (HHMM)\n"
                                     f"(Between 09:00 and 15:00)\n"
                                     f"> ")
                        # check if input is formatted properly
                        int_hour = int(hour)
                        am_pm = ""
                        # check for validity of hour
                        if int(hour[2:]) >= 60 :
                            print("\nValue inputted is invalid\n")
                            print (int(hour[3:4]))
                        else :
                            if 900 <= int_hour <= 1500 :
                                # check if hour inputted is in pm or am
                                if int_hour >= 1200 :
                                    am_pm = "PM"
                                    # format military time inputted into civilian time
                                    if int_hour >= 1300 :
                                        int_hour -= 1200
                                elif 900 <= int_hour  <= 1200 :
                                    am_pm = "AM"
                                break
                            else :
                                print("\nValue inputted is invalid\n")
                    except ValueError :
                        print("\nValue inputted is invalid")
                hour_list = []
                for number in str(int_hour) :
                    hour_list.append(number)
                # format 0 into front of time
                if int_hour < 1000:
                    hour_list.insert(0, "0")
                hour_list.insert(2,":")
                print(int_hour)
                hour = "".join(hour_list)
                yes_or_no = input(f"\n{year}-{month}-{date} | {hour} {am_pm}\n\n"
                            f"Is this the right date?\n"
                            f"(yes/no)\n"
                            f"> ").lower()
                # change old data into new data in floating list
                if yes_or_no == "yes" :
                    new_date = f"{year}-{month}-{date} | {hour} {am_pm}"
                    temp_list_1[index + 4] = new_date
                    new_date1 = f"{year}-{month}-{date}"
                    new_time = f"{hour} {am_pm}"
                    temp_list_6[index1 + 2] = new_date1
                    temp_list_6[index1 + 3] = new_time
                    write_into_file("Doctor'sData.txt",temp_list_1)
                    write_into_file("appointments.txt",temp_list_6)
                    show_specific_patient_list ("Doctor'sData.txt.",index,(0,1,4))
                    break
                elif yes_or_no == "no" :
                    pass
                print()
        except ValueError :
            print("Value inputted is invalid")

def show_history (number_of_columns1 = number_of_columns) :
    while True:
        try:
            # ask for patient id
            name = input(f"\nPlease enter code or name of the patient whose history you would like to view\n"
                         f"Please enter 'exit' to exit this action\n"
                         f"> ")
            if name.lower() == "exit" :
                print()
                break
            # find index and format index into patient list index
            index = temp_list_1.index(name)
            if (index - 1) % number_of_columns1 == 0:
                index -= 1
            index = (index//7)*4
            # call function with different file
            show_specific_patient_list("History.txt",index,(0,1,2,3),4)
            print()
        except ValueError :
            print("Value inputted is invalid")

def status_set (number_of_columns1 = number_of_columns) :
    while True:
        try:
            view_patient_list((0, 1, 2, 3, 5))
            name = input(f"\nPlease enter code or name of the patient whose status you would like to update\n"
                         f"Please enter 'exit' to exit this action\n"
                         f"> ")
            if name.lower() == "exit" :
                print()
                break
            else :
                try :
                    index = temp_list_1.index(name)
                    if (index - 1) % number_of_columns1 == 0:
                        index -= 1
                    show_specific_patient_list("Doctor'sData.txt", index, (0, 1, 2, 3, 5))
                    break
                except ValueError :
                    print("Value inputted is invalid")
            break
        except ValueError :
            print("Value inputted is invalid")
    while True:
        index = temp_list_1.index(name)
        if (index - 1) % number_of_columns1 == 0:
            index -= 1
        try:
            if name.lower() == "exit":
                break
            else :
                # show choices for new data
                status_input = input(f"\n{"Issue Discharge Approval":{"."}<80}(1)\n"
                                     f"{"Recommend further hospital stay":{"."}<80}(2)\n"
                                     f"{"Receive a second opinion":{"."}<80}(3)\n"
                                     f"{"Empty data":{"."}<80}(4)\n"
                                     f"Please enter 'exit' to exit this action\n"
                                     f"> ")
                if status_input == "exit" :
                    print()
                    break
                else :
                    # change data into new data
                    if status_input == "1" :
                        temp_list_1[index + 5] = "Discharge Approved"
                    elif status_input == "2" :
                        temp_list_1[index + 5] = "Further hospital stay recommended"
                    elif status_input == "3" :
                        temp_list_1[index + 5] = "Receive a second opinion"
                    elif status_input == "4" :
                        temp_list_1[index + 5] = ""
                    else :
                        print("Value inputted is invalid")
                    write_into_file("Doctor'sData.txt",temp_list_1)
                    show_specific_patient_list("Doctor'sData.txt", index, (0, 1, 2, 3, 5))
                break
        except ValueError:
            print("Value inputted is invalid")

if __name__ == "__main__" :
    DoctorMenu()