#project/_config.py

import os


basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'A8UFS0GOQf9g2UPGIUABP92Ppaiouf49yusagf8IU)*&F&T3po&^%E&$S&%RH'


# define the full path for the db
DATABASE_PATH = os.path.join(basedir, DATABASE)

# the database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
