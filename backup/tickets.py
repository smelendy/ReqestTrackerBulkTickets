#!/usr/bin/python
#RT Ticket Creator by smelendy@umw v0.3
from rtkit.resource import RTResource
from rtkit.authenticators import CookieAuthenticator
from rtkit.errors import RTResourceError
from rtkit import set_logging
import logging
import csv
import getpass
set_logging('debug')
logger = logging.getLogger('rtkit')
filecsv = raw_input("Please enter name of CSV file: ")
user = getpass.getuser()
passwd = getpass.getpass()
resource = RTResource('http://localhost/REST/1.0/', user , passwd , CookieAuthenticator)
with open(filecsv) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
	content = {
        	'content': {
                	'Queue': ('%s' % row[0]),
                	'Subject': ('%s' % row[1]),
                	'Text': ('%s' % row[2]),
			'Requestors': ('%s' % row[3]),
                	'Cc': ('%s' % row[4]),
                	'AdminCc' : ('%s' % row[5]), 
                        'Owner': ('%s' % row[6]),
                	'Starts': ('%s' % row[7]),
                	'Due': ('%s' % row[8]), 
			'CF.{Jira}': ('%s' % row[9]),
        	}
	}

	try:
		response = resource.post(path='ticket/new', payload=content,)
		logger.info(response.parsed)
	except RTResourceError as e:
		logger.error(e.response.status_int)
	 	logger.error(e.response.status)
		logger.error(e.response.parsed)
