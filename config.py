class Config(object):
    DEBUG = True
    SECRET_HERE = 'Y'
    SQLALCHEMY_DATABASE_URI = "sqlite:///movies.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False