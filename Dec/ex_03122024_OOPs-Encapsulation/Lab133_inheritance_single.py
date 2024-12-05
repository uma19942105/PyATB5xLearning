#single inheritance is used 85% of times in API automation
class Father:
    key = "2BHK-Flat"

    def car(self):
        print("Father has car -> alto")
        print(self.key)

# there is no  relationshp  between  father and  son when defined  lik this  in order  to bring inheritance this(class son:) need to be written as  class son(Father)
class Son(Father):  # this is single inheritance
    key2 ="3BHK Flat"

    def SUV(self):
        print("MG Hector, Black")
        print(self.key2)


father_obj=Father()
father_obj.car()

son_obj=Son()
son_obj.car()
