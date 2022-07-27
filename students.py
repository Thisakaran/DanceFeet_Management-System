class Students:
    def __init__(self,StudentID,FirstNAME,LastNAME,Email,Sex,DOB,TpNo,Address,TypeOfDance,MaxHoursRate):
        # The __init__() function is called automatically every time the class is being used to create a new object.
        # The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
        self.StudentID=StudentID
        self.FirstNAME=FirstNAME
        self.LastNAME=LastNAME
        self.Email=Email
        self.Sex=Sex
        self.DOB=DOB
        self.TpNo=TpNo
        self.Address=Address
        self.TypeOfDance=TypeOfDance
        self.MaxHoursRate=MaxHoursRate


