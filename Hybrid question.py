#Homework
class A:
    a = 1
class B(A):
    b = 1
class C(A):
    c = 1
class E(B):
    pass
class D(C):
    pass
class F(E,D):
    pass
a = A()
b = B()
c = C()
d = D()
e = E()
f = F()
