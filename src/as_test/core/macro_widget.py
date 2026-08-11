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


"""
    if evt:
        obj = evt.GetEventObject()
        print("Widget:", obj)
        print("Parent:", obj.GetParent())
        print("Event type:", evt.GetEventType())
        print("Event ID:", evt.GetId())
        print("Timestamp:", evt.GetTimestamp())
"""
