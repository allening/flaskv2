#!/usr/bin/python
from flask import Flask, g
from api.getappinfo import getappinfo as bp_getappinfo
from task.appinfo import appinfo as bp_appinfo
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

def init_db(app):
    dbEngine = create_engine(app.config['MYSQL_DATABASE_URI'])
    dbSession = sessionmaker(dbEngine)
    session = dbSession()
    return session

def create_app():
    app = Flask(__name__) 
    app.config.from_object('config.DevelopmentConfig')

    app.register_blueprint(bp_getappinfo)
    app.register_blueprint(bp_appinfo)

    @app.before_request
    def before_request():
        g.db = init_db(app)

    @app.teardown_request
    def teardown_request(exception):
        if hasattr(g,'db'):
            g.db.close()

    return app