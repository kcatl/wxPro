__author__ = 'admin'
import wx

class Frame(wx.Frame):
    pass


class App(wx.App):
    def __init__(self):
        wx.App.__init__(self)
        frame = wx.Frame(parent = None, title = "Bare")
        frame.Show(True)
        return None

app = App()
app.MainLoop()