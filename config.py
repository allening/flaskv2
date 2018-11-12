
class Config(object):
    MYSQL_DATABASE_URI = 'mysql+mysqlconnector://root:123456@127.0.0.1:3307/appinst?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    TEST = 'test string!!!'

class TestingConfig(Config):
    TESTING = True
