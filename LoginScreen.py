from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

import pandas as pd


class LoginScreen(App):

    def __init__(self):
        self.layout = None

    def build(self):


        self.layout = GridLayout()
        self.layout.cols = 2
        self.layout.rows = 5


        self.layout.add_widget(Label(text = 'Name:'))
        self.particName = TextInput(multiline=False)
        self.layout.add_widget(self.particName)


        self.layout.add_widget(Label(text = 'Surname:'))
        self.particSurname = TextInput(multiline=False)
        self.layout.add_widget(self.particSurname)


        self.layout.add_widget(Label(text = 'Age:'))
        self.particAge = TextInput(multiline=False)
        self.layout.add_widget(self.particAge)


        self.layout.add_widget(Label(text = 'Gender:'))
        self.particGender = TextInput(multiline=False)
        self.layout.add_widget(self.particGender)

        self.submitButton = Button(text = 'Submit')
        self.layout.add_widget(self.submitButton)
        self.submitButton.bind(on_press = self.submit)

        return self.layout

    def getPopup(self, p):
        self.popUp = p

    def submit(self, obj = None):
        self.dfParticipant = pd.DataFrame()
        self.dfParticipant.at[0,'Name'] = str(self.particName.text)
        self.dfParticipant.at[0,'Surname'] = str(self.particSurname.text)
        self.dfParticipant.at[0,'Age'] = str(self.particAge.text)
        self.dfParticipant.at[0,'Gender'] = str(self.particGender.text)
        self.dfParticipant.to_csv(str(self.particName.text)+'.csv', encoding='utf-8')
        self.popUp.dismiss()




    def call(self, obj=None):
        return self.run()




