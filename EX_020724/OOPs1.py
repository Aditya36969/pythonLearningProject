

# Single inheritence

class GF: # parent class
    key = "abc@123"
    def grandparent_method(self):
        return "grandparents test"
class father(GF):   #child class
    def father_method(self):
        return "fathers test"

Father = father()
print(Father.father_method())
print(Father.grandparent_method())
print(Father.key)



