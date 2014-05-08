__author__ = 'admin'
#-*-coding:utf-8 -*-
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "ClickButtonandChangeColor",size=(300, 500))#调用了父类的初始化函数，并对参数进行了传递
        self.panel = wx.Panel(self)#建立了一个面板
        self.panel.SetBackgroundColour('White')#定义了默认的面板颜色属性
        self.button = wx.Button(self.panel, label='ClickRed', pos=(10, 20), size=(70, 30))#使用关键字参数进行传递不容易出错
        self.button1 = wx.Button(self.panel, label='ClickGreen', pos=(110, 20), size=(70, 30))
        self.button2 = wx.Button(self.panel,  label='ClickBlue', pos=(210, 20), size=(70,30))
        self.Bind(wx.EVT_BUTTON, self.OnColorRed, self.button)#对事件进行了绑定
        self.Bind(wx.EVT_BUTTON, self.OnColorGreen, self.button1)
        self.Bind(wx.EVT_BUTTON, self.OnColorBlue, self.button2)
        self.button4 = wx.Button(self.panel, label='Red', pos=(10, 150), size=(70, 30))#使用关键字参数进行传递不容易出错
        self.button5 = wx.Button(self.panel, label='Green', pos=(110, 150), size=(70, 30))
        self.button6 = wx.Button(self.panel,  label='Blue', pos=(210, 150), size=(70,30))
        self.button4.Bind(wx.EVT_ENTER_WINDOW, self.OnColorRed)
        self.button4.Bind(wx.EVT_LEAVE_WINDOW, self.OnColorDefault)
        self.button5.Bind(wx.EVT_ENTER_WINDOW, self.OnColorGreen)
        self.button5.Bind(wx.EVT_LEAVE_WINDOW, self.OnColorDefault)
        self.button6.Bind(wx.EVT_ENTER_WINDOW, self.OnColorBlue)
        self.button6.Bind(wx.EVT_LEAVE_WINDOW, self.OnColorDefault)



    #定义触发函数

    def OnColorDefault(self, event):
        self.panel.SetBackgroundColour('White')
        self.panel.Refresh()

    def OnColorRed(self, event):
        self.panel.SetBackgroundColour('Red')
        self.panel.Refresh()#对面板属性进行刷新以在面板中显示属性更改

    def OnColorGreen(self, event):
        self.panel.SetBackgroundColour('Green')
        self.panel.Refresh()
    def OnColorBlue(self, event):
        self.panel.SetBackgroundColour('Blue')
        self.panel.Refresh()


app = wx.PySimpleApp()
frame = MyFrame(parent=None, id=-1)#这里的参数传递需要和MyFrame定义的初始化函数参数相对应，采用了关键字参数进行传递
frame.Show()
app.MainLoop()


