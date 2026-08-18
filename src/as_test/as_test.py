import wx
from MyApp import MyApp
from gui.main_frame import MainFrame


#def main():
"""
This is the main launcher for the Application and will call the GUI, Utilities, Core functions etc.
"""


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    frame.Fit()
    frame.Show()
    app.MainLoop()