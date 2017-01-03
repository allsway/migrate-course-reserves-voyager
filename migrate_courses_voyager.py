#!/usr/bin/python
import requests
import sys
import csv
import configparser
import logging
import collections
import datetime
import json
import xml.etree.ElementTree as ET

# Returns the API key
def get_key():
	return config.get('Params', 'apikey')

# Returns the Alma API base URL
def get_base_url():
	return config.get('Params', 'baseurl')

# Returns the base SRU URL	
def get_sru_url():
	return config.get('Params','sruurl')
	
# Returns the course file with the course details
def get_course_file():
	return config.get('Data', 'course_details')

# Returns the default end date for courses
def get_default_end_date():
	return config.get('Params', 'enddate')

# Returns the default begin date for courses
def get_default_begin_date():
	return config.get('Params', 'begindate')

def get_processing_dept():
	return config.get('Params', 'processing_dept')

# fix from format 6/24/02 to YYYY-MM-DD
def normalize_date(date):
	new_date = datetime.datetime.strptime(date, "%m/%d/%y")
	return new_date.strftime('%Y-%m-%d')
	


"""
	
"""
def parse_course_details(row):
	course_code = row[3] + row[1]
	course_code = course_code.strip(' ')
	course_name = row[3] + " " + row[1]
	if row[5] is not None:
		begin_date = row[5]
	else:
		begin_date = get_default_begin_date()
	if row[6] is not None:
		end_date = normalize_date(row[6])
	else:
		end_date = get_default_end_date()
	data = {}
	data['code'] = course_code
	data['name'] = course_name
	data['academic_department'] = {'value' : ''}
	data['processing_department'] = {'value' : get_processing_dept()}
	data['status'] = 'ACTIVE'
	data['start_date'] = begin_date
	data['end_date'] = end_date
	json_data = json.dumps(data)
	print (json_data)
	
	
"""
	Reads in the course details 
"""
def read_courses(course_file):
	f = open(course_file, 'rt')
	try:
		reader = csv.reader(f)
		next(reader)
		for row in reader:
			parse_course_details(row)
	finally:
		f.close()

	
"""
	Creates a course record through the Alma API
"""	
def create_course(course_row):
	print("create course")
	
"""
	Creates a course reading list in Alma, based on the course identifier
"""	
def create_reading_list(course_id):
	print ("create reading list")

"""
	Create a citation based on the barcode of an associated item
"""
def create_barcode_citation(barcode):
	print ("create citation based on barcode")


"""
	Create a citation based on the former system record number (uses SRU)
"""	
def create_citation(other_id):
	print ("create citation based on former system bib record number")



				
logging.basicConfig(filename='status.log',level=logging.DEBUG)	
			
config = configparser.ConfigParser()
config.read(sys.argv[1])

courses = sys.argv[2]
read_courses(courses)












