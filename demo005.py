#-*-coding:utf-8-*-
__author__ = 'admin'
import wx

class InsertFrame(wx.Frame):#定义了一个Frame的子类
    '''初始化函数定义了连个窗口，一个panel, 一个button，将button与事件进行绑定，事件触发时，调用对应函数'''
    def __init__(self, parent, id):#初始化Frame子类
        wx.Frame.__init__(self, parent, id, 'Frame with Button', size=(300, 200))#调用InsertFrame父类的初始化函数，并传递了参数。
        panel = wx.Panel(self)#建立一个面板，panel中的元素可以被TAB遍历，而Frame不行，用sizers进行对象布局的控制。
        button = wx.Button(panel, label="close", pos = (125, 10), size=(50, 50))#创建一个按钮
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)#绑定按钮button功能为OnClose
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseMe(self, event):#定义了OnCloseMe函数
        self.Close(True)
    def OnCloseWindow(self, event):#定义了OnCloseWindow函数
        self.Destroy()

app = wx.PySimpleApp()#实例化PySimpleApp类
frame = InsertFrame(parent = None, id = -1)#实例化InsertFrame类
frame.Show()#显示框架
app.MainLoop()#app主循环

