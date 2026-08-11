import wx

#from gui.as_menus import File_menu
from core.macro_widget import on_record



class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="My wxPython App", size=(800, 600))
        self.main_panel = wx.Panel(self)
        #wx.StaticText(main_panel, label="Hello from wxPython!", pos=(20, 20))

        ##########
        # build the main flexgridsizer - keep it simpel
        # FlexGridSizer(rows, cols, vgap, hgap) -> None
        # add several different widgets and a dialog for testing
        ##########

        self.fgs_main = wx.FlexGridSizer(3, 2, 5, 5)

        # add widgets sequentially (fills Row 1: Col 1, Col 2, then Row 2: Col 1, Col 2...)
        # row 1, col 1 radiobutton collection in a vertical box sizer
        self.rb_sizer = wx.BoxSizer(wx.VERTICAL)
        self.rb1 = wx.RadioButton(self.main_panel, -1, label="RB1 (Group 1)", style=wx.RB_GROUP)
        self.rb_sizer.Add(self.rb1, 0, wx.ALL, 5)
        self.rb2 = wx.RadioButton(self.main_panel, -1, label="RB2 Group 1)")
        self.rb_sizer.Add(self.rb2, 0, wx.ALL, 5)
        self.rb3 = wx.RadioButton(self.main_panel, -1, label="RB3 Group 1)")
        self.rb_sizer.Add(self.rb3, 0, wx.ALL, 5)
        self.rb4 = wx.RadioButton(self.main_panel, -1, label="RB4 Group 1)")
        self.rb_sizer.Add(self.rb4, 0, wx.ALL, 5)
        self.fgs_main.Add(self.rb_sizer, 1, wx.EXPAND)

        # row 1, col 2 checkboxes
        self.ckbx_sizer = wx.BoxSizer(wx.VERTICAL)
        self.ckb1 = wx.CheckBox(self.main_panel, -1, label="CKB1")
        self.ckb2 = wx.CheckBox(self.main_panel, -1, label="CKB2")
        self.ckb3 = wx.CheckBox(self.main_panel, -1, label="CKB3")
        self.ckb4 = wx.CheckBox(self.main_panel, -1, label="CKB4")
        self.ckbx_sizer.Add(self.ckb1, 0, wx.ALL, 5)
        self.ckbx_sizer.Add(self.ckb2, 0, wx.ALL, 5)
        self.ckbx_sizer.Add(self.ckb3, 0, wx.ALL, 5)
        self.ckbx_sizer.Add(self.ckb4, 0, wx.ALL, 5)

        self.fgs_main.Add(self.ckbx_sizer)

        # row2, col 1 wx.CombBox
        self.cbobx_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.cbob1 = wx.ComboBox(self.main_panel, -1)
        self.cbob1.AppendItems(["Really First","Option 1", "The Other", "Something else"])
        self.cbob1.SetSelection(0)
        self.cbobx_sizer.Add(self.cbob1, 0, wx.ALL, 5)
        self.fgs_main.Add(self.cbobx_sizer)

        # row 2, col 2;  predefined dialog
        self.dlg_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.dlg_button = wx.Button(self.main_panel, -1, label="File Dialog")
        self.dlg_button.Bind(wx.EVT_BUTTON, self.on_dlg_button)
        self.dlg_sizer.Add(self.dlg_button, 0, wx.ALL, 5)
        self.fgs_main.Add(self.dlg_sizer)

        # add multiline text control
        self.tc_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.mult_line_tx = wx.TextCtrl(self.main_panel, -1, style=wx.TE_MULTILINE)
        self.tc_sizer.Add(self.mult_line_tx, 0, wx.ALL, 5)
        self.fgs_main.Add(self.tc_sizer)

        # add record/recording, playback buttons
        self.butn_sizer = wx.BoxSizer(wx.VERTICAL)
        self.record_btn = wx.Button(self.main_panel, -1, label="🔴 Record Macro")
        self.record_btn.SetToolTip(
            "Click this button and then type, click, mouse around\n"
            "to record your macro. Then click here again when done.")
        # Bind the external handler use a lambda function to pass the widget to the external routine(s)
        # this passes both the widget and the event
        # linking the record and playback buttons so can pass both in the lambda function
        self.record_btn.Bind(wx.EVT_BUTTON, lambda evt: on_record(self.record_btn, self.playback_btn, evt))
        self.butn_sizer.Add(self.record_btn, 0, wx.ALL, 5)
        self.playback_btn = wx.Button(self.main_panel, -1, label="▶ Play Macro")
        self.playback_btn.SetToolTip("After recording click here to replay your macro")
        self.butn_sizer.Add(self.playback_btn, 0, wx.ALL, 5)
        self.fgs_main.Add(self.butn_sizer)

        # set flexgrid
        self.main_panel.SetSizer(self.fgs_main)
        self.main_panel.Layout()

    # basic event handling;
    def on_dlg_button(self, evt):
        # Wildcard string matching all files
        wildcard = "All files (*.*)|*.*"

        with wx.FileDialog(
                parent=self.main_panel,
                message="Select a file",
                defaultDir="",
                defaultFile="",
                wildcard=wildcard,
                style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST ) as file_dialog:
            # Show the dialog modally
            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return None  # User canceled

            # Return the selected file path
            #return file_dialog.GetPath()
            print(file_dialog.GetPath())



def main():
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()
