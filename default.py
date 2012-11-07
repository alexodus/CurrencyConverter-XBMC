# -*- coding: utf-8 -*-
# Copyright (c) 2012 Alessandro Rossi

import xbmc, xbmcgui

import urllib2
from xml.dom.minidom import parse, parseString
#get actioncodes from keymap.xml
ACTION_PREVIOUS_MENU = 10
 
class MyClass(xbmcgui.Window):
  def __init__(self):
    self.strActionInfo = xbmcgui.ControlLabel(250, 80, 200, 200, '', 'font14', '0xFFBBBBFF')
    self.addControl(self.strActionInfo)
    self.strActionInfo.setLabel('Push BACK to quit')
    u1 = urllib2.urlopen('http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml')
    dom = parse(u1)
    lista = [{'currency' : elem.attributes['currency'].value, 'rate' : elem.attributes['rate'].value,} for elem in dom.getElementsByTagName('Cube') if elem.hasAttribute('currency')]
    self.list = xbmcgui.ControlList(200, 100, 300, 400)
    self.addControl(self.list)
    for item in lista:
        self.list.addItem(item['currency'] + " = " + item['rate'])
    self.setFocus(self.list)
 
  def onAction(self, action):
    if action == ACTION_PREVIOUS_MENU:
      self.close()
 
  def onControl(self, control):
    if control == self.list:
      item = self.list.getSelectedItem()
      self.message('You selected : ' + item.getLabel())  
 
  def message(self, message):
    dialog = xbmcgui.Dialog()
    dialog.ok(" My message title", message)
 
mydisplay = MyClass()
mydisplay.doModal()
del mydisplay