class Parent:

     def home(self):
         print("2BHK")

class Son(Parent):
#here its overridden
    """def home(self):
        print("3BHK")"""
#with out over ridden
    def town(self):
        print("3BHK")
ob_Ref =Son()
ob_Ref.home()
ob_Ref.town()
