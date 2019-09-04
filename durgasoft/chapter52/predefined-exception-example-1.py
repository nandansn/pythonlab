import logging as log

class AgeInvalidException(Exception):
    def __init__(self,message):
        self.msg = message
        

log.basicConfig(filename="log.txt")
age = int(input('Enter Your Age: '))
log.info("Age is {}".format(age))
try:
    if age < 1 or age > 99 :
        raise AgeInvalidException("Age is invalid") # message we are passing it the value to the message variable in the constructor
    else:
        log.info('Age is {}'.format(age))
        print("your age is {} valid.".format(age))
        
except AgeInvalidException as msg:
    log.log(40,'Age is {}, this is invalid'.format(age))
    log.log(50,'Age is {}, this is invalid'.format(age))
