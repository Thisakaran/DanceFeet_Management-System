from tkinter import *
from Administrators import Administrators
from instructors import *
from Maintaining import isInsinDB


def showAdministratorsFunc():#main mehtod here
    print("1 : Add an instructor by Administrator")#handle by admin to add function
    print("2 : Delete an instructor by Administrator")#handle by admin to delete function
    print("3 : Edit an instructor by Administrator")#handle by admin to edit function
    print("4 : View all instructors by Administrator")#handle by admin to show function
    print("5 : Schedule an instructor by Administrator")#handle by admin to schedule function
    print("6 : Register a student by Administrator ") #register students by admin
    choice=int(input("input your choice : "))
    #choice options
    if(choice==1):
        Administrators.addInstructor()
    elif(choice==2):
        Administrators.deleteInstructor()
    elif(choice==3):
        Administrators.editInstructor()
    elif(choice==4):
        Administrators.viewInstructor()
    elif(choice==5):
        Administrators.scheduleInstructor()
    elif (choice == 6):
        Administrators.registerStudent()
    else:
        print("Please!Check your choice")



def instructorFunc():#create method

    name=input("Enter your Name (instructor) : ")
    res=isInsinDB(name)
    if(res==False):
        print("you are not registered..")#instructor not registerd it'll show this message

    else:
        ins = Instructor(res[0][0], res[0][1], res[0][2], res[0][3], res[0][4], "")#data show in row,coloum in gui
        ins.addLessonBooking()

#main tkinter decalaration
root=Tk()
root.title("DanceSystem")
root.config(bg="#2c3e50")



root=Tk()
root.title("DanceSystem") #root title name (show gui)
root.config(bg="#2c3e50")#background color

lable1=Label(root,text="")
lable2=Label(root,text="")
title = Label(lable1, text="DanceCompany", font=("Calibri", 18, "bold"),bg="#535c68", fg="Black")#add page formation style
title.grid(row=0, columnspan=2, padx=5, pady=10, sticky="w")
title = Label(lable2, text="Select Here:", font=("Calibri", 12, "bold"), fg="Black")
title.grid(row=0, columnspan=2, padx=2, pady=5, sticky="w")

buttonAdmin=Button(root,command=showAdministratorsFunc,text="Administrator")
buttonInstructor=Button(root,command=instructorFunc,text="Instructor")

lable1.grid(row=0,column=1)
lable2.grid(row=1,column=0)
buttonInstructor.grid(row=2,column=0)
buttonAdmin.grid(row=2,column=2)

root.mainloop(); #this a must and important call function such mainloop






