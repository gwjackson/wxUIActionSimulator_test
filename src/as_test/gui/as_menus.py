import wx


class File_menu(wx.MenuBar):
    """
    Menus for the as_test.py
    abstarcted out to this module
    parent_frame passed in (here from as_test.py)
    """

    def __init__(self, parent_frame):
        super().__init__()
        self.frame = parent_frame

        # Build individual menus
        self._build_file_menu()
        self._build_macro_menu()
        self._build_help_menu()


    def _build_file_menu(self):
        self.file_menu = wx.Menu()

        # Append top-level menu to MenuBar
        self.Append(self.file_menu, "&File")

    def _build_help_menu(self):
        self.help_menu = wx.Menu()

        # Append to top level
        self.Append(self.help_menu, "&Help")

    def _build_macro_menu(self):
        self.macro_menu = wx.Menu()

        # Append to top-level
        self.Append(self.macro_menu, "&Macro")

