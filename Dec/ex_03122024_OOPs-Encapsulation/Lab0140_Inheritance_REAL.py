class BaseTest:

    def open_browser(self):
        print("starting the browser")

    def read_from_excel(self):
        print("Read from excel")
        
    def close_browser(self):
        print("Close browser")

class TestCase1(BaseTest):

     def test_positive(self):
         self.open_browser()
         print("Test case P1 Executed !!")
         self.close_browser()

     def test_negative(self):
         self.open_browser()
         print("Test case N1 Executed !!")
         self.close_browser()

class Testcase2(BaseTest):

    def test_positive(self):
        self.open_browser()
        print("Test case P2 Executed !!")
        self.close_browser()



