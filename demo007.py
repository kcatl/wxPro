__author__ = 'admin'
import wx

class MyFrame(wx.Frame):#子类化wx.Frame
    def __init__(self, parent, id):#重写初始化函数
        wx.Frame.__init__(self, parent, id, 'ToolBar', size=(200, 300))#引用父类的初始化函数
        panel = wx.Panel(self)#定义了一个面板
        panel.SetBackgroundColour('Red')#为该面板添加了颜色属性
        button = wx.Button(panel, label="Ok", pos=(20, 30), size=(40,30))#建立了一个按钮元素
        self.Bind(wx.EVT_BUTTON, self.CloseMe, button)#绑定了按钮的功能

    def CloseMe(self, event):#定义了按钮功能函数
        self.Close(True)

app = wx.PySimpleApp()#实例化一个应用程序对象
frame = MyFrame(parent = None, id = -1)#实例化一个Frame对象，这和主应用程序对象都是wxpython必须的。
frame.Show()#展示了frame
app.MainLoop()#应用程序主循环
