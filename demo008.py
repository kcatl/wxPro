#-×- coding:utf-8 -*-
__author__ = 'admin'
import wx
class MyFrame(wx.Frame):#子类化Frame
    def __init__(self, parent, id):#重写了初始化函数
        wx.Frame.__init__(self, parent, id, size=(300, 200))#调用了父类的初始化函数
        self.panel =wx.Panel(self)#建立了一个面板对象
        self.panel.SetBackgroundColour('Red')#添加了面板属性
        menuBar = wx.MenuBar()#建立了一个菜单栏
        menu1 = wx.Menu()#添加了菜单1
        menu2 = wx.Menu()#添加了菜单2
        menuItem = menu1.Append(-1, "&Exit")#添加了菜单1的下拉菜单
        menuItem3 = menu1.Append(-1, "&Open")
        menuItem4 = menu1.Append(-1, "&Setting")
        menuItem2 = menu2.Append(-1, "&About")#添加了菜单2的下拉菜单
        menuBar.Append(menu1, "&File")#将菜单1添加到菜单栏中
        menuBar.Append(menu2, "&Option")#将菜单2添加到菜单栏中
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.OnCloseMe, menuItem)#事件绑定
        self.Bind(wx.EVT_MENU, self.OnClickMe, menuItem2)#类型要写对，如果写成了EVT_BUTTON，则不会触发
        self.Bind(wx.EVT_MENU, self.OnClickMe, menuItem3)
        self.Bind(wx.EVT_MENU, self.OnClickMe, menuItem4)
    def OnCloseMe(self, event):#事件触发定义
        self.Close(True)
    def OnClickMe(self, event):
        self.panel.SetBackgroundColour('Green')
        self.panel.Refresh()#刷新了面板显示，否则不会显示对panel属性的修改

class MyApp(wx.App):

    def __init__(self, redirect = False, filename = None):
        wx.App.__init__(self, redirect, filename)
    def OnInit(self):
        self.frame = MyFrame(None, -1)




        self.frame.Show()
        return True

app = MyApp()
app.MainLoop()