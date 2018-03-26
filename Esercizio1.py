list = []
while True:
    print ("Insert the number corresponding to the action you want to perform:\n"
           "1. insert a new task;\n "
           "2. remove a task;\n"
           "3. show all the tasks;\n "
           "4. close the program.\n")
    choise = int(input("Your choise: "))
    if choise==1:
        task = input("New task: ")
        list.append(task)
    elif choise==2:
        task = input("Task to be removed: ")
        list.remove(task)
    elif choise==3:
        print (sorted(list))
    elif choise==4:
        break

exit (1)