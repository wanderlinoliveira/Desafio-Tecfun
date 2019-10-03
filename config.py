import os
#basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Lets-hit-a-baba'
    SQLALCHEMY_DATABASE_URI =  'mysql://sql10307145:XzD2rfk7xm@sql10.freemysqlhosting.net/sql10307145' #Fazer modificações necessárias  os.environ.get('DATABASE_URL') or
        #'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False