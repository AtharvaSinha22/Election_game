#OOps(Object Oriented Programming)

'''
##5 concepts
##1. Class and Object
##2. Encapsulation
##3. Inheritence
##4. Abstraction
##5.Polymorphisam
##
##'''
####class Myclass:
####    def _init_(self,a):
####       self.a = a
####mc = Myclass(29)
##
###Encapsulation
##class encap:
##    _a=13
##    _a = 23
##    c = _a + _a
##e = encap()
##
###Inheritence
##class Parent:
##    a = 1
##
##class Child(Parent):
##    b = 1
##class Grandchild(Child):
##  pass
##p = Parent()
##c = Child()
##gc = Grandchild()
##
##
###Multiple Inheritence
##class Father:
# #    f = 14
##class Mother:
##    m = 28
##class Child(Mother,Father): 
##f = Father()
##m = Mother
##c = Child()


#Hybrid Inheritence homework question
##'''
##A- b,c
##b -e
##e , f
##c - p
##p - f
##
##'''
##class Parent:
##    def _init_(self,a):
##        self.a = a
##class child(Parent):
##    def _init_(self,a,b):
##        super()._init_(a)
##        self.b = b
##p = Parent("TGC")
##c = child("ABC")


#Abstraction
from abc import ABC,abstractmethod

class Car(ABC):

    @abstractmethod
    def engine(self):
        print("Engine available")
    @abstractmethod
    def wheel(self):
        print("ceat tyres")
m = Maruti()



#polymorphism
