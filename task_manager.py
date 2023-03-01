# Program to manage tasks assigned to each member of a team in a small business

# Importing the datetime module
from datetime import date


def get_user_dict():
    # initializing user dictionary
    user_dict_1 = {}
    # opening user.txt file and reading each line of the file
    user_file_1 = open('user.txt', 'r+')
    user_list_1 = user_file_1.readlines()

    # looping through the user list, removing the new line character and storing the username,password in the user
    # dictionary by using split
    for line_1 in user_list_1:
        line_1 = line_1.rstrip('\n')
        line_split_1 = line_1.split(',')
        user_dict_1[line_split_1[0].strip()] = line_split_1[1].strip()
    # print(user_dict)
    user_file_1.close()
    return user_dict_1


user_dict = get_user_dict()


# Error handling done to handle the scenarios of wrong username and wrong password
while True:
    # Asking the user to enter username and password using input method
    username = input("Enter your username: ")
    password = input("Enter password : ")

    # Using if condition checking whether the username entered is in the user dictionary
    # if username and password matches login successful else asks the user to enter valid credentials
    if username in user_dict.keys():
        if password == user_dict[username]:
            print("Login successful!")
            break
        else:
            print("Password Incorrect.")
    else:
        print("Username is not available.Please enter valid credentials.")

# block of code to handle separate menu options for admin and non admin users
while True:
    # using if condition to check whether the logged in username is admin or not and assign the menu options accordingly
    if username == "admin":
        # presenting the menu to the user 'admin' and
        # making sure that the user input is converted to lower case.
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
s - Statistics
e - Exit
: ''').lower()
    else:
        # presenting the menu to the non admin user and
        # making sure that the user input is converted to lower case.
        menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

# block of code to add a new user to the user.txt file
    # using if condition to check the menu option and the user 'admin'
    if menu == 'r' and username == 'admin':
        while True:

            # Asking the user to enter new user's username,password and confirm password
            # if the entered username already exists in the user.txt file, it will ask for different username
            new_username = input("Enter the new user's username: ")
            new_password = input("Enter the new user's password: ")
            confirm_password = input("Enter the new user's password again to confirm: ")
            if new_username in user_dict.keys():
                print("Username already exists.Please provide a different username")
            else:

                # using if condition to check whether the new password and confirm password are same or not
                # if they are same the new user will be created successfully
                # else displays they both are not matching
                if new_password == confirm_password:
                    update_user_file = open('user.txt','a+')
                    user_entry_line = f'\n{new_username}, {new_password}'
                    update_user_file.write(user_entry_line)
                    user_dict[new_username] = new_password
                    update_user_file.close()
                    print("New user created successfully.")
                    break
                else:
                    print("Password and Confirm Password does not match!!!")

# block of code that will allow a user to add a new task to task.txt file
    elif menu == 'a':

        # Using while True to handle error scenarios of wrong username
        # and will break the loop when the task details are captured correctly
        while True:
            user_dict = get_user_dict()

            # Asking the user to enter the username of the person to whom the task needs to be assigned
            task_assign_userName = input("Enter the Username of the person to whom the task is assign to: ")

            # if the entered username does not exists in the user.txt file
            # then asks the user to enter the username which already exists in the file
            if task_assign_userName not in user_dict.keys():
                print("Enter the username which already exists in the file.")
                continue

            # Asking the user to enter the required details to add a task
            task_title = input("Enter title of the task: ")
            task_description = input("Enter the description of the task(without commas): ")
            task_dueDate = input("Enter due date of the task (eg. 06 Mar 2023) : ")

            # to get the current date, imported date class of the date time module
            # and used the date.today() method to get the current date
            # used strftime() to create date in different format
            # googled about current date in https://www.programiz.com/python-programming/datetime/current-datetime
            today = date.today()
            task_assignDate = today.strftime("%d %b %Y")
            is_task_complete = 'No'
            update_task_file = open('tasks.txt','a+')
            task_file_line = f'\n{task_assign_userName}, {task_title}, {task_description}, {task_dueDate}, {task_assignDate}, {is_task_complete}'
            update_task_file.write(task_file_line)
            update_task_file.close()
            break

    # block of code to read all the tasks from task.txt file and print to the console in the specified format
    elif menu == 'va':
        read_task_file = open('tasks.txt','r')
        task_file_list = read_task_file.readlines()
        read_task_file.close()
        for line in task_file_list:
            line_strip = line.rstrip('\n')
            line_split = line_strip.split(', ')
            output = '-'*100 + '\n'
            output += f'Task:\t\t\t\t\t{line_split[1]}\n'
            output += f'Assigned to:\t\t\t{line_split[0]}\n'
            output += f'Date assigned:\t\t\t{line_split[3]}\n'
            output += f'Due date:\t\t\t\t{line_split[4]}\n'
            output += f'Task Complete?:\t\t\t{line_split[5]}\n'
            output += f'Task description:\t\t{line_split[2]}\n'
            output += '-'*100
            print(output)

# Block of code that will only read the task of the logged in user from tasks.txt file
    elif menu == 'vm':
        read_task_file = open('tasks.txt', 'r')
        task_file_list = read_task_file.readlines()
        read_task_file.close()
        task_count = 0
        for line in task_file_list:
            line_strip = line.rstrip('\n')
            line_split = line_strip.split(', ')

            # using if condition to check if the logged in username matches with the username in the tasks.txt file
            # using output variable to print to print the task details in specified format
            # Using task_count variable, to count the number of tasks
            # and if the task count is zero, then 'No tasks assigned for the user' will be printed to the console
            if username == line_split[0]:
                output = '-' * 100 + '\n'
                output += f'Task:\t\t\t\t\t{line_split[1]}\n'
                output += f'Assigned to:\t\t\t{line_split[0]}\n'
                output += f'Date assigned:\t\t\t{line_split[3]}\n'
                output += f'Due date:\t\t\t\t{line_split[4]}\n'
                output += f'Task Complete?:\t\t\t{line_split[5]}\n'
                output += f'Task description:\t\t{line_split[2]}\n'
                output += '-' * 100
                print(output)
                task_count += 1
        if task_count == 0:
            print('-' * 100)
            print("No tasks assigned for the logged in user")
            print('-' * 100)

# block of code to calculate the statistics and display the total number of users and tasks

    # allows the user to calculate the statistics if the username is ' admin'
    elif menu == 's' and username == 'admin':
        user_file = open('user.txt','r')
        task_file = open('tasks.txt','r')

        # open the user.txt file and tasks file
        # then count the number of lines in the task file list and number of lines in the user.txt file list
        users_count = len(user_file.readlines())
        tasks_count = len(task_file.readlines())
        user_file.close()
        task_file.close()

        # printing the users count and tasks count to the console
        result = '-' * 100 + '\n'
        result += f'Total number of users :\t\t\t\t\t{users_count}\n'
        result += f'Total number of tasks :\t\t\t\t\t{tasks_count}\n'
        result += '-' * 100
        print(result)

# if 'e' is selected exiting from the program
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

# block of code to handle if any wrong choices are entered
    else:
        print("You have made a wrong choice, Please Try again")
