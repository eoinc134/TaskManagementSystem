import pypyodbc as odbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'TEMPADM-OLQGVVR'
DATABASE_NAME = 'TaskManagementSystem'

class Sql:
    def __init__(self):
        self.cnxn = odbc.connect(f"""
            DRIVER={{{DRIVER_NAME}}};
            SERVER={SERVER_NAME};
            DATABASE={DATABASE_NAME};
            Trust_Connection=yes;
        """)

    def retrieve_all_emails():
        pass

    def get_user_password():
        pass