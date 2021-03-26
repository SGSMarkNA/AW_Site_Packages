import os
import json
from glob import glob
from datetime import datetime
import logging

_Xml_Element_template_format = """<log>
    <name>%(name)s</name>
    <level_name>%(levelname)s</level_name>
    <file_path>%(pathname)s</file_path>
    <file_name>%(filename)s</file_name>
    <line_number>%(lineno)d</line_number>
    <module_name>%(module)s</module_name>
    <func_name>%(funcName)s</func_name>
    <asc_time>%(asctime)s</asc_time>
    <message>
        %(message)s
    </message>
</log>
"""
_Xml_Attribute_template_format = '\t<log name="%(name)s" level_name="%(levelname)s" file_path="%(pathname)s" file_name="%(filename)s" line_number="%(lineno)d" module_name="%(module)s" func_name="%(funcName)s" asc_time="%(asctime)s">\n\t<message>\n%(message)s\t</message>\n\t</log>'
########################################################################
class XML_Formatter(logging.Formatter):
	def __init__(self):
		logging.Formatter.__init__(self,fmt=_Xml_Attribute_template_format, datefmt="%Y-%m-%d-%H-%M-%S")

	def format(self, record):
		new_message =  ""
		old_message = record.getMessage()
		lines =  old_message.splitlines()
		for line in lines:
			new_message += "\t\t<line>%s</line>\n" % str(line)
		record.msg = new_message
		return logging.Formatter.format(self,record)
	
########################################################################
class XML_Handler(logging.FileHandler):
	#----------------------------------------------------------------------
	def __init__(self, software, filename=None, mode='a', encoding=None, delay=0):
		""""""
		if filename is None:
			user_name  = os.environ.get("USERNAME", "Unknown_User")
			today      = datetime.today()
			date       = today.date()
			date_folder= "%s_%s_%s" % ( str(date.year), str(date.month).zfill(2), str(date.day).zfill(2))
			time_sufix = "%s_%s" % ( str(today.hour), str(today.minute).zfill(2))

			if os.environ.has_key('AW_GLOBAL_LOGGING_FOLDER'):
				log_folder   = os.environ.get('AW_GLOBAL_LOGGING_FOLDER')
				log_folder   = os.path.join(log_folder,user_name, date_folder, software)

			else:
				log_folder   = os.environ.get('TEMP')
				log_folder   = os.path.join(log_folder, "XML_Logs", date_folder, software)

			if not os.path.exists(log_folder):
				os.makedirs(log_folder)
			logs = glob(log_folder+"/log_n*.xml")
			if len(logs):
				logs.sort()
				last_log =  logs[-1]
				log_number = int(os.path.basename(last_log)[5:9]) + 1
				if len(logs) >= 10:
					os.remove(logs[0])
			else:
				log_number = 0
			filename = "log_n%s_%s.xml" % (str(log_number).zfill(4), time_sufix)
			filename  = os.path.join(log_folder,filename)
			
		super(XML_Handler, self).__init__(filename, mode, encoding, delay)
		
	def post_close(self):
		data =  ""
		with file(self._basefileName, "r") as f:
			data = f.read()
		with file(self._basefileName, "w") as f:
			f.write('<?xml version="1.0" encoding="utf-8"?>\n')
			#f.write("<?xml-stylesheet type='text/xsl' href='N:\User\dloveridge\Global_Logs\Logger_Style.xsl' version='1.0'?>\n")
			f.write("<XML_LOGS>\n" + data + "</XML_LOGS>")

	def close(self):
		self._basefileName = self.baseFilename
		logging.FileHandler.close(self)
		self.post_close()

########################################################################
class XML_Logger(logging.Logger):
	""""""
	def __init__(self,name=None):
		logging.Logger.__init__(self,name)
		self.setLevel(level)


#logging.setLoggerClass(XML_Logger)

def create_Logger(name, software, level=logging.WARNING, filename=None, mode='w', encoding=None, delay=0):
	logger   = logging.getLogger(name)
	handler  = XML_Handler(software, filename, mode, encoding, delay)
	formater = XML_Formatter()
	
	logger.setLevel(level)
	handler.setFormatter(formater)
	logger.addHandler(handler)
	
	return logger
def get_Sub_Logger(name):
	logger   = logging.getLogger(name)
	return logger
#print_log(maya_logger)
#print_log(Qt_logger)

