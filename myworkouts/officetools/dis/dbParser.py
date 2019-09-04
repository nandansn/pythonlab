import configparser

dbConfig = configparser.RawConfigParser()
dbConfig.read('db-config.properties')

def getHost():
    return dbConfig.get('Database','db.host')

def getPort():
    return dbConfig.get('Database','db.port')

def getServiceName():
    return dbConfig.get('Database','db.service_name')

def getUser():
    return dbConfig.get('Schema','schema.user')

def getPassword():
    return dbConfig.get('Schema','schema.pwd')