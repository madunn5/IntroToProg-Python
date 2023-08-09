# ------------------------------------------------------------------------ #
# Title: Assignment 05 - Creating a To Do List
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# MDunn,8.7.2023,Updated code in order to finish Assignment 05
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
FileName = 'ToDoList.txt'  # Text file name
objFile = ''  # An object that represents a file
RemoveTask = ''  # Variable that will represent a task the user wants to remove
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = """ 
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """  # A menu of user options. Placing at top of code so I can easily update w/o having to change my processing code
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# the try function will try to open the file if it exists. If it doesn't exist it will inform the user
# that it currently doesn't exist
try:
    objFile = open(FileName, 'r')
    for row in objFile:
        lstRow = row.split(',')  # Returns a list!
        dicRow = {'task': lstRow[0], 'priority': lstRow[1].strip()}
        lstTable += [dicRow]
    objFile.close()
except:
    print('There are currently no items on your To Do List. Please add some tasks!')

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print(strMenu)
    strChoice = str(input('Which option would you like to perform? [1 to 5] - '))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        print('Your To Do List is as follows:')
        for row in lstTable:
            print('Task:', row['task'].strip(), '| Priority:', row['priority'].strip())
        continue

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        task = input('Please enter a task: ')
        priority = input('Please choose from Low, Medium or High Priority: ')
        lstTable.append({'task': task, 'priority': priority})
        print(task, 'has been added to the list, but not saved yet!')
        continue

    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        RemoveTask = input('What task would you like to remove?: ')
        found = False
        for task in lstTable:
            if task['task'].lower() == RemoveTask.lower():
                lstTable.remove(task)
                print(RemoveTask, 'has been removed from list, but has not been saved yet!')
                found = True
                break
        # if the task is not found in the lstTable then it will remain false, and the code will print a single statement
        # instead of multiple statements based on the len(lstTable)
        if found:
            pass
        else:
            print('Task not found in the To Do List.')
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        objFile = open('ToDoList.txt', 'w')
        for row in lstTable:
            objFile.write(row['task'] + ',' + row['priority'] + '\n')
        print('Data Saved!')
        continue

    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        objFile.close()
        print('File is now closed. Goodbye!')
        break  # and Exit the program
