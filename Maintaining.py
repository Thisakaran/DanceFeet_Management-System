import sqlite3
from tkinter import *

con=sqlite3.connect("Information_DanceSystem.db")#add the database


def addInstructorToDB(instructors): #method within instructors
    query="insert into instructors values(?,?,?,?,?)"
    cursor=con.cursor()
    ls=(instructors.Name,instructors.Sex,instructors.Type,instructors.TpNo,instructors.HoursRATE)
    cursor.execute(query,ls)
    con.commit()
    for days in instructors.availability:
        query = "insert into instructors_availability values(?,?)"
        cursor = con.cursor()
        ls = (instructors.Name, days)
        cursor.execute(query, ls)
        con.commit()
    print("done")


def addStudentToDB(students):#method within Students
    query = "insert into students values(?,?,?,?,?,?,?,?,?,?,?)"
    cursor = con.cursor()
    ls = (students.StudentID,students.FirstNAME, students.LastNAME, students.Email, students.Sex, students.DOB,students.TpNo,students.Address,students.TypeOfDance,students.MaxHoursRate,"")
    cursor.execute(query, ls)
    con.commit()
    print("done")


def changeInstructorInDB(instructors):#method within instructors
    query = "update instructors set Sex=?,Type=?,tpNo=?,HoursRATE=? where Name=?"
    cursor = con.cursor()
    ls = (instructors.Sex, instructors.Type, instructors.TpNo, instructors.HoursRATE,instructors.Name)
    cursor.execute(query, ls)
    con.commit()
    print("done")

def deleteInstructorsInDB(instructors):#method within instructors
    query = "delete from instructors where Name=?"
    cursor = con.cursor()
    ls = (instructors,)
    cursor.execute(query,ls)
    con.commit()
    print("done")

def viewAllInstructors():#method within instructors
    query = "select * from instructors"
    cursor = con.cursor()

    cursor.execute(query)
    rows=cursor.fetchall()
    root=Tk()
    root.title("Instructors")
    rowCount=len(rows)
    colCount=len(rows[0])
    for i in range(rowCount):
        for j in range(colCount):
            enty=Label(root,width=20)
            enty.grid(row=i, column=j)
            enty['text'] = rows[i][j]


    print("done")

def setInstructorToStudents(nme):#gather information from students table put to the instructor table


    query1="select StudentID,Type,MaxHoursRate from students" #Sql query
    cursor = con.cursor()

    cursor.execute(query1)
    stuRows = cursor.fetchall()
    query2 = "select Type,HoursRATE from instructors where Name='"+nme+"'"
    cursor = con.cursor() #use click option

    cursor.execute(query2)
    instructors = cursor.fetchall() #find that we cannot have multiple instructors with same name
    #gather information from students for an instructor
    setStudents=list()
    if(len(instructors)==0):
        print("No such instructors in db")
    else:
        for students in stuRows:
            #check instructors Type of dance  equals to student type method and students HoursRATE = instructor HoursRATE
            if students[1]==instructors[0][0] and students[2]>=instructors[0][1]: #assume that we cannot have access multiple instructors with same name
                setStudents.append(students[0])

        for StudentID in setStudents:#for looping line by line output

            query3="update students set instructorNAME=? where StudentID=?"
            cursor = con.cursor()
            ls = (nme,StudentID)
            cursor.execute(query3, ls)#when we click the curser on add query3
            con.commit()
            print("done")




def isInsinDB(instructorNAME): #method
    query = "select * from instructors where Name='"+instructorNAME+"'"
    cursor = con.cursor()

    cursor.execute(query)
    rows = cursor.fetchall()
    if(len(rows)==0):
        return False
    return rows


def addAbooking(instructorNAME,ScheduleNO): #add booking table when we added schedule information
    query="select StudentID from Students where instructorNAME='"+instructorNAME+"'"
    cursor = con.cursor()

    cursor.execute(query)
    stuRows = cursor.fetchall()
    for stNo in stuRows:
        query1 = "insert into schedule values(?,?,?)"
        cursor = con.cursor()
        stNo = stNo[0]
        ls = (stNo, instructorNAME, ScheduleNO)
        cursor.execute(query1, ls)
        con.commit()
    print("done")


