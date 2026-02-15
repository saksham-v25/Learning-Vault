class Student:
    def  __init__(self,name,rollno,age):
        self.name=name         #public instance variable
        self._rollno=rollno    #protected instance variable
        self.__age=age         #private instance variable

    def display(self):
        print(f"Hi myself {self.name} {self.__age} year old rollno {self._rollno}")


    def displayPrivateData(self):
        self.display()

class Branch(Student):
    def show(self):
        print(f"my rollno is {self._rollno}")
def showData():
    b1=Branch("Nisha",22,22)
    print(b1.name)
    print(b1._rollno)

    s1=Student("sam",22,20)
    print(s1.name)
    s1.display()
    s1.displayPrivateData()

showData()