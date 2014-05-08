__author__ = 'admin'
import wx
import images

class ToolbarFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'ToolBars', size=(200, 300))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        statusBar = self.CreateStatusBar()
        toolbar = self.CreateToolBar()
        toolbar.AddSimpleTool(wx.NewId(), images.getNewBitmap(), "New", "Loog help for New")
        toolbar.Realize()
        menuBar = wx.MenuBar()

        menu1 = wx.Menu()
        menuBar.Append(menu1, "File")
        menu2 = wx.Menu()

        menu2.Append(wx.NewId(), "Copy", "Copy in status bar")
        menu2.Append(wx.NewId(), "Cut", "")
        menuBar.Append(menu2, "Edit")
        self.SetMenuBar(menuBar)


app = wx.PySimpleApp()
frame = ToolbarFrame(parent = None, id = -1)
frame.Show()
app.MainLoop()