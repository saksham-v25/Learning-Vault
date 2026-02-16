class Student:
    def __init__(self,name,rollno,age):
         self.name=name
         self._rollno=rollno
         self.__age=age

    def get_age(self,):
        return self.__age
    def set_age(self,age):
        if age>35:
            print("Invalid age given..  Age sholud be less than 35")
        else:
            self.__age=age

s1=Student(" piyush",23,20)
print(s1.get_age())
s1.set_age(34)
print(s1.get_age())
