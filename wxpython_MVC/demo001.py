#-*- coding:utf-8 -*-
__author__ = 'admin'
'''代码重构的要求，不要重复：不要模块般的重复操作， 一次只做一件事：比如说创建面板，按钮，把他们分别用方法来分开'''

import wx

class RefactorExample(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, size=(200, 300))
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour('White')
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.createMenuBar()
        self.createMenuBar(panel)
        self.createTextFields(panel)

    def OnCloseWindow(self):pass
    def menuData(self):
        return(("file", ("Open", "Open in status bar", self.OnOpen),
                ("Quit", "Quit", self.OnCloseWindow),
                ("Exit", ("Copy", "Copy", self.OnCopy),
                 ("Cut", "Cut", self.OnCut),
                 ("Paste", "Paste", self.OnPaste),
                 ("","",""),
                 ("Option", "Display options", self.OnOptions))))

    def createMenuBar(self):
        menuBar = wx.MenuBar()
        for eachMenuData in self.menuData():
            menuLabel = eachMenuData[0]
            menuItems= eachMenuData[1:]
            menuBar.Append(self.createMenu(menuItems), menuLabel)
        self.SetMenuBar(menuBar)

    def createMenu(self, menuData):
        menu = wx.Menu()
        for eachLabel, eachStatus, eachHandler in menuData:
            if not eachLabel:
                menu.AppendSeparator()
                continue
            menuItem = menu.Append(-1, eachLabel, eachStatus)
            self.Bind(wx.EVT_MENU, eachHandler, menuItem)
        return menu
    def buttonData(self):
        return (("First", self.OnFirst),
                ("<<PREV", self.OnPrev),
                ("NEXT", self.OnNext),
                ("Last", self.OnLast))

    def createButonBar(self, panel, yPos=0):
        xPos = 0
        for eachLabel, eachHandler in self.buttonData():
            pos = (xPos, yPos)
            button = self.buildOneButton(panel, eachLabel, eachHandler, pos)
            xPos += button.GetSize().width
    def buildOneButton(self, parent, id, handler, pos = (0,0)):
        button = wx.Button(parent, -1, label, pos)
        self.Bind(wx.EVT_BUTTON, handler, button)
        return button

    def textFields(self):
        return (("FirstName", (10, 50)),
                ("lastName", (10, 80)))

    def createTextFields(self, panel):
        for eachLabel, eachPos in self.textFieldsData():
            self.createCaptionedText(panel, eachLabel, eachPos)

    def createCaptionedText(self, panel, label, pos):
        static = wx.StaticText(panel, wx.NewId(), label, pos)
        static.SetBackgroundColour("White")
        textPos = (Pos[0] + 75, pos[1])
        wx.TextCtrl(panel, wx.NewId(), "", size = (100, -1), pos=textPos)

    def OnPrev(self, event): pass
    def OnNext(self, event): pass
    def OnLast(self, event): pass
    def OnFirst(self, event): pass
    def OnOpen(self, event): pass
    def OnCopy(self, event): pass
    def OnCut(self, event): pass
    def OnPaste(self, event): pass
    def OnOptions(self, event): pass
    def OnCloseWindow(self, event):
        self.Destroy()

app = wx.PySimpleApp()
frame = RefactorExample(parent=None, id=-1)
frame.Show()
app.MainLoop()






