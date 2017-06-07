import sqlite3
#from courses.models import Course
from home.course import Course

class Algorithm():

############################################
############ INITIALIZATION ################
############################################
	def __init__(self, user, majorelec):
	
		self.major = "" #The Major of the Student
		self.conc = "" #The Concentration of the Major of the Student
		self.majorelec = majorelec #List of Major Elective Passed To Algorithm
		self.start = 0 #Starting Quarter (0 (Fall), 1 (Winter), 2 (Spring), 3 (Summer))
		self.rate = 0 #How Many Classes the Student Wishes to Take
		self.summer = "" #Does the Student Wish to take Summer Classes ("no", "yes")
		self.paths = [] #List of the Paths
		
		conn = sqlite3.connect('db.sqlite3')
		c = conn.cursor()
		data = c.execute('SELECT * FROM accounts_student')
		for row in data:
			if row[6] == user:
				self.major = row[1]
				self.conc = row[2]
				self.starting = row[3]
				self.rate = row[4]
				self.summer = row[5].lower()
	
############################################
############ REFILL METHOD #################
############################################

	def refill(self, intro, foundation, advanced, majorelec, capstone):
		course_needed = []
		
		#Grabbing All Possible Classes from Computer Science Database
		if self.major == "Computer Science":
			conn = sqlite3.connect('db.sqlite3')
			c = conn.cursor()
			data = c.execute('SELECT * FROM courses_course')
			csc_classes = []
			for row in data:
				csc_classes.append((row[1],row[3].split(" and "),[row[5],row[9],row[7],row[8]]))
	
		#Grabbing All Possible Classes from Information Systems Database
		elif self.major == "Information Systems":
			conn = sqlite3.connect('db.sqlite3')
			c = conn.cursor()
			data = c.execute('SELECT * FROM courses_is_course')
			is_classes = []
			for row in data:
				is_classes.append((row[1],row[3].split(" and "),[row[5],row[9],row[7],row[8]]))

		#Appending Intro Classes
		for clazz in intro:
			if self.major == "Computer Science":
				for classs in csc_classes:
					if clazz == classs[0]:
						course_needed.append(Course(classs[0], classs[1], classs[2]))
						break
			else:
				for classs in is_classes:
					if clazz == classs[0]:
						course_needed.append(Course(classs[0], classs[1], classs[2]))
						break
		
		#Appending Foundation Classes
		for clazz in foundation:
			if self.major == "Computer Science":
				for classs in csc_classes:
					if clazz == classs[0]:
						course_needed.append(Course(classs[0], classs[1], classs[2]))
						break
			else:
				for classs in is_classes:
					if clazz == classs[0]:
						course_needed.append(Course(classs[0], classs[1], classs[2]))
						break
						
		#Appending Advanced Classes
		for clazz in advanced:
			if self.major == "Computer Science":
				for classs in csc_classes:
					if clazz == classs[0]:
						course_needed.append(Course(classs[0], classs[1], classs[2]))
						break
			else:
				for classs in is_classes:
					if clazz == classs[0]:
						course_needed.append(Course(classs[0], classs[1], classs[2]))
						break
						
		#Appending Major Electives
		for clazz in majorelec:
			if self.major == "Computer Science":
				for classs in csc_classes:
					if clazz == classs[0]:
						course_needed.append(Course(classs[0], classs[1], classs[2]))
						break
			else:
				for classs in is_classes:
					if clazz == classs[0]:
						course_needed.append(Course(classs[0], classs[1], classs[2]))
						break
						
		#Appending Capstone Classes
		for clazz in capstone:
			if self.major == "Computer Science":
				for classs in csc_classes:
					if clazz == classs[0]:
						course_needed.append(Course(classs[0], classs[1], classs[2]))
						break
			else:
				for classs in is_classes:
					if clazz == classs[0]:
						course_needed.append(Course(classs[0], classs[1], classs[2]))
						break
					
		return course_needed
	
############################################
############ ALGORITHM  ####################
############################################

	def algorithm(self, course_needed, numcourses, elective, season, iteration):
		counter = 1
		current_season = int(season)
		truenum = numcourses
		i = iteration
		completed = []
		path = []
		year = 1
	
		while len(course_needed) != 0:
			current_quarter = []
			current_season = current_season % 4
			if current_season == 0:
				if counter != 1:
					year = year + 1
			if current_season == 1 and i == 3:
				numcourses = 1
			elif i ==3:
				numcourses = truenum
			if current_season == 3 and self.summer == "no":
				current_season = (current_season + 1) % 4
				year = year + 1
			for course in course_needed:
				coursename = course.getName()
				courseprereq = course.getPreReq()
				courseava = course.getAva()	
				or_prereqs = [] #Only 1 Required
				and_prereqs = [] #The Required
				
				for prereq in courseprereq:
					if "or" in prereq:
						or_prereqs = prereq.split(" or ")
					else:
						and_prereqs.append(prereq)
				
				if courseava[current_season] == 1:
					try:
						if courseprereq == ['None'] and len(current_quarter) < int(numcourses):
							current_quarter.append(course)
						elif not set(and_prereqs).issubset(completed):
							raise StopIteration
						elif len(current_quarter) < int(numcourses):
							if or_prereqs == []:
								current_quarter.append(course)
							else:
								for prereq in or_prereqs:
									prereq = [prereq]
									if set(prereq).issubset(completed):
										current_quarter.append(course)
					except StopIteration: pass
		
			while len(current_quarter) < int(numcourses) and len(elective) != 0:
				elect = elective.pop()
				current_quarter.append(Course(elect[0],elect[1],[1,1,1,1]))
		
			#if current_season == 0:
				#print("For Year " + str(year) + " Fall Quarter, you will be taking: ")
			#elif current_season == 1:
				#print("For Year " + str(year) + " Winter Quarter, you will be taking: ")
			#elif current_season == 2:
				#print("For Year " + str(year) + " Spring Quarter, you will be taking: ")
			#elif current_season == 3:
				#print("For Year " + str(year) + " Summer Quarter, you will be taking: ")
			
			temp = []
			for course in current_quarter:
				coursename = course.getName()
				#print(coursename)
				temp.append(coursename)
				completed.append(coursename)
				if coursename == 'Elective1' or coursename == 'Elective2':
					pass
				else:
					course_needed.remove(course)
			path.append(temp)
			counter = counter + 1
			current_season = current_season + 1
	
		while len(elective) != 0:
			current_quarter = []

			while len(elective) != 0 and len(current_quarter) < int(numcourses):
				elect = elective.pop()
				current_quarter.append(Course(elect[0],elect[1],[1,1,1,1]))
	
			#if current_season == 0:
				#print("For Year " + str(year) + " Fall Quarter, you will be taking: ")
			#elif current_season == 1:
				#print("For Year " + str(year) + " Winter Quarter, you will be taking: ")
			#elif current_season == 2:
				#print("For Year " + str(year) + " Spring Quarter, you will be taking: ")
			if current_season == 3 and self.summer == "no":
				year = year + 1
				#print("For Year " + str(year) + " Fall Quarter, you will be taking: ")
			#else:
				#print("For Year " + str(year) + " Summer Quarter, you will be taking: ")
			temp = []
			for course in current_quarter:
				#print(course.getName())
				temp.append(course.getName())
			path.append(temp)
			counter = counter + 1
			current_season = (current_season + 1) % 4
			
		return path
			
############################################
############ RUN METHOD  ###################
############################################

	def run(self):
		cscintro = []
		cscfoundation = []
		cscadvanced = []
		cscmajorelec = []
		csccapstone = [] #Computer Science Has No Capstone
		
		isintro = []
		isfoundation = []
		isadvanced = []
		ismajorelec = []
		iscapstone = [('IS 577')] #Information Systems Has One Capstone

		#Setup for Computer Science
		if(self.major == "Computer Science"):
			cscintro = [('CSC 400'), ('CSC 401'), ('CSC 402'), ('CSC 403'), ('CSC 406'), ('CSC 407')]
			cscfoundation = [('CSC 421'), ('CSC 435'), ('CSC 447'), ('CSC 453'), ('SE 450')]
			cscadvanced = []
			cscmajorelec = self.majorelec
	
		#Setup for Information Systems
		if(self.major == "Information Systems"):
			if self.conc == "Business Analysis":
				isintro = []
				isfoundation = [('IS 421'),('CSC 451'),('IS 422'),('IS 430')]
				isadvanced = [('CNS 440'),('IS 435'),('IS 485'),('IS 535'),('IS 560')]
				ismajorelec = self.majorelec
			elif self.conc == "Business Intelligence":
				isintro = [('IT 411'), ('IT 403')]
				isfoundation = [('IS 421'),('CSC 451'),('IS 422'),('IS 430')]
				isadvanced = [('IS 574'),('CSC 423'),('IS 467'),('IS 549')]
				ismajorelec = self.majorelec
			elif self.conc == "Database Administration":
				isintro = [('IT 411')]
				isfoundation = [('IS 421'),('CSC 451'),('IS 422'),('IS 430')]
				isadvanced = [('IS 549'),('CSC 454'),('CSC 452'),('CSC 554')]
				ismajorelec = self.majorelec
			elif self.conc == "IT Enterprise Management":
				isintro = []
				isfoundation = [('IS 421'),('CSC 451'),('IS 422'),('IS 430')]
				isadvanced = [('ECT 424'),('IS 556'),('IS 570'),('IS 535')]
				ismajorelec = self.majorelec
			else: #Standard Concentration
				isintro = []
				isfoundation = [('IS 421'),('CSC 451'),('IS 422'),('IS 430')]
				isadvanced = []
				ismajorelec = self.majorelec
		i = 1

		#While All Three Routes Haven't Been Done (1 = Longest Route, 2 = Shortest Route, 3 = Work Friendly Route)
		while(i != 4):
	
			#Setup For Longest Route
			if i == 1:
				#print("Longest Route to Graduation")
				numcourses = 1
		
				if self.major == "Computer Science":
					course_needed = self.refill(cscintro, cscfoundation, cscadvanced, cscmajorelec, csccapstone)
					elective = [('Elective2','None'),('Elective1','None')]
			
				elif(self.major == "Information Systems"):
					course_needed = self.refill(isintro, isfoundation, isadvanced, ismajorelec, iscapstone)
					elective = [('Elective1',['None'])]
			
				self.paths.append(self.algorithm(course_needed, numcourses, elective, self.start, i))
				i = i + 1
			
			#Setup For Shortest Route
			elif i == 2:
				#print("Shortest Route based on Input")
		
				if self.major == "Computer Science":
					course_needed = self.refill(cscintro, cscfoundation, cscadvanced, cscmajorelec, csccapstone)
					elective = [('Elective2','None'),('Elective1','None')]
			
				elif self.major == "Information Systems":
					course_needed = self.refill(isintro, isfoundation, isadvanced, ismajorelec, iscapstone)
					elective = [('Elective1','None')]
			
				self.paths.append(self.algorithm(course_needed, self.rate, elective, self.start, i))
				i = i + 1
			
			#Setup For Work Friendly Route
			else:
				#print("Work Friendly Route")
		
				if self.major == "Computer Science":
					course_needed = self.refill(cscintro, cscfoundation, cscadvanced, cscmajorelec, csccapstone)
					elective = [('Elective2','None'),('Elective1','None')]
			
				elif self.major == "Information Systems":
					course_needed = self.refill(isintro, isfoundation, isadvanced, ismajorelec, iscapstone)
					elective = [('Elective1','None')]
		
				self.paths.append(self.algorithm(course_needed, self.rate, elective, self.start, i))
				i = i + 1
		
		return self.paths