import os

#create class for setup 
class Config(object):
    # SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string" 
    # run in cmd to get random hex secret key py -c "import os; print(os.urandom(16))" 
    # copy everything form b"####" to below
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xc3\xe4\x8anI\xb5\x05\xac\xa4\xc8U\xd5\x01\xe5\x04\xe6'

    # Set up string for MONGO database
    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment'}    