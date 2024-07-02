# multiple inheritance(dimond problem solved)
# 

class Mother:
    key="old car"
    def Mother_method(self):
        print ("gf house")

class Father:
    key1="medium car"
    def Father_method(self):
        print ("Father house")
class son(Father,Mother):
    key3="new car"
    def son_method(self):
        return "son house"

beta= Father()
bike= son()
bike.Father_method()
bike.Mother_method()
bike.son_method()
print(bike.key3)
print(bike.key1)
print(bike.key)
print(beta.key1)
beta.Father_method()
#print(beta.key)



