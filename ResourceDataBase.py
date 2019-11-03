import sqlite3 
import Resource
import quiz

conn = sqlite3.connect("resources.db") # use filename as db # encrypted
										# creates sql object and saves it as variable named conn
curse = conn.cursor() # create cursor to execute sql command

def createdb():
	curse.execute("""CREATE TABLE resources (
		org_name text,
		location text,
		hours text,
		phone text,
		gender text,
		family int,
		age int,
		lgtbq int,
		description text)""")

def add_from_file(filename):
	infile = open(filename, "r")
	text = infile.read().split("\n")
	for f in range(len(text)):
		provider_data = text[f].split(",")
		org_name1 = provider_data[0].strip()
		location1 = provider_data[1].strip()
		hours1 = provider_data[2].strip()
		phone1 = provider_data[3].strip()
		gender1 = provider_data[4].strip()
		family1 = int(provider_data[5].strip())
		age1 = int(provider_data[6].strip())
		lgtbq1 = int(provider_data[7].strip())
		description1 = provider_data[8].strip()
		# resource = Resource(org_name1, location1, hours1, phone1, gender1, family1, age1, lgtbq1, description1)
		# resources_list.append(resource)
		entities = (org_name1, location1, hours1, phone1, gender1, family1, age1, lgtbq1, description1)
		curse.execute("INSERT INTO resources VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", entities)
		conn.commit()
	infile.close()

def getQuizResults():
	file = open("infoquiz.txt", "r")
	answers = file.read().split()
	file.close()
	return answers

def query_db(): 
	quizResults = getQuizResults()
	gender = quizResults[0].upper()
	fam = quizResults[1].upper()
	age = quizResults[2].upper()
	lgtbq = quizResults[3].upper()
	fam_q, age_q, lgtbq_q = 2, 2, 2
	if fam == 'Y':
		fam_q = 1
	else:
		fam_q = 0
	if age == 'Y':
		age_q = 1
	else:
		age_q = 0
	if lgtbq == 'Y':
		lgtbq_q = 1
	else:
		lgtbq_q = 0
	entities = (gender, fam_q, age_q, lgtbq_q)
	curse.execute("SELECT * FROM resources WHERE gender=? OR gender='MF' AND family=? AND age=? AND lgtbq=?", entities)
	
	search_results = curse.fetchall()
	return search_results

def main():
	# createdb()
	# add_from_file("service_providers.txt")
	if (quiz.option()): 
		search_results = query_db()
		print("\nSearch results: \n")
		for n in range(len(search_results)):
			print(search_results[n][0])
			print("Address: " + search_results[n][1]) 
			print("Hours: " + search_results[n][2])
			print("Phone number: " + search_results[n][3])
			print("Description: " + search_results[n][8])
			print("\n")

main()
conn.close()