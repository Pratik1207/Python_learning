class ToDoList:
    def __init__(self):
        self.emptyList = []
        self.loadTask()

    def addTask(self):
        t = input("Enter task: ")
        self.emptyList.append(t)
        self.saveTask()

    def saveTask(self):
        with open("Text.txt", "w") as file:
            for x in self.emptyList:
                file.write(x + "\n")

    def loadTask(self):
        try:

            with open("Text.txt", "r") as file:
                task = file.read().splitlines()
                self.emptyList = task
        except FileNotFoundError:
            self.emptyList = []


    def deleteTask(self):
            if not self.emptyList:
                print("No Task available to delete.")
                return
            try:
                remove = int(input("which task number do you want to delete?: "))

                if remove >= 1 and remove <= len(self.emptyList):
                        self.emptyList.pop(remove-1)
                        self.saveTask()
                        print("Task deleted successfully.")
                else:
                    print("Invalid Task Number.")

            except ValueError:
                print("Enter a valid Number.")


    def viewTask(self):
        if self.emptyList:
            print("Your Current Task are as follows: ")
            for index , item in enumerate(self.emptyList, start=1):
                print(index , item)
        else:
            print("No Task Found")

    def markCompleted(self):
        if not self.emptyList:
            print("No Task Available.")
            return
        try:
            completedTask = int(input("Which Task number is completed: "))

            if 1 <= completedTask <= len(self.emptyList):
                if not self.emptyList[completedTask-1].startswith("[completed]"):
                    self.emptyList[completedTask - 1] = "[completed] " + self.emptyList[completedTask-1]
                    self.saveTask()
                    print("Task marked as completed.")
                else:
                    print("This task is already completed.")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Enter a valid number.")

print("To Do List Application")

t1 = ToDoList()

while True:
    try:
        choice = int(input("\nWhich operation you want to perform?\n1. Add Task\n2. View Task\n3. Mark As Completed\n4.Delete Task\n5. Exit\n"))
        
        match choice:
            case 1:
                t1.addTask()
                print("Task Added ")
    
            case 2:
                t1.viewTask()
    
            case 3:
                if t1.emptyList:
                    t1.viewTask()
                    t1.markCompleted() 
                else:
                    print("No Task Available.")
            case 4:
                if t1.emptyList:
                    t1.viewTask()
                    t1.deleteTask() 
                else:
                    print("No Task available to delete.")

            case 5:
                print("exit")
                break
            case _:
                print("Invalid Operation: Enter the Correct Number.")
    except ValueError:
        print("Enter a valid Number.")