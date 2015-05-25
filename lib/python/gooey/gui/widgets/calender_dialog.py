__author__ = 'Chris'

import wx
from gooey.gui import styling


class CalendarDlg(wx.Dialog):
  def __init__(self, parent):
    wx.Dialog.__init__(self, parent)

    self.SetBackgroundColour('#ffffff')

    self.ok_button = wx.Button(self, label='Ok')
    self.datepicker = wx.DatePickerCtrl(self, style=wx.DP_DROPDOWN)

    vertical_container = wx.BoxSizer(wx.VERTICAL)
    vertical_container.AddSpacer(10)
    vertical_container.Add(styling.H1(self, label='Select a Date'), 0, wx.LEFT | wx.RIGHT, 15)
    vertical_container.AddSpacer(10)
    vertical_container.Add(self.datepicker, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 15)

    vertical_container.AddSpacer(10)
    button_sizer = wx.BoxSizer(wx.HORIZONTAL)
    button_sizer.AddStretchSpacer(1)
    button_sizer.Add(self.ok_button, 0)

    vertical_container.Add(button_sizer, 0, wx.LEFT | wx.RIGHT, 15)
    vertical_container.AddSpacer(20)
    self.SetSizerAndFit(vertical_container)

    self.Bind(wx.EVT_BUTTON, self.OnOkButton, self.ok_button)

  def OnOkButton(self, event):
    self.Close()
    return wx.ID_OK

  def OnCancellButton(self, event):
    try:
      return None
    except:
      self.Close()

  def GetPath(self):
    return str(self.datepicker.GetValue()).split(' ')[0]
