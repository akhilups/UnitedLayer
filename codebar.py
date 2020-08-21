import pandas as pd

class Codebar():

    def __init__(self):
        self.data = {}
        self.data2 = {}
        self.addWorkshop()

    def addWorkshop(self):
        Name = input("Enter Workshop Subject: ")
        if self.data.get(Name, False):
            print("Workshop with same Subject already exist!..")
            #self.addWorkshopAgain()
        else:
            #self.data["Workshop"].append(Name)
            date = input("Enter Date: ")
            #self.data["Data"].append(date)
            self.data2={"Workshop":[],"date":[],"MemberList": [], "MemberInto": [], "MemberType": [], "Skills": [],"Bio":[],"reason":[]}
            self.addAllParticipants(Name, date)
                

    def addAllParticipants(self, Name, date):
        MemberName = input("Enter the Member name: ")
        Intro = input("Please introduce yourself: ")
        Member = input("Enter if Instructor/Student: ")
        if Member.lower() == "instructor":
            bio = input("Bio of Instructor attending PythonCon: ")
            reason= ""
            self.add_skill(Name,date,MemberName,Member,Intro,bio,reason)
        elif Member.lower() == "student":
           reason = input("Reason for attending PythonCon: ")
           skill = ""
           bio= ""
           self.add_List(Name,date,MemberName,Member,Intro,skill,reason,bio)
        else:
            print("Invalid Input")
            self.addParticipantsAgain(Name, date)
    
    
    def add_List(self,Name,date,MemberName,Member,Intro,skill,reason,bio):
        self.data2["Workshop"].append(Name)
        self.data2["date"].append(date)
        self.data2["MemberList"].append(MemberName)
        self.data2["MemberInto"].append(Intro)
        self.data2["MemberType"].append(Member)
        self.data2["Skills"].append(skill)
        self.data2["Bio"].append(bio)
        self.data2["reason"].append(reason)
        self.addParticipantsAgain(Name, date)
        
 
    def add_skill(self, Name,date,MemberName,Member,Intro,bio,reason):
        skill = input("Enter the skill: ")
        self.add_List(Name,date,MemberName,Member,Intro,skill,reason,bio)
    

    def addParticipantsAgain(self,Name,date):
        add_Member = input("Do you want to add New Member (Yes/No): ")
        if add_Member.lower() == "yes":
            self.addAllParticipants(Name,date)
        elif add_Member.lower() == "no":
           # self.addWorkshopAgain()
           self.print_details()
        else:
            print("Invalid Input")
            self.addParticipantsAgain(Name,date)

    def print_details(self):
        df= pd.DataFrame(self.data2)
        print(df)


Codebar()