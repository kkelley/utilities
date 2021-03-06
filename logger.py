#!/usr/local/bin/python
###############################################################################
# 'logger.py'
#
# About:
#
# Version: 0.01
# Author: Kevin Kelley [kevin@thesta.in] (http://thesta.in)
# License: WTFPL

###############################################################################
# Configuration


###############################################################################
# Code

class Logger(object):
	def __init__(self):
		pass

	def __del__(self):
		self.close()

	def configure(self, configuration=None):
		# List of required configuration items
        required = ["debug", "log_filename", ]

        self.error = False
        self.error_message = {
            "log_error": None,
            }

        if configuration is None:
			# Error
			self.error = True
            self.error_message["log_error"] = "No configuration provided."

            return None

		if type(configuration) is not type({}):
			# Error
			self.error = True
            self.error_message["log_error"] = "Invalid configuration data provided."

            return None

		for i in required:
			if i not in configuration.keys():
				# Error
                self.error = True
                self.error_message["log_error"] = "Required configuration data '%s' not provided." % (i)

        if "log_format" not in configuration.keys():
            log_format = "%Y-%m-%d %H:%M:%S"
        else:
            log_format = configuration["log_format"]

		# Configure the instance
        self.debug = configuration["debug"]
        self.log = None
        self.log_filename = configuration["log_filename"]
        self.log_format = log_format

        self.open()

		return None

	def open(self):
        if self.log is not None:
            # Error
            self.error = True
            self.error_message["log_error"] = "Log file is already open."

            return None

        try:
            self.log = open(self.log_filename, 'a')
        except IOError as err:
            # Error
            self.error = True
            self.error_message["log_error"] = "Unable to open log file '%s'. %s" % (self.log_filename, err)

            return None

        return None

    def close(self):
        if self.log is None:
            return None

        try:
            self.log.close()
        except IOError as err:
            # Error
            self.error = True
            self.error_message["log_error"] = "Unable to close log file '%s'. %s" % (self.log_filename, err)

            return None

        return None

    def write(self, message=None):
        if self.message is None:
            # Error
            self.error = True
            self.error_message = "No log message provided."

            return None

        if self.log is None:
            self.open()

        if self.debug is True:
            message = "[DEBUG] %s" % (message)

        message = "[%s] %s\n" % (time.strftime(self.logformat, time.localtime()), message)

        try:
            self.log.write(message)
        except IOError as err:
            # Error
            self.error = True
            self.error_message["log_error"] = "Unable to write to log file '%s'. %s" % (self.log_filename, err)

            return None

        return None

###############################################################################
# Main

if __name__ == "__main__":
	# Add code to support single file conversion from command-line.
	pass

###############################################################################
# End

