class OldBrowser:

      def start_browser(self):
          print("IE browser is starting")

      def stop_browser(self):
          print("IE browser is Closing")


class Chrome(OldBrowser):


      def start_broswer(self):
          super().start_browser() #parent
          print("better chrome browser is starting..")

      def stop_broswer(self):
          print("better chrome browser is stopping..")



obj_ref=Chrome()
obj_ref.start_browser()
obj_ref.stop_browser()

@@revisit