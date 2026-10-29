# ====== TO-DO LIST ======
# 1. Add Task
# 2. View Tasks
# 3. Mark Task as Completed
# 4. Delete Task
# 5. Exit
# ========================
# Enter your choice:

class ToDoList:
    def __init__(self):
        pass

    def loadtask(self):
        with open("text.txt") as f:
            for x in f:
                print(x)

    def saveTask(self, item_list):
            with open("text.txt", "a") as f:
                for x in item_List:
                    f.write(x + "\n")

    def addTask(self,item_List):
        while True:
            task = input("Enter the Task: ")
            item_List.append(task)
            break

    def markAsCompleted(self,done):
        with open('text.txt', "r") as f:
            lines = f.readlines()

        with open('text.txt', "w") as f:
            for i, line in enumerate(lines, start=1):
                if i == done:
                    f.write("[Task Completed]" + line)
                else:
                    f.write(line)

    def deleteTask(self,taskToBeDeleted):
        with open("text.txt", "r") as f:
            lines = f.readlines()

        with open('text.txt', "w") as f:
            for i, line in enumerate(lines, start=1):
                if i != taskToBeDeleted:
                    f.write(line)


t1 = ToDoList()

item_List = []

print("Welcome to  Command Line To Do List")

choice = int(input("What you want to do?\n1. Add Task\n2. View Tasks\n3. Mark Task as Completed\n4. Delete Task\n5. Exit\nEnter your number:"))

match choice:
    case 1:
        t1.addTask(item_List)
        t1.saveTask(item_List)
        print("Task Added")

    case 2:
        t1.loadtask()

    case 3:
        t1.loadtask()
        done = int(input("Which number of task is completed?"))
        t1.markAsCompleted(done)
        t1.loadtask()

    case 4:
        removeTask = int(input("Which task you want to delete?"))
        t1.deleteTask(removeTask)
        t1.loadtask()
    case _:
        print("Invalid Option")