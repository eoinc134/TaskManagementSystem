class ToDoList:
    def __init__(self, title: str):
        self.title = title
        self._tasks = []

    def setTitle(self, title: str):
        self.title = title

    def getTitle(self):
        return self.title
    
    def addTask(self, task):
        self._tasks.append(task)

    def removeTask(self, task):
        self._tasks.remove(task)

    def printList(self):
        print(f"Title: {self.title}\n")
        for task in self._tasks:
            task.printTask()
    
