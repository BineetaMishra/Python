from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db_config = config['database']
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username=db_config['username'],
    password=db_config['password'],
    hostname=db_config['hostname'],
    databasename=db_config['databasename'],
)
app = Flask(__name__, template_folder="template")
app.config['SECRET_KEY'] = 'eccc71bfaced73cfc01951c5745a93c5'
app.config['SQLALCHEMY_DATABASE_URI']= SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
db = SQLAlchemy(app)
db.app = app
bcrypt = Bcrypt(app)

from firstflask import route