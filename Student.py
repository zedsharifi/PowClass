class student:
    def __init__(self, FirstName, LastName, StudentNumber, MelliCode):
        self.MelliCode = MelliCode
        self.StudentNumber = StudentNumber
        self.LastName = LastName
        self.FirstName = FirstName

    def Show_info(self):
        print("First Name: ", self.FirstName)
        print("Last Name: ", self.LastName)
        print("Student Number: ",self.StudentNumber)
        print("Melli Code: ", self.MelliCode)

    def login(self):
        if len(self.StudentNumber)==9:
            print("matched!")
        else:
            print("not matched!")