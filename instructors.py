from students import *
from Maintaining import *
class Instructor:
    def __init__(self,Name,Sex,Type,TpNo,HoursRATE,availability):
        #The __init__() function is called automatically every time the class is being used to create a new object.
        #The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
        self.Name=Name
        self.Sex=Sex
        self.Type=Type
        self.TpNo=TpNo
        self.HoursRATE=HoursRATE
        self.availability=availability


    def addLessonBooking(self):#Use the Instructor class to create an object, and then execute the addLessonBooking  method:



        if(isInsinDB(self.Name)):
            bookingNo=input("input booking no : ")

            addAbooking(self.Name,bookingNo)
        else:
            print("you are not registered..")




