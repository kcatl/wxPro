__author__ = 'admin'
import wx
class MouseEventMove(wx.Frame):#定义了Frame子类
    def __init__(self, parent, id):#重写了初始化函数，并确定了2个参数
        wx.Frame.__init__(self, parent, id, 'Frame with Button', size=(200, 300))#调用了父类Frame的初始化函数
        self.panel = wx.Panel(self)#添加了一个面板
        self.button = wx.Button(self.panel, label="Not Over", pos = (10, 30))
        self.Bind(wx.EVT_BUTTON, self.OnButtonClick, self.button)#事件进行绑定
        self.button.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterWindow)
        self.button.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow)

    def OnButtonClick(self, event):
        self.SetBackgroundColour('Red')
        self.panel.Refresh()


    def OnEnterWindow(self, event):
        self.button.SetLabel('Over me!')
        event.Skip()


    def OnLeaveWindow(self, event):
        self.button.SetLabel('Not Over!')
        event.Skip()


app = wx.PySimpleApp()
frame = MouseEventMove(parent=None, id=-1)#MouseEventMove初始化函数中定义了2个参数
frame.Show()
app.MainLoop()


