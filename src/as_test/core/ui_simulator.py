import wx

class UI_Simulator(wx.UIActionSimulator):
    """
    Custom wrapper around wx.UIActionSimulator to provide high-level
    recording replay and interaction routines.
    """
    def __init__(self):
        super().__init__()