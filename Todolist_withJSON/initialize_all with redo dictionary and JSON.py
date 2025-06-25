#Name : EdwTorch
#Project : To Do List
#Description : This Project is used to set up and display
# Todolist App, this app can see the list, add, remove, and update 
import time
import json
listtodo = {}
counter = 1
name = 0
def open_json():
    global listtodo
    decision = int(input("Do You Want to Open Another Todolist File? (Write 1 for Yes, 0 for No) : "))
    if decision == 1:
        print()
        inputjson = input("Please write your file json name that you want to access in this folder (ex: June.json (Just write June)): ")
        try: 
            with open(f"{inputjson}.json",'r') as fileinput:
                listtodo = json.load(fileinput)
                global name 
                name = inputjson
                selector()
        except FileNotFoundError:
            print(f"the {inputjson}.json doesn't exist ")
            open_json()
    elif decision ==0:
        selector()
    else:
        print("Wrong input please try again")
        open_json()
        
def redo(numbers):
    global listtodo
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
    global listtodo
    print(f"You have {len(listtodo)} to do list")
    print('''What do you want to do
          1. Add_List
          2. Remove_List
          3. See_List
          4. Update_List Name and Date
          5. Update Task Status 
          6. Upload_List to JSON
          7. Close App
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
        status_update()
    elif selecting ==6:
        upload_list()
    elif selecting ==7:
        exit
    else:
        print("Wrong input please try again")
        selector()
def rearrange_listforremoval(update):
    global listtodo
    x = update
    global counter
    while x<counter:
        listtodo[x] = listtodo[x+1]
        x+=1
        
    del listtodo[counter]
        
def upload_list():
    global name
    global listtodo
    if type(name) == str:
        with open (f"{name}.json","w") as filesave:
            json.dump(listtodo,filesave,indent=4)
    else: 
        name = input("Please write your file json name that you want to upload in this folder (ex: June.json (Just write June)): ")
        with open (f"{name}.json","w") as filesave:
            json.dump(listtodo,filesave,indent=4)
def add_list():
    global counter
    global listtodo
    print("Please Write your task below")
    listadd = input()
    listtodo[counter] = {}
    listtodo[counter]["Task"] = listadd
    print("Please Write the date and time of your task")
    datelistadd = input()
    listtodo[counter]["Date"]= datelistadd
    listtodo[counter]["Status"] = "Not Done"
    print(f"Your {counter} Task is {listtodo[counter]["Task"]} at {listtodo[counter]["Date"]} with Status {listtodo[counter]["Status"]}")
    counter +=1
    print()
    time.sleep(2)

def remove_list():
    global counter
    global listtodo
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
    global listtodo
    print("These are the list of your task")
    seelist()
    print("Which task do you want to update (Name of Task and Time) ?")
    updates = int(input("Please input the number of task : "))
    updatetask = input("Input the new task : ")
    updatetaskdate = input("Input the new task date : ")
    listtodo[updates]["Task"] = updatetask
    listtodo[updates]["Date"] = updatetaskdate
    seelist()
    time.sleep(3)
       
def seelist():
    global listtodo
    seelistcounter = 1
    for isian in range (len(listtodo)):
        print(f"Task {seelistcounter} {listtodo[str(seelistcounter)]["Task"]} at {listtodo[str(seelistcounter)]["Date"]} with Status {listtodo[str(seelistcounter)]["Status"]}")
        seelistcounter += 1
    time.sleep(3)
    print()

def status_update():
    global listtodo
    print("These are the list of your task")
    seelist()
    print("Which task status do you want to update ?")
    updates = int(input("Please input the number of task : "))
    updatetaskstatus = int(input("Input 1 for Done and 0 for Not Done : "))
    if updatetaskstatus ==1:
        updatetaskstatus = "Done"
    elif updatetaskstatus ==0:
        updatetaskstatus = "Not Done"
    else:
        print("Wrong Input please try again")
        status_update()
    listtodo[str(updates)]["Status"] = updatetaskstatus
    seelist()
    time.sleep(3)
print(f"Hello, Welcome to To Do List Task")
open_json()