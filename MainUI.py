from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from opto import opto

class MyApp(App):

    def build(self):



        self.title = "PACE"
        self.obj = opto()

        layout = BoxLayout(orientation = 'vertical')
        btn = Button(text = 'Start Optokinetic Test', background_normal = "", border = (10,10,10,10), background_color = (1, .3, .4, .85))
        btn2 = Button(text = 'Enter Participant Information')
        btn.bind(on_press = self.obj.runTest)

        layout.add_widget(btn2)
        layout.add_widget(btn)



        return layout


if __name__ == '__main__':
    MyApp().run()



'''
First Button: Pop Up Window for Form
Second Button: Start the Optokinetic Test

'''
