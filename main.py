
def loadtasks():
    global tasks, ctasks
    with open("Tasks/tasks.txt") as f:
        tasks = f.read()
    with open("Tasks/completedtasks.txt") as f:
        ctasks = f.read()

def mainmenu():
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    print("■■■■■■■-Main Menu-■■■■■■■■■")
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    print("1. View Tasks\n2. Complete Tasks\n3. Add Tasks\n4. Remove Tasks\n5. Exit")
    choice = int(input("Enter: "))
    if choice == 1:
        viewtasks()
    elif choice == 2:
        completetasks()
    elif choice == 3:
        addtasks()
    elif choice == 4:
        removetasks()
    elif choice == 5:
        print("Closing Simple TASKS!")
        exit()
    else:
        print("Invalid input.")
        mainmenu()

def viewtasks():
    print("■■■■-Current Tasks-■■■■")
    print(tasks)
    print("■■■■-Completed Tasks-■■■■")
    print(ctasks)
    print("■■■■■■■■■■■■■■■■■■■■■■■■■")
    print("1. Main Menu\n2. Exit")
    print("■■■■■■■■■■■■■■■■■■■■■■■■■")
    choice = int(input("Enter: "))
    if choice == 1:
        mainmenu()
    elif choice == 2:
        print("Closing Simple TASKS!")
        exit()
    else:
        print("Invalid input.")
        mainmenu()
    
def completetasks():
    print("■■■■■■■■■■■■■■■■■■■■■■■■■")
    print(tasks)
    print("■■■■■■■■■■■■■■■■■■■■■■■■■")
    ans = input("Enter the task you completed: ")
    if ans in tasks.splitlines():
        with open("Tasks/tasks.txt") as f:
            lines = f.readlines()
        with open("Tasks/tasks.txt", "w") as f:
            for line in lines:
                if line.strip() != ans:
                    f.write(line)
        with open("Tasks/completedtasks.txt", "a") as f:
            f.write('\n' + ans)
        loadtasks()
        print("■■■■■■■■■■■■■■■■■■■■■■■■■")
        print(f"{ans} has been successfully marked as completed!")
        print("■■■■■■■■■■■■■■■■■■■■■■■■■")
        print("1. Main menu\n2. Complete another task\n3. Exit")
        print("■■■■■■■■■■■■■■■■■■■■■■■■■")
        choice = int(input("Enter: "))
        if choice == 1:
            mainmenu()
        elif choice == 2:
            completetasks()
        elif choice == 3:
            print("Closing Simple TASKS!")
            exit()
        else:
            print("Invalid input.")
            mainmenu()
    else:
        print("Please enter a task present in the above list.")
        completetasks()

def addtasks():
    print("■■■■■■■■■■■■■■■■■■■■■■■■■")
    newtask = input("Enter new task: ")
    with open("Tasks/tasks.txt", "a") as f:
        f.write(newtask + '\n')
    loadtasks()
    print(f"{newtask} has been successfully added to your Tasks.")
    print("■■■■■■■■■■■■■■■■■■■■■■■■■")
    print("1. Main menu\n2. Add another task\n3. Exit")
    print("■■■■■■■■■■■■■■■■■■■■■■■■■")
    choice = int(input("Enter: "))
    if choice == 1:
        mainmenu() 
    elif choice == 2:
        addtasks()
    elif choice == 3:
        print("Closing Simple TASKS!")
        exit()
    else:
        print("Invalid input.")
        mainmenu()
    
def removetasks():
    print("■■■■■■■■■■■■■■■■■■■■■■■■■")
    print(tasks)
    print("■■■■■■■■■■■■■■■■■■■■■■■■■")
    ans = input("Enter a task you want to remove: ")
    if ans in tasks.splitlines():
        with open("Tasks/tasks.txt") as f:
            lines = f.readlines()
        with open("Tasks/tasks.txt", "w") as f:
            for line in lines:
                if line.strip() != ans:
                    f.write(line)
        loadtasks()
        print("■■■■■■■■■■■■■■■■■■■■■■■■■")
        print(f"{ans} has been successfully removed from your Tasks!")
        print("■■■■■■■■■■■■■■■■■■■■■■■■■")
        print("1. Main menu\n2. Remove another task\n3. Exit")
        print("■■■■■■■■■■■■■■■■■■■■■■■■■")
        choice = int(input("Enter: "))
        if choice == 1:
            mainmenu() 
        elif choice == 2:
            removetasks()
        elif choice == 3:
            print("Closing Simple TASKS!")
            exit()
        else:
            print("Invalid input.")
            mainmenu()
    else:
        print("Please enter a task present in your Tasks.")
        mainmenu()

print("■-- Welcome to Simple TASKS! --■")
loadtasks()
mainmenu()
