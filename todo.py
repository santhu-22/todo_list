todo_list=[ "eat","sleep","walk","going"]
def  show_tasks():
    if not todo_list:
        print("no task")
    else:
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def add_tasks(task):
    todo_list.append(task)
    print("task added")

def delete_tasks(index):
    if 0<index<=len(todo_list):
        removed=todo_list.pop(index-1)
        print(f"deleted:{removed}")
    else:
        print("invalid task number")
while True:
    print("\n----todo_list---")
    print("1. show lists")
    print("2. add tasks")
    print("3. remove tasks")
    print("4. exit")

    choice=input("choose an option(1-4)")

    if choice=='1':
        show_tasks()
    elif choice=='2':
        task=input("enter task")
        add_tasks()
    elif choice=='3':
        show_tasks()
        try:
            idx=int(input("enter a number deleted"))
            delete_tasks(idx) 
        except ValueError:
                print("please enter a valid number")

    elif choice=='4':
        print("goodbye !")
        break
    else:
        print("invalid option")

