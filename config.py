import os

#create class for setup 
class Config(object):
    SECRET_KeY = os.environ.get('SECRET_KEY') or "secret_string" 

    # Set up string for MONGO database
    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment'}    