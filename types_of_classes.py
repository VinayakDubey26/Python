class Person:
    def __init__(self,name,age):
        self.name = "John"
        self.age = 36

p1 = Person("John",36)

print(p1.name)
print(p1.age)



# str( method)
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("John",36)

print(p1.name)
