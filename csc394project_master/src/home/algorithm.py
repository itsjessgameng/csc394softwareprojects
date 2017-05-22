# import sys

# class Simulation():
# 	def __init__(self, name, prereq):
# 		self.name = name
# 		self.prereq = prereq
		
# 	def getName(self):
# 		return self.name
		
# 	def getPreReq(self):
# 		return self.prereq
		
# intro = [('CSC400',''), ('CSC401',''), ('CSC402','CSC401'), ('CSC403', 'CSC402'), ('CSC406','CSC401,CSC402'), ('CSC407','CSC406')]
# foundation = [('CSC421','CSC400,CSC403'), ('CSC435','CSC403,CSC407'), ('CSC447','CSC403,CSC406'), ('CSC453','CSC403'), ('SE450','CSC403')]
# majorelec = [('CSC448', 'CSC447'), ('CSC475', 'CSC407'), ('CSC551', 'CSC435,CSC453'), ('SE525', 'CSC435,SE450'), ('CSC548', 'CSC448'), ('CSC461', 'CSC400,CSC406,CSC403')]
# elective = [('Elective2',''),('Elective1','')]

# while len(majorelec) < 6:
# 	print("Give course Name: ")
# 	course = sys.stdin.readline()
# 	print("Give course PreReqs: ")
# 	prereq = sys.stdin.readline()
# 	majorelec.append((course, prereq))
	
# print("Give Desired Number of Courses Per Quarter: ")
# numcourses = sys.stdin.readline()

# course_needed = []

# for clazz in intro:
# 	course_needed.append(Simulation(clazz[0],clazz[1]))
	
# for clazz in foundation:
# 	course_needed.append(Simulation(clazz[0],clazz[1]))
	
# for clazz in majorelec:
# 	course_needed.append(Simulation(clazz[0],clazz[1]))
	
# completed = []
# counter = 1
# plan = []
# qurater_count = []

# while len(course_needed) != 0:
# 	current_quarter = []
# 	for course in course_needed:
# 		coursename = course.getName()
# 		courseprereq = course.getPreReq().split(",")
# 		try:
# 			if courseprereq == [''] and len(current_quarter) < int(numcourses):
# 				current_quarter.append(course)
# 			elif not set(courseprereq).issubset(completed):
# 				raise StopIteration
# 			elif len(current_quarter) < int(numcourses):
# 				current_quarter.append(course)
# 		except StopIteration: pass
		
# 	while len(current_quarter) < int(numcourses) and len(elective) != 0:
# 		elect = elective.pop()
# 		current_quarter.append(Simulation(elect[0],elect[1]))
		
# 	print("For Quarter " + str(counter) + ", you will be taking: ")
# 	for course in current_quarter:
# 		coursename = course.getName()
# 		print(coursename)
# 		completed.append(coursename)
# 		if coursename == 'Elective1' or coursename == 'Elective2':
# 			pass
# 		else:
# 			course_needed.remove(course)
# 	counter = counter + 1

# if len(elective) != 0:
# 	current_quarter = []

# 	while len(elective) != 0:
# 		elect = elective.pop()
# 		current_quarter.append(Simulation(elect[0],elect[1]))
	
# 	print("For Quarter " + str(counter) + ", you will be taking: ")
	
# 	for course in current_quarter:
# 		print(course.getName())
# 		plan.append(course.getName)
	# return plan 

	

	