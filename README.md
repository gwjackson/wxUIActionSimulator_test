# wx.UIActionSimulator test prgram

An attempt to learn the UIActionSimulator to creat / record macros

UIAction stuff
https://docs.wxpython.org/wx.UIActionSimulator.html
Accelerator stuff
https://wxpython.org/Phoenix/docs/html/wx.AcceleratorEntry.html
and baried deep in the wx.Window page is the HotKey stuff
https://wxpython.org/Phoenix/docs/html/wx.Window.html#wx.Window.RegisterHotKey

The UIActionSimulatory in the Demo file was just to simplified, though a good place to starte

* Test against various widgets
* Test against dialogs
* Test w/serializing; load / save
* dialog to chose previous saved macros
* effect on screen size / resolution / location
* Still working on project layout and packaging
* and distribution options 

8/5/16Initial commit  ~ 
8/19/26 multiple commits trying to roll my own hotkey system - complete waste of time
8/19/26 used the wxPython Hotkey and Accelerator table much easier.  This is just a
toy program to test the ability to do this, have not gotten yet to the 'macro' part
of the project but it may not even use the UIActionSimulator



Dependencies:
* Python >= 3.13.x
* wxPython >= 4.x.x

License:
MIT 
