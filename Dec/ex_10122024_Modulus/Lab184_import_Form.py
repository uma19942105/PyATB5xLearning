from BrowserPackage.OpenBrowser import start_browser
from BrowserPackage.CloseBrowser import stop_browser


class TestCase:
    def test_Case(self):
        start_browser()
        print("Hello Running TC")
        stop_browser()


obj_tc = TestCase()
obj_tc.test_Case()