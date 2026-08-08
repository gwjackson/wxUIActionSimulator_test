import wx
from src.as_test.gui.main_frame import MainFrame

def main():
    """
    This is the main function and will call the GUI, Utilities, Core functions etc.
    :return: None
    """
    app = wx.App(False)
    frame = MainFrame()
    frame.Fit()
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()
