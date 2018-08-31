#references : parsing the property file: https://wiki.python.org/moin/ConfigParserExamples
#ref: get the directory path, https://stackoverflow.com/questions/3430372/how-to-get-full-path-of-current-files-directory-in-python
#ref: oracle connection https://stackoverflow.com/questions/3521692/how-can-i-access-oracle-from-python
#ref: my sql connection https://stackoverflow.com/questions/12072961/how-to-connect-to-mysql-database-from-python-using-connection-string


import configparser
import os
config = configparser.RawConfigParser()
config.read(os.path.dirname(os.path.abspath(__file__))+'\\test.properties')

print(os.path.dirname(os.path.abspath(__file__)))

print(os.getcwd())
print(config.get('SOURCE_DB_CONFIG','source.db.host'))