import mysql.connector as sql
db=sql.connect(host="localhost",user="root",password="Eitri#123")
cursor=db.cursor()
def createList(L):
    output=[]
    for i in range(len(L)):
        output.append(L[i][0])
    return output
        
cursor.execute("USE DB;")
ans="y"
cursor.execute("SELECT ROLL_NO FROM STUDENT;")
rollnums=createList(cursor.fetchall())
cursor.execute("SELECT MOB_NO FROM STUDENT;")
mobnums=createList(cursor.fetchall())
cursor.execute("SELECT NAME FROM STUDENT;")
names=createList(cursor.fetchall())
print('''Choices:
1.Enter values in the table
2.Remove values from the table
3.Change values in the table
4.Display
5.Exit''')
choice = 1
while choice!=5:
    choice=int(input("Enter the operation you want to do:"))
    #add values to database
    if choice==1:
        while ans=="y" or ans=="Y":
            rno=int(input("Enter the 10 digit Roll number:"))
            name=input("Enter the name:")
            mobno=int(input("Enter the mobile number:"))
            cursor.execute(f'''INSERT INTO Student VALUES("{rno}","{name}","{mobno}");''')
            rollnums.append(str(rno))
            names.append(name)
            mobnums.append(str(mobno))
            db.commit()
            ans=input("Do you want to enter more values y/n:")
    #removing values
    elif choice==2:
        removal=input("Enter the Roll number of the student you want to delete the data of:")
        if removal in rollnums:
            cursor.execute(f'''DELETE FROM STUDENT WHERE ROLL_NO="{removal}"''')
            index=rollnums.index(str(removal))
            rollnums.pop(index)
            names.pop(index)
            mobnums.pop(index)
            db.commit()
        else:
            print("Roll number not in database")
    elif choice==3:
        update_rno=input("Enter the roll number of the student you want to update the information of:")
        if update_rno in rollnums:
            print('''1.Roll number\n2.Name\n3.Mobile number''')
            change=int(input("Enter the number of the value you want to change:"))
            if change==1:
                update=input("Enter the updated Roll number:")
                cursor.execute(f'''UPDATE STUDENT
                SET ROLL_NO="{update}" WHERE ROLL_NO="{update_rno}";''')
                rollnums.append(update)
                rollnums.remove(update_rno)
                db.commit()
            elif change==2:
                update=input("Enter the updated name:")
                cursor.execute(f'''UPDATE STUDENT
                SET NAME="{update}" WHERE ROLL_NO="{update_rno}";''')
                names.append(update)
                names.remove(names[rollnums.index(update_rno)])
                db.commit()
            elif change==3:
                update=input("Enter the updated mobile number:")
                cursor.execute('''UPDATE STUDENT
                SET MOB_NO="{update}" WHERE ROLL_NO="{update_rno}"''')
                mobnums.append(update)
                mobnums.append(mobnums[rollnums.index(update_rno)])
            else:
                print("Invalid Operation")
        else:
            print("Roll number not in database")
    elif choice==4:
        cursor.execute("SELECT * FROM STUDENT;")
        print(cursor.fetchall())


