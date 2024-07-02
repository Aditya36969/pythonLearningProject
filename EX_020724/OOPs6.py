# dimond problem in easy way

class A:
    def method(self):
        return "ABC"
class B:
    def method(self):
        return "BCD"
class C(B,A):  #prefrence is given to 1st class
    pass
c=C()
print(c.method())