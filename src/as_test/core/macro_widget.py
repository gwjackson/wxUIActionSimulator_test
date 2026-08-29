import wx
import time
import functools

# module level state class
class _State:
    last_record_btn = None
    last_playback_btn = None
    last_event = None
    last_contest = None

    def reset_state(self):
        state.last_record_btn = None
        state.last_playback_btn = None
        state.last_event = None
        state.last_context = None

state = _State()



class UI_Simulator(wx.UIActionSimulator):
    """
    Custom wrapper around wx.UIActionSimulator to provide high-level
    recording replay and interaction routines.
    """
    def __init__(self):
        super().__init__()
        pass

# this needs to be moved down to the new Macro class
# MacroManager to be in that class
def on_record(record, play, evt=None):
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
    state.last_play_btn = play
    state.last_record_btn = record

    macros = MacroManager()

    if record.GetLabel() == "🔴 Record Macro":
        record.SetLabel("⏹ Stop Recording")
        play.Disable()
        start_time = time.time()
        macros.start_recording()
    else:
        record.SetLabel("🔴 Record Macro")
        play.Enable()
        macros.stop_recording("Test Macro")
        return

def on_play(record, play,  evt=None):
    state.last_play_btn = play
    state.last_record_btn = record
    macros = MacroManager()

    if play.GetLabel() == "Play Macro":
        play.SetLabel("Playing Macro")
        record.Disable()
        print("Playing Macro")
        #macros.apply_macro(self.macro_name)
    else:
        play.SetLabel("Play Macro")
        record.Enable()
        print("stop Playing Macro")
    return



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
        print(file_dialog.GetPath())
        return file_dialog.GetPath()




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

# ------------------------------------------------------------------
# Command Classes
# ------------------------------------------------------------------
class MacroCommand(wx.Command):
    def __init__(self, widget, new_value, old_value, label="Macro Command"):
        super().__init__(True, label)
        self.widget = widget
        self.new_value = new_value
        self.old_value = old_value

    def Do(self ):
        self.widget.SetValue(self.new_value)
        return True

    def Undo(self ):
        self.widget.SetValue(self.old_value)
        return True


class CompositeMacroCommand(wx.Command):
    def __init__(self, actions, label="Composite Macro"):
        super().__init__(True, label)
        self.actions = actions                      #list of (widget, new, old)

    def Do(self ):
        for widget, new_value, old_value in self.actions:
            widget.SetValue(new_value)
        return True

    def Undo(self ):
        for widget, new_value, old_value in self.actions:
            widget.SetValue(old_value)
        return True


class MacroManager:
    def __init__(self):
        self.processor = wx.CommandProcessor()
        self.recording = False                                      #should this be read from the app Macro button?
        self.record_buffer = []
        self.user_macros = {}

    # --------------------------------
    # Recording control
    # --------------------------------
    def start_recording(self):                       # toggle record macro / stop recording: to have to refractor this from above
        self.macro_Name = "test_macro"               # need to get user input for macro name
        self.recording = True
        self.record_buffer.clear()
        print("Macro started recording")
        # add call macro recorder to actually get it started

    def stop_recording(self, macro_name):
        self.recording = False
        self.user_macros[macro_name] = list(self.record_buffer)
        print("Macro stopper recording")
        # call on_record to toggle off


    # -----------------------------------------
    #  Decorator
    # -----------------------------------------
    """
    Every widget / hotkey etc. that you want to include in a macro has to 
    1. run it's business logic i.e. what you want the widget to do launch record etc. 
    2. has to capture is initial state
    3  had to capture is final state (this is for the Do / Undo function of command)
    4. append its self on to the record_buffer
    Now that is a lot of boiler plate for every widget -- > so a decorator just makes sense
    And you need to only decorate user generated events that you want to record, not all your widgets
    For instance you do not what to record the 'Record', 'Stop Recording', 'Playback' buttons you 
    would create a crazy loop and cause a tear in the space-time continuum 
    """
    def recoradable(self, widget_getter):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # 1 run the business logic
                result = func(*args, **kwargs)

                if self.recording:
                    # @self.macros.recordable(lambda self, widget, event: widget) is for the widget handler
                    widgets = widget_getter(*args, **kwargs)

                    if not isinstance(widgets, (list, tuple)):
                        widgets = [widgets]

                    for widget in widgets:
                        new_value = widget.GetValue()
                        self.record_buffer.append((widget, new_value, new_value))
                return result
            return wrapper
        return decorator

    # ----------------------------------------
    # Replay macro
    # ________________________________________
    def apply_macro(self, macro_name):
        actions = self.user_macros.get(macro_name)
        if not actions:
            return

        cmd = CompositeMacroCommand(actions, label=f'Macro: {macro_name}')
        self.processor.Submit(cmd)
        # call on_play to toggle off

    # ---------------------------------------------
    # Undo / Redo  (not sure will be using but is part of Command / CommandProcessor
    # ----------------------------------------------
    def undo(self):
        self.processor.Undo()

    def redo(self):
        self.processor.Redo()


