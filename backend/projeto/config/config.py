
import os
import datetime
import secrets

BASE_DIR = os.getcwd()

class Config:
    SQLALCHEMY_DATABASE_URI =  os.environ.get('DATABASE_URL')
    #SQLALCHEMY_DATABASE_URI =  'sqlite:///database.db'
    #UPLOAD_FOLDER = 'static/imagens'
    SECRET_KEY = secrets.token_hex(32)
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=900000)



