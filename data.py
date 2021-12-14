import sqlite3

con = sqlite3.connect('users.db')
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users(ID Integer Primary Key,NAME text,AGE Integer,CITY text);")

def insertData(name, age, city):
    qry = "insert into users (NAME,AGE,CITY) values (?,?,?);"
    con.execute(qry, (name, age, city))
    con.commit()
    print("User Details Added")


def updateData(name, age, city, id):
    qry = "update users set NAME=?,AGE=?,CITY=? where id=?;"
    con.execute(qry, (name, age, city, id))
    con.commit()
    print("User Details Updated")


def deleteData(id):
    qry = "delete from users where id=?;"
    con.execute(qry, (id))
    con.commit()
    print("User Details Deleted")


def viewData():
    qry = "select * from users"
    result = con.execute(qry)
    r = result.fetchall()
    for row in r:
        print(row)

def selectData(id):
    qry = "select NAME,AGE,CITY from users where id=?;"
    result = con.execute(qry,(id))
    r = result.fetchall()
    print(r)



print("""
1.Insert
2.Update
3.Delete
4.View
5.select
""")

ch = 1
while ch == 1:
    c = int(input("Select Your Choice : "))
    if (c == 1):
        print("Add New Record")
        name = input("Enter Name : ")
        age = input("Enter Age : ")
        city = input("Enter City : ")
        insertData(name, age, city)
    elif (c == 2):
        print("Edit A Record")
        id = input("Enter ID : ")
        name = input("Enter Name : ")
        age = input("Enter Age : ")
        city = input("Enter City : ")
        updateData(name, age, city, id)
    elif (c == 3):
        print("Delete A Record")
        id = input("Enter ID : ")
        deleteData(id)
    elif (c == 4):
        print("Print All Record")
        viewData()
    elif (c==5):
        print("Select A Record")
        id = input("Enter id:")
        selectData(id)
    else:
        print("Invalid Selectio")
    ch = int(input("Enter 1 To Continue : "))
print("Thank You")