import sqlite3
conn=sqlite3.connect("Students.sqlite3")
cursor=conn.cursor()
class Student:
    def __init__(self,name,address,rollno,subject):
        self.name=name
        self.address=address
        self.rollno=rollno
        self.subject=subject
    def createTable(self):
        conn.execute('''create table if not exists students
        (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        Name char(150) NOT NULL,
        Address char(150) NOT NULL,
        Rollno INT NOT NULL,
        Subject char(150) NOT NULL 
        );''')

    def insertData(self):
        self.createTable()
        queryString="insert into students (name,address,rollno,subject) values (?,?,?,?);"
        cursor.execute(queryString,(self.name,self.address,self.rollno,self.subject))
        conn.commit()
        print("Data Inserted Successfully !! ")

Std1=Student("Abcd","KTM",15,"Python")
# Std1.createTable()  
# Std1.insertData()  
Std2=Student("Pravhat","Chakarpath",19,"Time pass ")
Std2.insertData()