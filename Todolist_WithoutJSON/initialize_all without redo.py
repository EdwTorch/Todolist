#Name : EdwTorch
#Project : To Do List
#Description : This Project is used to set up and display
# Todolist App, this app can see the list, add, remove, and update 
import time
listtodo = []
listtododate = []
def selector():
    print(f"You have {len(listtodo)} to do list")
    print('''What do you want to do
          1. Add_List
          2. Remove_List
          3. See_List
          4. Update_List
          5. Close App
          ''')
    selecting = int(input("Please Choose number of action you want to choose : "))
    if selecting == 1:
        add_list()
    elif selecting == 2:
        remove_list()
    elif selecting ==3:
        seelist()
        selector()
    elif selecting ==4:
        update_list()
    elif selecting ==5:
        exit
    else:
        print("Wrong input please try again")
        selector()
def add_list():
    print("Please Write your task below")
    listadd = input()
    listtodo.append(listadd)
    print("Please Write the date and time of your task")
    datelistadd = input()
    listtododate.append(datelistadd)
    indexx = len(listtodo)
    print(f"Your {len(listtodo)} Task is {listtodo[indexx-1]} at {listtododate[indexx-1]}")
    print()
    time.sleep(2)
    selector()
    
def remove_list():
    print("These are the list of your task")
    seelist()
    print("Which one do you want to delete ?")
    removes = int(input("Please write the number of the task : "))
    print()
    if type(removes) == int and removes <= len(listtodo):
        listtodo.pop(removes-1)
        listtododate.pop(removes-1)
        seelist()
        selector()
    else:
        print("Wrong input please try again")
        remove_list()
    
def update_list():
    print("These are the list of your task")
    seelist()
    print("Which one do you want to update ?")
    updates = int(input("Please input the number of task : "))
    updatetask = input("Input the new task : ")
    updatetaskdate = input("Input the new task date : ")
    listtodo[updates-1] = updatetask
    listtododate[updates-1]= updatetaskdate
    seelist()
    selector()
       
def seelist():
    counter = 1
    for contain in listtodo:
        print(f"Task {counter}. {contain} at {listtododate[counter-1]}")
        counter += 1
    time.sleep(10)
    print()

print(f"Hello, Welcome to To Do List Task")
selector()
