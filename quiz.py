import sys
import os

def quiz():
	file=open("infoquiz.txt", 'w+')
	# language=input("Are you in need of service in another lenguage? (Y/N)")
	gender = input ("Enter gender (M/F/Other): ")
	familymembers = input("Do you have family members with you? (Y/N): ")
	age=input("Are you over 18? (Y/N): ")	
	lgbtq=input("Are you in need of a LGBTQ friendly shelter? (Y/N): ")
	# file.write(language+'\n')
	file.write(gender+'\n')
	file.write(familymembers+'\n')
	file.write(age+'\n')
	file.write(lgbtq+'\n')
	file.close()

def option():
	emergency = input("Is this an emergency?")
	if (emergency=="Y"):
		print("Call 911")
		return False
	else:
		quiz()
		return True

# def main():
# 	option()

# main()