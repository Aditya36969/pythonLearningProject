# multilevel inheritance

class GF:
    key="old car"
    def gf_method(self):
        return "gf house"

class Father(GF):
    key1="medium car"
    def Father_method(self):
        return "Father house"
class son(Father):
    key3="new car"
    def son_method(self):
        return "son house"

beta= Father()
bike= son()
bike.Father_method()
bike.gf_method()
bike.son_method()
print(bike.key3)
print(bike.key1)
print(bike.key)
print(beta.key1)
beta.Father_method()
print(beta.key)



