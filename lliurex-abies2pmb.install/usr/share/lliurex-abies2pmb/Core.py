
#!/usr/bin/env python

#import LliurexGoogleDriveManager
#import lliurex.lliurexgdrive
import LliurexAbiesToPmb
import ConvertBox
import abies2pmb



class Core:
	
	singleton=None
	DEBUG=True
	
	@classmethod
	def get_core(self):
		
		if Core.singleton==None:
			Core.singleton=Core()
			Core.singleton.init()

		return Core.singleton
		
	
	def __init__(self,args=None):
		
		self.dprint("Init...")
		
	#def __init__
	
	def init(self):
		
		#self.LliurexAbies2PmbManager=lliurex.lliurexgdrive.LliurexGoogleDriveManager()
		self.dprint("Creating ConvertBox...")
		self.convert_box=ConvertBox.ConvertBox()
		self.abies2pmb=abies2pmb.abies2Pmb()	
		
		
		# Main window must be the last one
		self.dprint("Creating LliurexAbiesToPmb...")
		self.lap=LliurexAbiesToPmb.LliurexAbiesToPmb()
		
		self.lap.load_gui()
		self.lap.start_gui()
		
		
	#def init
	
	
	
	def dprint(self,msg):
		
		if Core.DEBUG:
			
			print("[CORE] %s"%msg)
	
	#def  dprint
