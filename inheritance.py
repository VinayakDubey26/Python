class Person:
       def __init__(self,name,lname):
              self.name = name
              self.lname = lname

       def printname(self):
              print(self.name,self.lname)


x = Person("John","Doe")
x.printname()