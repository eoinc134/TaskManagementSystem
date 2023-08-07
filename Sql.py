import pypyodbc as odbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'TEMPADM-OLQGVVR'
DATABASE_NAME = 'TaskManagementSystem'

class Sql:
    def __init__(self):
        self.cnxn = odbc.conect(f"""
            DRIVER={{{DRIVER_NAME}}};
            SERVER={SERVER_NAME};
            DATABASE={DATABASE_NAME};
            Trust_Connection=yes;
        """)