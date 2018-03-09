from bs4 import BeautifulSoup
import requests

# CuLearn Login
username = "" # Enter your CuLearn Username here
password = "" # Enter your CuLearn Password here

# CuLearn Course ID's (Found in the CuLearn URL)
# Ex: https://culearn.carleton.ca/moodle/enrol/index.php?id=98008 -> Course ID is 98008, NOT COMP2402B [11060]
# If you have several courses, seperated them by commas, ex: [98008, 12345, 10001]
courses = [98008] #Replace with your courses here

#You don't need to touch anything below here

# URL for your class grades
url = "https://culearn.carleton.ca/moodle/grade/report/user/index.php?id="

# Make a session and login onto CuLearn
s = requests.Session()
data = {'username': username, 'password' : password}
s.post('https://culearn.carleton.ca/moodle/login/index.php', data=data)

# Get URLS of all courses
urls = []

for course in courses:
	urls.append(s.get(url+str(course)))	

# Get the HTML data from all urls
html_data = []

for data in urls:
	html_data.append(BeautifulSoup(data.content, 'html.parser'))

# Store course names
courseNames = []

# Store the grades in here
grades = []

# Store filtered HTML data while extracting the grades/assignment names
filtered = []

counter = 0
for data in html_data:
	# Find the table of grades
	html_data[counter] = data.find("table", {"summary": "The table is arranged as a list of graded items including categories of graded items. When items are in a category they will be indicated as such."})
	counter += 1


counter = 0
for data in html_data:
	# Find course name and add it to the array of names
	courseNames.append(data.find("th", {"class": "level1 levelodd oddd1 b1b b1t column-itemname"}).text)
	filtered.append([data.findAll("tr")])




counter = 0
for data in filtered:
	# Delete first rows since they're not needed
	del filtered[counter][0][0]
	del filtered[counter][0][0]
	counter += 1

counter = 0
for entries in filtered:

	# Create an empty array for each ourse
	grades.append([])

	for data in entries[0]:
		if(data.find("td")):
			# Assignment/Test name - Format it nicely (Remove unnecessary () and white space)
			i_name = data.findAll("th")[0].text.split("(")[0].strip()
			
			# Assignment/test Grade
			i_grade = data.findAll("td")[0].text

			# What the assignment/test is out of
			i_range = data.findAll("td")[1].text.split("–")[1] 

			# Calculate grade percentage if you received the mark
			if(i_grade == "-"):
				i_final = "-"
			else:
				i_final = (float(i_grade) / float(i_range))*100

			# Only add assignment/test marks to the array of grades
			if(not i_name == "Course totalWeighted mean of grades. Include empty grades."):
				# Add each grade entry to the grades array into the grades array
				grades[counter].append([i_name, i_final, i_grade, i_range])

	counter += 1

#Output data in a nicely formatted way
counter = 0
for course in grades:

	print(courseNames[counter])
	
	for entry in course:
		if(entry[1] == "-"):
			print("%20s: %s" % (entry[0], "-"))
		else:
			print("%20s: %2.0f%%\t(%0.1f/%0.1f)" % (entry[0], entry[1], float(entry[2]), float(entry[3])))

	print()

input("")