from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from opto import opto
from LoginScreen import LoginScreen
from kivy.uix.popup import Popup

class MyApp(App):

    def build(self):



        self.title = "PACE"

        self.objOpto = opto()

        self.objLogin = LoginScreen()

        self.demoLayout = self.objLogin.build()

        self.popup = Popup(title='Participant Information', content = self.demoLayout)
        self.objLogin.getPopup(self.popup)

        layout = BoxLayout(orientation = 'vertical')
        btn = Button(text = 'Start Optokinetic Test', background_normal = "", border = (10,10,10,10), background_color = (1, .3, .4, .85))
        btn2 = Button(text = 'Enter Participant Information')
        btn.bind(on_press = self.objOpto.runTest)
        btn2.bind(on_press = self.popup.open)

        layout.add_widget(btn2)
        layout.add_widget(btn)



        return layout

    def getpopup(self):
        return self.popup


if __name__ == '__main__':
    MyApp().run()



'''
First Button: Enter Login Screen
Second Button: Start the Optokinetic Test

'''
