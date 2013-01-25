# This file was automatically generated by pywxrc, do not edit by hand.
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


class xrcFindReplace(wx.Dialog):
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle()."""
        pass

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreDialog()
        self.PreCreate(pre)
        get_resources().LoadOnDialog(pre, parent, "FindReplace")
        self.PostCreate(pre)

        # create attributes for the named items in this container
        self.Find = xrc.XRCCTRL(self, "Find")
        self.Replace_ = xrc.XRCCTRL(self, "Replace_")
        self.Replace = xrc.XRCCTRL(self, "Replace")
        self.Status = xrc.XRCCTRL(self, "Status")
        self.findInCurrent = xrc.XRCCTRL(self, "findInCurrent")
        self.findInProject = xrc.XRCCTRL(self, "findInProject")
        self.findInOpen = xrc.XRCCTRL(self, "findInOpen")
        self.Cancel = xrc.XRCCTRL(self, "Cancel")
        self.OK = xrc.XRCCTRL(self, "OK")



# ------------------------ Resource data ----------------------

def __init_resources():
    global __res
    __res = xrc.EmptyXmlResource()

    wx.FileSystem.AddHandler(wx.MemoryFSHandler())

    FindReplace = '''\
<?xml version="1.0" ?><resource class="wxDialog">
  <object class="wxDialog" name="FindReplace">
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <object class="wxPanel">
          <object class="wxStaticText">
            <pos>10, 15</pos>
            <size>200,20</size>
            <label>Find</label>
          </object>
          <object class="wxTextCtrl" name="Find">
            <XRCED>
              
              
              <events>EVT_TEXT_ENTER</events>
              
              
              <assign_var>1</assign_var>
            </XRCED>
            <pos>10, 40</pos>
            <size>360, 24</size>
          </object>
        </object>
        <flag>wxEXPAND|wxFIXED_MINSIZE</flag>
        <minsize>100, 70</minsize>
      </object>
      <object class="sizeritem">
        <object class="wxPanel">
          <object class="wxStaticText" name="Replace_">
            <label>Replace With</label>
            
            <pos>10, 5</pos>
            <size>380, 20</size>
          </object>
          <object class="wxTextCtrl" name="Replace">
            <pos>10, 40</pos>
            <size>360, 24</size>
          </object>
          <object class="wxStaticText" name="Status">
            <label/>
            <pos>10, 70</pos>
            <size>375, 20</size>
            <style>wxALIGN_RIGHT</style>
          </object>
          <object class="wxRadioButton" name="findInCurrent">
            <label>In Current File</label>
            <value>1</value>
            <pos>10, 95</pos>
          </object>
          <object class="wxRadioButton" name="findInProject">
            <label>In Project</label>
            <value>0</value>
            <pos>10, 120</pos>
          </object>
          <object class="wxRadioButton" name="findInOpen">
            <label>In All Open Files</label>
            <value>0</value>
            <pos>10, 145</pos>
          </object>
        </object>
        <flag>wxEXPAND</flag>
        <minsize>380, 200</minsize>
      </object>
      <object class="sizeritem">
        <object class="wxBoxSizer">
          <object class="spacer">
            <option>1</option>
          </object>
          <object class="sizeritem">
            <object class="wxButton" name="Cancel">
              <label>Cancel</label>
              <XRCED>
                
                
                <events>EVT_BUTTON</events>
                
                
                <assign_var>1</assign_var>
              </XRCED>
            </object>
            <flag>wxFIXED_MINSIZE</flag>
            <minsize>100, 20</minsize>
          </object>
          <object class="spacer">
            <size>10, 40</size>
            <option>0</option>
            <flag>wxRIGHT|wxFIXED_MINSIZE</flag>
          </object>
          <object class="sizeritem">
            <object class="wxButton" name="OK">
              <size>100, 20</size>
              <label>OK</label>
              <default>1</default>
              <XRCED>
                
                
                <events>EVT_BUTTON</events>
                
                
                <assign_var>1</assign_var>
              </XRCED>
            </object>
            <flag>wxFIXED_MINSIZE</flag>
            <minsize>100, 20</minsize>
          </object>
          <orient>wxHORIZONTAL</orient>
          <object class="spacer">
            <size>10, 10</size>
            <flag>wxALIGN_RIGHT|wxFIXED_MINSIZE</flag>
          </object>
        </object>
        <option>0</option>
        <flag>wxEXPAND|wxGROW|wxALIGN_CENTRE_VERTICAL|wxADJUST_MINSIZE|wxFIXED_MINSIZE</flag>
        <border>0</border>
        <minsize>320, 80</minsize>
      </object>
    </object>
    <pos>10,10</pos>
    <size>400, 310</size>
    <title>Replace</title>
    <centered>1</centered>
  </object>
</resource>'''

    wx.MemoryFSHandler.AddFile('XRC/FindReplace/FindReplace', FindReplace)
    __res.Load('memory:XRC/FindReplace/FindReplace')


# ----------------------- Gettext strings ---------------------

def __gettext_strings():
    # This is a dummy function that lists all the strings that are used in
    # the XRC file in the _("a string") format to be recognized by GNU
    # gettext utilities (specificaly the xgettext utility) and the
    # mki18n.py script.  For more information see:
    # http://wiki.wxpython.org/index.cgi/Internationalization 
    
    def _(str): pass
    
    _("Find")
    _("Replace With")
    _("In Current File")
    _("In Project")
    _("In All Open Files")
    _("Cancel")
    _("OK")
    _("Replace")
