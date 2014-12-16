from KButton import KButton

class GameButton(KButton):
	
	def __init__(self, value, x, y,w,h, textureID = -1, textureSize = ()):
		KButton.__init__(self,x,y,w,h,textureID,textureSize)
		self.color = (252,90,90)
		self.value = value
		self.on = True;
	
	def getValue(self):
		return self.value
		
	def setValue(self, newvalue):
		self.value = newvalue
		
	def toggle(self, toggle):
		self.on = toggle
		
	def isAvailable(self):
		return self.on