from Dashboard import Dashboard
from ToDoList import ToDoList
from Task import Task, TaskStatus

## Create Dashboard #
userDashboard = Dashboard()

## Create List ##
userDashboard.createList('Gym Routine')

## Create Tasks ##
task1 = Task("Chest", "Bench, Incline", "06/08/23", TaskStatus.COMPLETE)
task2 = Task("Back", "Rows, Lat Pulldown", "07/08/23", TaskStatus.IN_PROGRESS)
task3 = Task("Legs", "Squat, Lunges", "08/08/23", TaskStatus.TO_DO)

## Get Lists ##
lists = userDashboard.returnLists()
list1 = lists[0]

## Add Tasks ##
list1.addTask(task1)
list1.addTask(task2)
list1.addTask(task3)


## Print List ##
userDashboard.printLists()

## Remove List ##
userDashboard.removeList(list1)

userDashboard.printLists()