import mysql.connector as sql
db=sql.connect(host="localhost",user="root",password="Eitri#123")
cursor=db.cursor()
cursor.execute("USE DB;")
#cursor.execute("CREATE TABLE Student(Roll_no varchar(255),Name varchar(255),Mob_No varchar(255));")
for i in range(2):
    rno=int(input("Enter the 10 digit Roll number:"))
    name=str(input("Enter the name:"))
    mobno=int(input("Enter the mobile number:"))
    cursor.execute(f"INSERT INTO Student VALUES({rno},{name},{mobno});")
    db.commit()
cursor.execute("SELECT * FROM Student;")
result=cursor.fetchall()
print(result)

