'''
Created on Dec 23, 2013

@author: Chris
'''

import wx

from gooey.gui import imageutil, image_repository
from gooey.gui import styling
from gooey.gui.lang import i18n


PAD_SIZE = 10


class FrameHeader(wx.Panel):
  def __init__(self, heading, subheading, **kwargs):

    wx.Panel.__init__(self, **kwargs)
    self.SetDoubleBuffered(True)
    self._controller = None

    self._header = None
    self._subheader = None
    self._settings_img = None
    self._running_img = None
    self._check_mark = None

    self._init_properties()
    self._init_components(heading, subheading)
    self._init_pages()
    self._do_layout()


  def _init_properties(self):
    self.SetBackgroundColour('#ffffff')
    self.SetSize((30, 90))
    self.SetMinSize((120, 80))

  def _init_components(self, heading, subheading):
    self._header = styling.H1(self, heading)

    self._subheader = wx.StaticText(self, label=subheading)

    self._settings_img = self._load_image(image_repository.settings2, height=79)
    self._running_img = self._load_image(image_repository.computer3, 79)
    self._check_mark = self._load_image(image_repository.alessandro_rei_checkmark, height=75)


  def _do_layout(self):
    vsizer = wx.BoxSizer(wx.VERTICAL)
    sizer = wx.BoxSizer(wx.HORIZONTAL)
    headings_sizer = self.build_heading_sizer()
    sizer.Add(headings_sizer, 1, wx.ALIGN_LEFT | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND | wx.LEFT, PAD_SIZE)
    sizer.Add(self._settings_img, 0, wx.ALIGN_RIGHT | wx.EXPAND | wx.RIGHT, PAD_SIZE)
    sizer.Add(self._running_img, 0, wx.ALIGN_RIGHT | wx.EXPAND | wx.RIGHT, PAD_SIZE)
    sizer.Add(self._check_mark, 0, wx.ALIGN_RIGHT | wx.EXPAND | wx.RIGHT, PAD_SIZE)
    self._running_img.Hide()
    self._check_mark.Hide()
    vsizer.Add(sizer, 1, wx.EXPAND)
    self.SetSizer(vsizer)

  def _load_image(self, img_path, height=70):
    return imageutil.resize_bitmap(self, imageutil._load_image(img_path), height)

  def build_heading_sizer(self):
    sizer = wx.BoxSizer(wx.VERTICAL)
    sizer.AddStretchSpacer(1)
    sizer.Add(self._header, 0)
    sizer.Add(self._subheader, 0)
    sizer.AddStretchSpacer(1)
    return sizer

  def RegisterController(self, controller):
    if self._controller is None:
      self._controller = controller

  def _init_pages(self):

    def PageOne():
      self._header.SetLabel(i18n.translate("running_title"))
      self._subheader.SetLabel(i18n.translate('running_msg'))
      self._check_mark.Hide()
      self._settings_img.Hide()
      self._running_img.Show()
      self.Layout()

    def PageTwo():
      self._header.SetLabel(i18n.translate('finished_title'))
      self._subheader.SetLabel(i18n.translate('finished_msg'))
      self._running_img.Hide()
      self._check_mark.Show()
      self.Layout()

    self._pages = iter([PageOne, PageTwo])

  def NextPage(self):
    try:
      next(self._pages)()
    except:
      self._init_pages()
      next(self._pages)()
