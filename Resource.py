class Resource:
	"""A class of service providers including name, location, distance, hours, phone, and 
	target population"""

	def __init__(self, org_name, location, hours, phone, gender, family, age, lgtbq, description):
		self.org_name = org_name
		self.location = location
		self.hours = hours
		self.phone = phone
		self.gender = gender
		self.family = family
		self.age = age
		self.lgtbq = lgtbq
		self.description = description
		
	def get_org_name():
		return self.org_name
	def get_location():
		return self.location
	def get_hours():
		return self.hours
	def get_phone():
		return self.phone
	def get_gender():
		return self.gender
	def get_family():
		return self.family
	def get_age():
		return self.age
	def get_lgtbq():
		return self.lgtbq
	def get_description():
		return self.get_description

	def __str__():
		return ("Organization: " + self.org_name \
			+ "Location" + self.location \
			+ "Hours: " + self.hour \
			+ "Phone: " + self.phone \
			+ "Gender: " + self.gender \
			+ "Family: " + self.family \
			+ "Age: " + self.age \
			+ "LGBTQ: " + self.lgtbq \
			+ "Description: " + self.description)
