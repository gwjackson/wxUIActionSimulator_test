import wx
import time



class UI_Simulator(wx.UIActionSimulator):
    """
    Custom wrapper around wx.UIActionSimulator to provide high-level
    recording replay and interaction routines.
    """
    def __init__(self):
        super().__init__()
        pass


def on_record(record, playback, evt=None):
    """
    use a lamda function in the .Bind
    # Bind the external handler
        wx.EVT_BUTTON,
            lambda evt: on_record(self.record_btn, self.playback_btn, evt)
    toggle record/recording
    toggle enable / disable playback
    build the macro list of moves / clicks / chars / etc.
    :return:
    """

    if record.GetLabel() == "🔴 Record Macro":
        record.SetLabel("⏹ Stop Recording")
        playback.Disable()
        start_time = time.time()
        recording = True
        _start_record_macro(recording)
    else:
        record.SetLabel("🔴 Record Macro")
        playback.Enable()
        print("Stopped recording")
        return

def _start_record_macro(recording):
        print("recording")
        pass

# ------------------------------------------------
# Menu selections
# ________________________________________________
def on_file_open_macors(self, evt):
    print("File Open menu selected Ctrl+N")

def on_file_save_macors(self, evt):
    print("File Save menu selected Ctrl+M")

def on_exit(self, evt):
    print(f"Exit menu selected Ctrl+Q")
    wx.GetApp().ExitMainLoop()

def on_txtctrl_lost_focus( widget,evt=None):
    text = widget.GetValue()
    print("lost focus text is ->", text)
    # need the skip to allow the lost focus event to propagate normally
    evt.Skip()


# --------------------------------------------------
# dialog call
# ---------------------------------------------------

def on_dlg_button(self, evt):
    # Wildcard string matching all files
    wildcard = "All files (*.*)|*.*"

    with wx.FileDialog(
            #parent=self.main_panel,
            parent = None,
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




""" 
    some items that the event object has you can query 
    if evt:
        obj = evt.GetEventObject()
        print("Widget:", obj)
        print("Parent:", obj.GetParent())
        print("Event type:", evt.GetEventType())
        print("Event ID:", evt.GetId())
        print("Timestamp:", evt.GetTimestamp())
"""
