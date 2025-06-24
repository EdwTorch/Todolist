#Name : EdwTorch
#Project : To Do List
#Description : This Project is used to set up and display
# Todolist App, this app can see the list, add, remove, and update 
import time
listtodo = {}
temporarylisttodo = {}
counter = 1
def redo(numbers):
    decision = int(input("Do you want to do it again? (Write 1 for Yes, 0 for No) : "))
    if decision ==1:
        print()
        if numbers ==1:
            add_list()
            redo(1)
        elif numbers ==2:
            remove_list()
            redo(2)
        elif numbers ==3:
            seelist()
            redo(3)
        elif numbers ==4:
            update_list()
            redo(4)
    elif decision ==0:
        print()
        selector()
    else:
        print("Wrong input please try again")
        print()
        selector()
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
        
        redo(1)
    elif selecting == 2:
        remove_list()
        redo(2)
    elif selecting ==3:
        seelist()
        redo(3)
    elif selecting ==4:
        update_list()
        redo(4)
    elif selecting ==5:
        exit
    else:
        print("Wrong input please try again")
        selector()
def rearrange_listforremoval(update):
    x = update
    global counter
    while x<counter:
        listtodo[x] = listtodo[x+1]
        x+=1
        
    del listtodo[counter]
        

def add_list():
    global counter
    print("Please Write your task below")
    listadd = input()
    listtodo[counter] = {}
    listtodo[counter]["Task"] = listadd
    print("Please Write the date and time of your task")
    datelistadd = input()
    listtodo[counter]["Date"]= datelistadd
    print(f"Your {counter} Task is {listtodo[counter]["Task"]} at {listtodo[counter]["Date"]}")
    counter +=1
    print()
    time.sleep(2)

def remove_list():
    global counter
    print("These are the list of your task")
    seelist()
    print("Which one do you want to delete ?")
    removes = int(input("Please write the number of the task : "))
    print()
    if type(removes) == int and removes <= len(listtodo):
        counter -=1
         #Delnya pindahin ke def rearrangelist
        rearrange_listforremoval(removes)
        seelist()
    time.sleep(3)
    
def update_list():
    print("These are the list of your task")
    seelist()
    print("Which one do you want to update ?")
    updates = int(input("Please input the number of task : "))
    updatetask = input("Input the new task : ")
    updatetaskdate = input("Input the new task date : ")
    listtodo[updates]["Task"] = updatetask
    listtodo[updates]["Date"] = updatetaskdate
    seelist()
    time.sleep(3)
       
def seelist():
    seelistcounter = 1
    for isian in range (len(listtodo)):
        print(f"Task {seelistcounter} {listtodo[seelistcounter]["Task"]} at {listtodo[seelistcounter]["Date"]}")
        seelistcounter += 1
    time.sleep(3)
    print()

print(f"Hello, Welcome to To Do List Task")
selector()
