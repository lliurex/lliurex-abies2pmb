#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Pango, GdkPixbuf, Gdk, Gio, GObject,GLib



import signal
import os
import sys
import Core


signal.signal(signal.SIGINT, signal.SIG_DFL)


RSRC="/usr/share/lliurex-abies2pmb/"
CSS_FILE=RSRC + "lliurex-abiestopmb.css"


class LliurexAbiesToPmb:
	
	def __init__(self):

		self.core=Core.Core.get_core()
		

	#def init

	def load_gui(self):
		
		builder=Gtk.Builder()
		ui_path=RSRC + "rsrc/lliurex-abies-to-pmb.ui"
		builder.add_from_file(ui_path)
		
		
		self.main_window=builder.get_object("main_window")
		self.main_window.set_title("LliureX Abies2Pmb")
		self.main_box=builder.get_object("main_box")
		self.help_button=builder.get_object("help_button")
		
		self.convert_box=self.core.convert_box
		self.main_box.add(self.convert_box)
		
		
		# Add components
			
		self.set_css_info()
		self.connect_signals()
		
		self.main_window.show_all()
		
	#def load_gui


	def set_css_info(self):
		
		
		self.style_provider=Gtk.CssProvider()
		f=Gio.File.new_for_path(CSS_FILE)
		self.style_provider.load_from_file(f)
		Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(),self.style_provider,Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
		self.main_window.set_name("WINDOW")
						
	#def set_css_info					
			
	def connect_signals(self):
		
		self.main_window.connect("destroy",self.quit)
		self.help_button.connect("clicked",self.show_help)
			
	#def connect_signals

	def show_help(self,widget):

		lang=os.environ["LANG"]

		if 'ca_ES' in lang:
			cmd=("xdg-open http://wiki.lliurex.net/tiki-index.php?page=Migració+d\\'Abies+a+PMB")
		else:
			cmd=("xdg-open http://wiki.lliurex.net/tiki-index.php?page=Migración+de+Abies+a+Pmb")

		os.system(cmd)

	#def show_help	

	def quit(self,widget):

		Gtk.main_quit()	
	
	#def quit

	def start_gui(self):
		
		GObject.threads_init()
		Gtk.main()
		
	#def start_gui


	
#class LliurexAbiesToPmb


if __name__=="__main__":
	
	lap=LliurexAbiesToPmb()
	lap.start_gui()
	
