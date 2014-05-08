__author__ = 'admin'
import wx

class Frame(wx.Frame):
    """this is a line for doc file"""
    def __init__(self, image, parent = None, id = -1, pos = wx.DefaultPosition, title = "hello , wxpython"):

        temp = image.ConvertToBitmap()
        size = temp.GetWidth(), temp.GetHeight()
        wx.Frame.__init__(self, parent, id, title, pos, size)
        self.bmp = wx.StaticBitmap(parent = self, bitmap = temp)

class App(wx.App):
    """Application pass"""
    def OnInit(self):
        image = wx.Image('wxpython.jpg', wx.BITMAP_TYPE_JPEG)
        self.frame = Frame(image)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

app = App()
app.MainLoop()