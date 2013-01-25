# This file was automatically generated by pywxrc.
# -*- coding: UTF-8 -*-

import wx
import wx.xrc as xrc

__res = None

def get_resources():
    """ This function provides access to the XML resources in this module."""
    global __res
    if __res == None:
        __init_resources()
    return __res




class xrcManageLinked(wx.Dialog):
#!XRCED:begin-block:xrcManageLinked.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass
        
#!XRCED:end-block:xrcManageLinked.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreDialog()
        self.PreCreate(pre)
        get_resources().LoadOnDialog(pre, parent, "ManageLinked")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers

        self.theList = xrc.XRCCTRL(self, "theList")
        self.Cancel = xrc.XRCCTRL(self, "Cancel")
        self.Unlink = xrc.XRCCTRL(self, "Unlink")            


# ------------------------ Resource data ----------------------

def __init_resources():
    global __res
    __res = xrc.EmptyXmlResource()

    wx.FileSystem.AddHandler(wx.MemoryFSHandler())

    manageLinkedProjects_xrc = '''\
<?xml version="1.0" ?><resource class="wxDialog">
  <object class="wxDialog" name="ManageLinked">
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <object class="wxPanel">
              <object class="wxStaticBitmap">
                <bitmap stock_id="wxART_INFORMATION"/>
                <pos>10, 0</pos>
              </object>
              <object class="wxStaticText" name="Label1">
                <label>Manage linked projects:</label>
                <pos>48, 5</pos>
                <size>400, 30</size>
              </object>
            </object>
          </object>
          <object class="sizeritem">
            <object class="wxListBox" name="theList">
              <pos>0,0</pos>
              <size>320, 240</size>
              <style>wxSIMPLE_BORDER|wxFULL_REPAINT_ON_RESIZE</style>
            </object>
            <option>1</option>
            <flag>wxGROW</flag>
            <border>0</border>
            <minsize>322, 200</minsize>
          </object>
        </object>
        <option>1</option>
        <flag>wxGROW</flag>
      </object>
      <object class="sizeritem">
        <object class="wxPanel">
          <object class="wxButton" name="Unlink">
            <label>Unlink</label>
            <default>0</default>
            <pos>540, 0</pos>
            <size>80, 30</size>
          </object>
          <object class="wxButton" name="Cancel">
            <label>Close</label>
            <default>1</default>
            <pos>450, 0</pos>
            <size>80, 30</size>
          </object>
        </object>
        <option>0</option>
        <flag>wxEXPAND</flag>
        <minsize>640, 40</minsize>
      </object>
    </object>
    <pos>0,0</pos>
    <size>640, 320</size>
    <title>Manage Linked Projects</title>
    <centered>1</centered>
  </object>
</resource>'''

    wx.MemoryFSHandler.AddFile('XRC/manageLinkedProjects/manageLinkedProjects_xrc', manageLinkedProjects_xrc)
    __res.Load('memory:XRC/manageLinkedProjects/manageLinkedProjects_xrc')


# ----------------------- Gettext strings ---------------------

def __gettext_strings():
    # This is a dummy function that lists all the strings that are used in
    # the XRC file in the _("a string") format to be recognized by GNU
    # gettext utilities (specificaly the xgettext utility) and the
    # mki18n.py script.  For more information see:
    # http://wiki.wxpython.org/index.cgi/Internationalization 
    
    def _(str): pass
    
    _("Manage linked projects:")
    _("Unlink")
    _("Close")
    _("Manage Linked Projects")
