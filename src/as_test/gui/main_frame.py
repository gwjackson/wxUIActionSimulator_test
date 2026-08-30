import wx

import as_test.core.macro_widget
# ? change this to import as_test.core.macro_widget as macro_widgets ?
macro_widgt = as_test.core.macro_widget

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="My wxPython App", size=(800, 600))
        self.main_panel = wx.Panel(self)


        ##########
        # build the main flexgridsizer - keep it simpel
        # FlexGridSizer(rows, cols, vgap, hgap) -> None
        # add several different widgets and a dialog for testing
        ##########

        self.fgs_main = wx.FlexGridSizer(3, 2, 5, 5)

        # add widgets sequentially (fills Row 1: Col 1, Col 2, then Row 2: Col 1, Col 2...)
        # row 1, col 1 radiobutton collection in a vertical box sizer
        self.rb_sizer = wx.BoxSizer(wx.VERTICAL)
        self.rb_group = []
        self.rb1 = wx.RadioButton(self.main_panel, -1, label="RB1 (Group 1)", style=wx.RB_GROUP)
        self.rb_sizer.Add(self.rb1, 0, wx.ALL, 5)
        self.rb2 = wx.RadioButton(self.main_panel, -1, label="RB2 (Group 1)")
        self.rb_sizer.Add(self.rb2, 0, wx.ALL, 5)
        self.rb3 = wx.RadioButton(self.main_panel, -1, label="RB3 (Group 1)")
        self.rb_sizer.Add(self.rb3, 0, wx.ALL, 5)
        self.rb4 = wx.RadioButton(self.main_panel, -1, label="RB4 (Group 1)")
        self.rb_sizer.Add(self.rb4, 0, wx.ALL, 5)
        self.rb_group.append(self.rb1)
        self.rb_group.append(self.rb2)
        self.rb_group.append(self.rb3)
        self.rb_group.append(self.rb4)
        # the reason for this_rb=rb ?
        # lambdas in loops capture the variable, not the value
        # Defalute arguments capture the value, not the variable
        # a python closure issue (feature)
        # freeze the value with the this_rb=rb statment!
        # clicking an already selected RB -> NO EVENT!
        # so bind to a right click as well if the user clicks on a selected RB
        for rb in self.rb_group:
            self.Bind(wx.EVT_MOUSE_EVENTS,
                      lambda evt, this_rb=rb: macro_widgt.onRBselect(this_rb, evt),
                      id=rb.GetId())
            self.Bind(wx.EVT_RADIOBUTTON,
                      lambda evt, this_rb=rb: macro_widgt.onRBselect(this_rb, evt),
                      id=rb.GetId())

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
        #bind all to same handler (see handler doc)
        self.ckb1.Bind(wx.EVT_CHECKBOX, macro_widgt.on_checkbox)
        self.ckb2.Bind(wx.EVT_CHECKBOX, macro_widgt.on_checkbox)
        self.ckb3.Bind(wx.EVT_CHECKBOX, macro_widgt.on_checkbox)
        self.ckb4.Bind(wx.EVT_CHECKBOX, macro_widgt.on_checkbox)

        self.fgs_main.Add(self.ckbx_sizer)

        # row2, col 1 wx.CombBox
        self.cbobx_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.cbob1 = wx.ComboBox(self.main_panel, -1, style=wx.CB_READONLY | wx.CB_DROPDOWN)
        self.cbob1.AppendItems(["Really First","Option 1", "The Other", "Something else"])
        self.cbob1.SetSelection(0)
        self.cbob1.Bind(wx.EVT_COMBOBOX, macro_widgt.on_combobox1)
        self.cbobx_sizer.Add(self.cbob1, 0, wx.ALL, 5)
        self.fgs_main.Add(self.cbobx_sizer)

        # row 2, col 2;  predefined dialog
        self.dlg_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.dlg_button = wx.Button(self.main_panel, -1, label="File Dialog")
        self.Bind(wx.EVT_BUTTON,
                  lambda evt: macro_widgt.on_dlg_button(self.dlg_button, evt),
                  id=self.dlg_button.GetId())
        self.dlg_sizer.Add(self.dlg_button, 0, wx.ALL, 5)
        self.fgs_main.Add(self.dlg_sizer)

        # add multiline text control
        self.tc_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.mult_line_tx = wx.TextCtrl(self.main_panel, -1, style=wx.TE_MULTILINE)
        self.mult_line_tx.SetToolTip("Tab or click any other control to enter text")
        # this lambda lets me package the widget and the event into the handler call
        self.mult_line_tx.Bind(wx.EVT_KILL_FOCUS,
                               lambda evt: macro_widgt.on_txtctrl_lost_focus(self.mult_line_tx, evt))
        self.tc_sizer.Add(self.mult_line_tx, 0, wx.ALL, 5)
        self.fgs_main.Add(self.tc_sizer)

        # add record/recording, playback buttons
        self.butn_sizer = wx.BoxSizer(wx.VERTICAL)
        self.record_btn = wx.Button(self.main_panel, -1, label="🔴 Record Macro")
        # Bind the external handler use a lambda function to pass the widget to the external routine(s)
        # this passes both the widget and the event
        # linking the record and playback buttons so can pass both in the lambda function
        self.record_btn.Bind(wx.EVT_BUTTON,
                             lambda evt: macro_widgt.on_record(self.record_btn, self.playback_btn, evt))
        self.record_btn.SetToolTip("Click this button or HotKey Alt+M to start / end macro recording")
        self.butn_sizer.Add(self.record_btn, 0, wx.ALL, 5)

        self.playback_btn = wx.Button(self.main_panel, -1, label="▶ Play Macro")
        self.playback_btn.SetToolTip("After recording click here to replay your macro")
        self.playback_btn.Bind(wx.EVT_BUTTON,
                             lambda evt: macro_widgt.on_play(self.record_btn, self.playback_btn, evt))
        self.butn_sizer.Add(self.playback_btn, 0, wx.ALL, 5)

        self.fgs_main.Add(self.butn_sizer)

        # set flexgrid
        self.main_panel.SetSizer(self.fgs_main)
        self.main_panel.Layout()


        # ---------------------------------------------------
        # Build the accelerator table
        # has to be below the GUI creation as that is what is referenced here
        # ---------------------------------------------------
        # create linking ID's for the wx.EVT_MENU to the accelerator in the table
        # here again using lambda functions to load the call to the handlers in macro_widget.py
        # this passes in the handler in macro_widget; the control and the evt as well

        ID_ALT_W =wx.NewIdRef()
        ID_ALT_M = wx.NewIdRef()

        self.Bind(wx.EVT_MENU,
                  lambda evt: macro_widgt.on_txtctrl_lost_focus(self.mult_line_tx, evt),
                  id=ID_ALT_W)
        self.Bind(wx.EVT_MENU,
                  lambda evt:  macro_widgt.on_record(self.record_btn, self.playback_btn, evt),
                  id=ID_ALT_M)

        self.accel_table = wx.AcceleratorTable([(wx.ACCEL_ALT, ord('W'), ID_ALT_W),
                                                (wx.ACCEL_ALT, ord('M'), ID_ALT_M),
                                                ])


        self.SetAcceleratorTable(self.accel_table)



        # I refactor the menu here? is part of this GUI
        #################################################
        # this frames menu
        #################################################

        self.menu_bar = wx.MenuBar()

        self.file_menu = wx.Menu()

        self.item_file_open = self.file_menu.Append(wx.ID_ANY, "&Open Macros\tCtrl+N", "Open Macro files")
        # using lambda to pass args self.item_file_open, and the event - evt
        # but the item ID is not part of the lambda but part of the binding
        self.Bind(wx.EVT_MENU,
                  lambda evt: macro_widgt.on_file_open_macors(self.item_file_open, evt),
                  id=self.item_file_open.GetId())

        self.item_file_save = self.file_menu.Append(wx.ID_ANY, "&Save Macros\tCtrl+M", "Save Macro files")
        self.Bind(wx.EVT_MENU,
                  lambda evt: macro_widgt.on_file_save_macors(self.item_file_save, evt),
                  id=self.item_file_save.GetId())

        self.file_menu.AppendSeparator()

        self.item_file_close = self.file_menu.Append(wx.ID_EXIT, "E&xit\tCtrl+Q", "Exit")
        self.Bind(wx.EVT_MENU,
                  lambda evt: macro_widgt.on_exit(self.item_file_close, evt),
                  id=self.item_file_close.GetId())

        self.menu_bar.Append(self.file_menu, "&File")

        self.help_menu = wx.Menu()
        self.help_menu.Append(wx.ID_ANY, "&Help")
        self.menu_bar.Append(self.help_menu, "&Help")

        self.macro_menu = wx.Menu()
        self.macro_menu.Append(wx.ID_ANY, "&Macro Options")
        self.menu_bar.Append(self.macro_menu, "&Macro")

        self.SetMenuBar(self.menu_bar)

    def FindWindowAtPointer(self, pos):
        # ScreenToClient()
        pos = self.ScreenToClient(pos)
        child = self.main_panel.FindWindowByLabel('RB1 (Group 1)', main_panel)
        return child



    # basic event handling;
    """
    moving all to the macro_widget.py after testing here
    -
    this is just to be GUI while macro_widget will have all the business stuff
    """


def main():
    app = wx.App(False)
    frame = MainFrame()
    frame.Fit()
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
