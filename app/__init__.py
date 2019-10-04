from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config) #Config, database and login definitions
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models

db.create_all()

migrate = Migrate(app, db)  #Definitions for migrate database
manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()

app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')  #pyjade extension