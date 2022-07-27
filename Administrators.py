from students import *
from instructors import Instructor
from Maintaining import *


class Administrators(object): #admin main class

    @staticmethod
    def addInstructor(): #admin handle method
        Name=input("Enter the instructor name: ")
        Sex = input("Type your gender : ")
        Type = input("Enter dance style : ")
        TpNo = input("Enter your contact number : ")
        HoursRATE = input("Enter per hour rate: ")
        availability=list()
        print("Enter days available : (press 1 to end)")
        while(True):
            day=input(" input day : ")
            if(day=='1'):
                break
            availability.append(day)#check days availability
        addInstructorToDB(Instructor(Name,Sex,Type,TpNo,HoursRATE,availability))


    @staticmethod
    def editInstructor():#admin handle method
        Name= input("Do you want to edit? Input instructor name here: ")
        Sex = input("Retype gender  ")
        Type = input("Retype dance style : ")
        TpNo= input("Retype contact number : ")
        HoursRATE = input("ReEnter per hour rate : ")
        availability = list()
        # assume here you are unable to edit available dates
        changeInstructorInDB(Instructor(Name,Sex,Type,TpNo,HoursRATE, availability))

    @staticmethod
    def deleteInstructor():#admin handle method
        nme=input("do you want delete ? input name of instructor:")
        deleteInstructorsInDB(nme)


    @staticmethod
    def viewInstructor():#admin handle method
        viewAllInstructors();

    @staticmethod
    def scheduleInstructor():#admin handle method
        nme=input("Enter instructor name : ")
        setInstructorToStudents(nme)

    @staticmethod
    def registerStudent():#admin handle method
        StudentID= input("Enter your Student_id: ")
        FirstNAME = input("Enter your first name : ")
        LastNAME = input("Enter your Last name : ")
        Email = input("Enter your email : ")
        Sex = input("Enter your gender : ")
        DOB = input("Enter your birthday : ")
        TpNo = input("Enter your contact num : ")
        Address = input("Enter your address : ")
        TypeOfDance = input("Enter your  dance style : ")
        MaxHoursRate = input("Enter your Maximum hour rate  : ")
        addStudentToDB(Students(StudentID,FirstNAME,LastNAME ,Email,Sex, DOB,TpNo,Address ,TypeOfDance,MaxHoursRate))#add

