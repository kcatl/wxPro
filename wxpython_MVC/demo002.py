__author__ = 'admin'
import wx
import wx.grid


class LineupTable(wx.grid.PyGridTableBase):
    data = (("CF","BOB", "Denier"),("2B", "Ryne","Sandberg"))
    colLabels = ("Last", "First")

    def __init__(self):
        wx.grid.PyGridTableBase.__init__(self)
    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.data[0]) -1


    def GetColLabelValue(self, col):
        return self.colLabels[col]

    def GetRowLabelValue(self, row):
        return self.data[row][0]
    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        return self.data[row][col + 1]
    def SetValue(self,row, col, value):
        pass

class SimpleGrid(wx.grid.Grid):
    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent, -1)
        self.SetTable(LineupTable())

class TestFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "A Grid", size=(275, 275))
        grid = SimpleGrid(self)

app = wx.PySimpleApp()
frame = TestFrame(parent = None)
frame.Show(True)
app.MainLoop()



