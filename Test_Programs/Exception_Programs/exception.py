from prg1 import Myexception
class Hcl_list():
    def __init__(self):
        self.list1=[]
    def insertelement(self):
        try:
            element=int(input("enter elements"))
            if element>100:
                raise Myexception("stupid")
            else:
                self.list1.append(element)
        except Myexception as e:
            print(e)
obj=Hcl_list()
obj.insertelement()




