import wx
from src.as_test.gui.main_frame import MainFrame
from src.as_test.gui.as_menus import File_menu

def main():
    """
    This is the main function and will call the GUI, Utilities, Core functions etc.
    :return: None
    """
    app = wx.App(False)
    frame = MainFrame()


    # Instantiate and assign the imported menu bar
    menu_bar = File_menu(MainFrame)
    frame.SetMenuBar(menu_bar)

    frame.Fit()
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()
