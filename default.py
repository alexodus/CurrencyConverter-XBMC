# -*- coding: utf-8 -*-
# Copyright (c) 2012 Alessandro Rossi

import xbmc, xbmcgui
 
#get actioncodes from keymap.xml
ACTION_PREVIOUS_MENU = 10
 
class MyClass(xbmcgui.Window):
  def onAction(self, action):
    if action == ACTION_PREVIOUS_MENU:
      self.close()
mydisplay = MyClass()
mydisplay .doModal()
del mydisplay