from textual.app import App
from textual.widgets import Input, Label, Header, Footer,Button
import pyfiglet
f = pyfiglet.figlet_format('MediaStorOptimizer',width=110)


class NewApp(App):
    def compose(self):
        yield Button("asdasdasd")
    

class MainApp(App):
    #Tells us what widgets this application will be using
    def compose(self):
        yield Header(show_clock=True)
        yield Label(f)
        yield Input(placeholder="Input Whatever")
        yield Button("START")
        yield Button("Stop")
        yield Footer()
    
    def something(self):
        input=self.query_one(Input)
        uname=input.value
        self.mount(Label(uname))
        input.value=""

MainApp().run()

