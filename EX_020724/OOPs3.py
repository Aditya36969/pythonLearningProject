#Hirarhical inheritance
class Father:

    def house1(self):
        print("1house")

class Aditya(Father):

    def house2(self):
        print("2house")

class sahitya(Father):

    def house3(self):
        print("3house")

class saahas(Father):
    def nohouse(self):
        print("no_house")

adi = Aditya()
sai = sahitya()
saa= saahas()
adi.house1()
adi.house2()
sai.house1()
sai.house3()
saa.house1()
saa.nohouse()