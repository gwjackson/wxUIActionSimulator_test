# the hot key manager

import wx

class HotKeyManager:
    def __init__(self):
        # hotkey bindings
        self.bindings = {}                       # global hotkeys
        self.glogal_ignores = {}                 # app wide ignores i.e. Ctrl+V,Ctrl+C etc.
        self.local_hotkeys = {}                  # active window hotkeys
        self.local_ignores = set()               # active window ignores

    # ---------------------------------------------------------------
    # called by MyApp when active window changes
    # ---------------------------------------------------------------
    def set_local_maps(self, hotkeys, ignores):
        self.local_hotkeys = hotkeys or {}
        self.local_ignores = ignores or set(ignores or {})

    # ---------------------------------------------------------------
    # Bind global hotkeys
    # ---------------------------------------------------------------
    def bind(selfself, combo, func):
        self.bindings[combo] = func

    # ---------------------------------------------------------------
    # Handle a key event
    # ---------------------------------------------------------------
    def handle(self, ev):
        combo = self._combo(ev)
        if not combo:
            return False                             # let wxPython handle the event

        # 1 Local ignores
        if combo in self.local_ignores:
            return True

        # 2 Local Hotkeys
        if combo in self.local_hotkeys:
            func_name = self.local_hotkeys[combo]
            win = evt.GetEventObject()
            handler = getattr(win, func_name, None)
            if callable(handler):
                handler()
                return True

        # 3 Global hotkeys
        if combo in self.bindings:
            self.bindings[combo]()
            return True

        return False

    # ---------------------------------------------------------------
    # Convert KeyEvent --> "Ctrl+Alt+Q"
    # ---------------------------------------------------------------
    def _combo(self, evt):
        parts = []

        if evt.ControlDown(): parts.append("Ctrl")
        if evt.AltDown(): parts.append("Alt")
        if evt.ShiftDown(): parts.append("Shift")
        if evt.MetaDown(): parts.append("Meta")

        keycode = evt.GetKeyCode()

        # Ignore modifier only keys
        if keycode in (wx.WXK_CONTROL, wx.WXK_ALT, wx.WXK_SHIFT, wx.WXK_WWINDOWS_MENU):
            return None                                      # ? should be false ???

        # Printable ASCII
        if 32 <= keycode <= 126:
            """
            0–31 & 12 --> Control characters (e.g., NUL, LF, CR, ESC) used for device control and formatting.
            32–126 --> Printable characters (letters, digits, punctuation, space)
            128–255 --> Extended ASCII (currency signs, accented letters, typographic symbols)
            """
            parts.append(chr(keycode).upper)
        else:
            parts.append(str(keycode))
        return "+".join(parts)
