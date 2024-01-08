#we have parametrized and default type of constructor

# 1. lets do default
# ==> yadi fun ma self sanga kunai kura parameter passed hunna vane tyo default constructor ho

class Person:
    name="Rabin"
    occupation="student"
    age=20
    
    def func(self):
        print("My name is=",self.name,"\nMy occupation is=",self.occupation,"\nMy age is=",self.age)
        self.name="Shiva"
        print("My name is=",self.name,"\nMy occupation is=",self.occupation,"\nMy age is=",self.age)

object=Person()
object.func()    

# 2. lets do parametrized constructor
# ==> parametrized constructor vanako chai function ma self lay kahi parameter leko hunu
# paryo    

class Person:
   
    
    def func(self,name,occupation,age):
         self.name="Rabin"
         self.occupation="student"
         self.age=20
         
object=Person("Rabin","student",20)
print("The name is=",object.name,"\nThe occupation is=",object.occupation,"\nThe age is=",object.age)

        