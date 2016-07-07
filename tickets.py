#!/usr/bin/python
#RT Ticket Creator
from rtkit.resource import RTResource
from rtkit.authenticators import CookieAuthenticator
from rtkit.errors import RTResourceError
from rtkit import set_logging
import logging
set_logging('debug')
logger = logging.getLogger('rtkit')
import csv
resource = RTResource('http://localhost/REST/1.0/', 'username', 'passwoed', CookieAuthenticator)
with open('tickets.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
	content = {
        	'content': {
                	'Queue': ('%s' % row[0]),
                	'Subject': ('%s' % row[1]),
                	'Text': ('%s' % row[2]),
                	'Cc': ('%s' % row[3]),
                	'AdminCc' : ('%s' % row[4]), 
                        'Owner': ('%s' % row[5]),
                	'Starts': ('%s' % row[6]),
                	'Due':  ('%s' % row[7]), 
        	}
	}

	try:
		response = resource.post(path='ticket/new', payload=content,)
		logger.info(response.parsed)
	except RTResourceError as e:
		logger.error(e.response.status_int)
		logger.error(e.response.status)
		logger.error(e.response.parsed)



