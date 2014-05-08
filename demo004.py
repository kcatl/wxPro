__author__ = 'admin'
import wx,sys

class Frame(wx.Frame):
    def __init__(self, parent, id, title):
        print 'Frame__init__'
        wx.Frame.__init__(self, parent, id, title)

class App(wx.App):
    def __init__(self, redirect=True, filename = None):
        print "APP_init"
        wx.App.__init__(self, redirect, filename)
    def OnInit(self):
        print "OnInit"
        self.frame = Frame(parent = None, id = -1, title = 'Startup')
        self.frame.Show()
        self.SetTopWindow(self.frame)
        print >> sys.stderr, "A pressed message"
        return True

    def OnExit(self):
        print "OnExit"

app = App(redirect=False)
print 'before Mainloop'
app.MainLoop()
print "after MainLoop"
