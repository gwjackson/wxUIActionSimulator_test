# subclass of wx.App
import wx
#from controller import Controller
from hotkeys import HotKeyManager
#from gui.main_frame import MainFrame
# from  import other frames


"""
Main job is to Filter Events w/ App.FilterEvent to be able to implement system wide
   HotKeys / shifts / chords
   MyApp (wx.App), --> Controller --> Frames
       it owns the EventFilter and hotkey manager
           HotkeyManager normalized the hotkeys, combos etc.
           MyApp only detects the events the Controller decides what happens
   Controller owns the applications logic for the events (not the business logic)
   Frames are the pure UI
       no global logic
       does keep list of local hotkeys read / passed to the EventFilter -> Controller
       |
       |-- appp.py                 wx.App subclass + EventFilter + Startup
       |                               owns the event fild=ter and hotkey manager
       |-- controller.py           Controller layer (routes hotkeys --> frames)
       |                               owns the logic
       |-- hotkeys.py              is resuable and independent
       |-- frames/                 GUI's
       |    |--.__init__.py
       |    |-- main_frame.py
       |    |-- other frames.py
       |-- as_test.y              entry point to launch
MyApp never call frames directly.  The controller decides what frames should do
"""

"""
need a App level get_comb at top of filter out ignored events so only useful stiff falls through
for the HotKeyManager to deal with 

???? Take the similar code out of HotKeyManager ????
"""
def get_combo(evt):
    parts = []
    if evt.ControlDown(): parts.append("Ctrl")
    if evt.AltDown():     parts.append("Alt")
    if evt.ShiftDown():   parts.append("Shift")
    if evt.MetaDown():    parts.append("Meta")

    keycode = evt.GetKeyCode()

    # Ignore modifier only keys
    if keycode in (wx.WXK_CONTROL, wx.WXK_ALT, wx.WXK_SHIFT, wx.WXK_WINDOWS_MENU):
        return None

    # Printable ASCII
    if 32 <= keycode <= 126:
        parts.append(chr(keycode).upper())
    else:
        parts.append(str(keycode))
    return "+".join(parts)


class MyApp(wx.App):

    WINDOWS_DEFAULT_IGNORES = {
        "Ctrl+C", "Ctrl+V", "Ctrl+X",
        "Ctrl+Z", "Ctrl+A", "Ctrl+S",
        "Ctrl.P",
    }                                    # can add others here this is just a start

     # -------------------------------------------------------------
    def OnInit(self):
        self.hotkeys = HotKeyManager()

        #self.controller = Controller()

        # Example global hotkey
        self.hotkeys.bind("Alt+Q", self.quit_app)           # got to check where this and other callables go
        return True

    def quit_app(self):
        wx.CallAfter(self.Exit)


def FilterEvent(self, evt):
    if isinstance(evt, wx.KeyEvent):
        keycode = evt.GetKeyCode()
        etype = evt.GetEventType()

        # -------------------------------------------
        # A



    # ----------------------------------------------------

        f0 = MainFrame()
        # f1 = MainFrame("Frame One")          # see if can do import from ?’run.py’
        # f2 = OtherFrame("Frame Two")         # so not have to hard code this

        # self.controller.register_frame(mf)
        # self.controller.register_frame(f1)   # ? loop through a list from run.py
        # self.controller.register_frame(f2)

        f0.Show()
        f0.Fit()
        return True

    def FilterEvent(self, event):
        if isinstance(event, wx.KeyEvent):
            if self.hotkeys.handle(event):
                return True
        return super().FilterEvent(event)

    def register_hotkeys(self):
        # Bind global hotkeys
        #self.hotkeys.bind('Ctrl+Shift+K', self.do_something)
        self.hotkeys.bind('Alt+Q', self.controller.hotkey_quit)


        #def FilterEvent(self, event):
            #if is instance(event, wx.KeyEvent):
                #if self.hotkeys.hangel(event):
                    #return True
            #return super().FilterEvent(event)


        #self.controller = Controller()

        f0 = MainFrame()
        #f1 = MainFrame("Frame One")          # see if can do import from ?’run.py’
        #f2 = OtherFrame("Frame Two")         # so not have to hard code this

        #self.controller.register_frame(mf)
        #self.controller.register_frame(f1)   # ? loop through a list from run.py
        #self.controller.register_frame(f2)

        f0.Show()
        f0.Fit()
        #f1.Show()
        #f2.Show()


        return True
