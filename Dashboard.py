from ToDoList import ToDoList

class Dashboard:
    def __init__(self):
        self._lists = []

    def createList(self, title: str):
        to_do_list = ToDoList(title)
        self._lists.append(to_do_list)

    def returnLists(self):
        return self._lists

    def removeList(self, list):
        self._lists.remove(list)

    def printLists(self):
        print("DASHBOARD:")
        for to_do_list in self._lists:
            to_do_list.printList()