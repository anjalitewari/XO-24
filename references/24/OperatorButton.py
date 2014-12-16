from KButton import KButton

class OperatorButton(KButton):
	
	def __init__(self, operator, x, y,w,h, textureID = -1, TexturePressed = -1, textureSize = ()):
		KButton.__init__(self,x,y,w,h,textureID,textureSize)
		self.color = (252,90,90)
		self.operation = operator
		self.tapped = False
		#states
		self.normal = textureID
		self.pressed = TexturePressed
		
	def getOperation(self):
		return self.operation
		
	def setOperation(self, newvalue):
		self.operation = newvalue