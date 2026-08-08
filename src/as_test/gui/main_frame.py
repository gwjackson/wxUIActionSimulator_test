import wx

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="My wxPython App", size=(800, 600))
        main_panel = wx.Panel(self)
        wx.StaticText(main_panel, label="Hello from wxPython!", pos=(20, 20))




def main():
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()
