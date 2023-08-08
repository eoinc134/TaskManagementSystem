from Sql import Sql

sql = Sql()
cursor = sql.cnxn.cursor()

cursor.execute("SELECT TOP (1000) [UserID],[Email],[Password] FROM [TaskManagementSystem].[dbo].[Users]")
for row in cursor:
    print('row = %r' % (row,))