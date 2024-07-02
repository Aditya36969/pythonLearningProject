# single inheritance
class parent:
    gold = "2kg"

    def BHK2(self):
        print("2BHK")


class child(parent):

    def BHK3(self):
        print("3BHK")


child_test= child()
child_test.BHK3()
child_test.BHK2()
print(child_test.gold())
