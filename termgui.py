from textual.app import App
from textual import on
from textual.widgets import Input, Label, Header, Footer,Button,Static
import pyfiglet
f = pyfiglet.figlet_format('MediaStorOptimizer',width=110)

#You import on, in order to set the buttons

#You can add CSS to this program; you can edit the components by calling them directly as written e.g EntryPath{layout:horizontal}
#You can link a css file to the program rather than hard coding the code
#Individual components have an attribute named id, you can edit by id this way

#Try to make it so that the output is listed on an other segment of the program
class NewApp(App):
    def compose(self):
        yield Button("asdasdasd")
    
class EntryPath(Static):

    #Read the files in the listed path
    @on(Button.Pressed)
    def readFiles(self,filePath):
        pass


    def compose(self):
        yield Input("Enter Folder Path")
        yield Button("Enter",variant="success")

class MainApp(App):

    @on(Button.Pressed,"#stop")
    def stop(self):
        self.app.exit()

    #Tells us what widgets this application will be using
    def compose(self):
        yield Header(show_clock=True)
        yield Label(f)
        yield EntryPath()
        yield Button("Stop",variant="error",id="stop")
        yield Footer()
    
    def something(self):
        input=self.query_one(Input)
        uname=input.value
        self.mount(Label(uname))
        input.value=""
NewApp().run()
MainApp().run()

