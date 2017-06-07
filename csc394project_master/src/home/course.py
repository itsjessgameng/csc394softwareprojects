#Course class used to define and store a course and its information
class Course():
	def __init__(self, name, prereq, ava):
		self.name = name
		self.prereq = prereq
		self.ava = ava
		
	def getName(self):
		return self.name
		
	def getPreReq(self):
		return self.prereq
		
	def getAva(self):
		return self.ava