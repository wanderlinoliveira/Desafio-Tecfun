import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Lets-hit-a-baba'
    
    #Database Config
    SQLALCHEMY_DATABASE_URI =  'mysql://sql10307145:XzD2rfk7xm@sql10.freemysqlhosting.net/sql10307145'
    SQLALCHEMY_TRACK_MODIFICATIONS = False