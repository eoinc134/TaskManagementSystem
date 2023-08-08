from sql.Sql import Sql

database = Sql()
cursor = database.cnxn.cursor()

cursor.execute("SELECT TOP (1000) [UserID],[Email],[Password] FROM [TaskManagementSystem].[dbo].[Users]")

for row in cursor:
    
    print('row = %r' % (row,))