
class Consoler:
    def __init__(self,console):
        self.console=console

    def clear(self):
        self.console.clear()

    def echoText(self,text,color="#000",feed=True):
        if feed:
            self.console.insertHtml(f"<font color='{color}'>{text}</font><br>")
        else:
            self.console.insertHtml(f"<font color='{color}'>{text}</font>")

    def echoError(self,text,feed=True):
        if feed:
            self.console.insertHtml(f"<font color='red'>Error : <b>{text}</b></font><br>")
        else:
            self.console.insertHtml(f"<font color='red'>Error : <b>{text}</b></font>")