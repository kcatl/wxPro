#--×-- coding:utf-8 -*-
__author__ = 'admin'
import wx
'''介绍了如何自定义事件，添加绑定器和触发函数'''
class TwoButtonEvent(wx.PyCommandEvent):#定义了事件,是wx.PyCommandEvent的子类
    def __init__(self, evtType, id):#重写了初始化函数
        wx.PyCommandEvent.__init__(self, evtType, id)#调用了父类的初始化函数
        self.clickCount = 0#添加了一个属性

    def GetClickCount(self):#定义了TwoButtonEvent的方法，并返回了clickCount的值
        return self.clickCount

    def SetClickCount(self, count):
        self.clickCount = count

myEVT_TWO_BUTTON = wx.NewEventType()#创建一个事件类型,返回了事件的ID并唯一标识这个事件，作用类似于wx.NewId()
EVT_TWO_BUTTON = wx.PyEventBinder(myEVT_TWO_BUTTON, 1)#创建了一个绑定器对象



class TwoButtonPanel(wx.Panel):
    def __init__(self, parent, id=-1, leftText="LEFT", rightText="Right"):#初始化了leftText和rightText两个变量
        wx.Panel.__init__(self, parent, id)
        self.leftButton = wx.Button(self, label=leftText)#初始化了左右两个按钮
        self.rightButon = wx.Button(self, label=rightText, pos=(100, 0))
        self.leftClick = False#初始化了变量的初值
        self.rightClick = False
        self.clickCount = 0

        self.leftButton.Bind(wx.EVT_LEFT_DOWN, self.OnLeftClick)#对绑定器和函数进行绑定
        self.rightButon.Bind(wx.EVT_RIGHT_DOWN, self.OnRightClick)

    def OnLeftClick(self, event):
        self.leftClick = True
        self.OnClick()
        event.Skip()#继续处理

    def OnRightClick(self, event):
        self.rightClick = True
        self.OnClick()
        event.Skip()


    def OnClick(self):
        self.clickCount += 1
        if self.leftClick or self.rightClick:
            self.leftClick = False
            self.rightClick = False
            evt = TwoButtonEvent(myEVT_TWO_BUTTON, self.GetId())
            evt.SetClickCount(self.clickCount)#添加数据到事件
            self.GetEventHandler().ProcessEvent(evt)#处理事件,GetEventHandler返回了对象，ProcessEvent将其放入了事件处理系统中

class CustomEventFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent=None, id=-1, title="Click Count:0 ", size=(200, 300))
        panel = TwoButtonPanel(self)
        self.Bind(EVT_TWO_BUTTON, self.OnTwoClick, panel)#绑定自定义事件
    def OnTwoClick(self, event):
        self.SetTitle("Click Count : %s" % event.GetClickCount())


app = wx.PySimpleApp()
frame = CustomEventFrame(parent=None, id=-1)
frame.Show()
app.MainLoop()



