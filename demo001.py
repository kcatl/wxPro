__author__ = 'admin'
import wx

class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, "MyFrame", size = (200, 300))
        panel = wx.Panel(self, -1)

        panel.Bind(wx.EVT_MOTION, self.OnMove)
        wx.StaticText(panel, -1, "Pos: ", pos = (10, 20))
        self.posCtrl = wx.TextCtrl(panel, -1, "", pos = (40, 10))

    def OnMove(self, event):
        pos = event.GetPosition()
        self.posCtrl.SetValue("%s, %s"% (pos.x, pos.y))
app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()


