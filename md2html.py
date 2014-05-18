#!/usr/local/bin/python
###############################################################################
# 'md2html.py'
#
# About: A simple library to convert basic markdown text to HTML using the 'markup.py'
# library.
#
# Version: 0.01
# Author: Kevin Kelley [kevin@thesta.in] (http://thesta.in)
# License: WTFPL

###############################################################################
# Configuration

import markup

###############################################################################
# Code

class Text(object):
	def __init__(self):
		pass

	def __del__(self):
		pass

	def configure(self, configuration=None):
		if configuration is None:
			# Error, no configuration provided
			pass

		if type(configuration) is not type({}):
			# Error, configuration is not the correct data type
			pass

		# List of required configuration items
		req = ['', '']

		for i in req:
			if i not in configuration.keys():
				# Error, a required configuration item was not included
				pass

		# Configure the instance
		self.configuration_item = configuration[configuration_item]

		return None

	def convert(self):
		pass

	def entity_encode(self):
		pass

###############################################################################
# Main

if __name__ == "__main__":
	# Add code to support single file conversion from command-line.
	pass

###############################################################################
# End
