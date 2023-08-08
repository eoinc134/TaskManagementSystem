import datetime
from enum import Enum

date_format = '%Y-%m-%d'

class TaskStatus(Enum):
    TO_DO = 'To Do'
    IN_PROGRESS = 'In Progress'
    COMPLETE = 'Completed'


class Task:
    def __init__(self, name: str, description: str, date, status: TaskStatus):
        self.name = name
        self.description = description
        self.date = self.validate_date(date)
        self.status = status

    def setName(self, name: str):
        self.name = name

    def getName(self):
        return self.name
    
    def setDescription(self, description: str):
        self.description = description
    
    def getDescription(self):
        return self.description
    
    def setDate(self, date):
        self.validate_date(date)
        self.date = date
    
    def getDate(self):
        return self.date
    
    def setStatus(self, status: TaskStatus):
        self.status = status
    
    def getStatus(self):
        return self.status
    
    def validate_date(self, date_str):
        try:
            date_obj = datetime.datetime.strptime(date_str, date_format)
            return date_obj.date()
        except ValueError:
            raise ValueError("Invalid date format. Date should be in 'YYYY-MM-DD' format.")
    
    def printTask(self):
        print(f"Task: {self.name}")
        print(f"Description: {self.description}")
        print(f"Date: {self.date}")
        print(f"Status: {self.status.value}\n")

