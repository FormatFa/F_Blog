from flask import Flask
from settings import config
import logging
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

file_handler = logging.FileHandler('日志.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def create_app():
    logger.debug('create app:%s',__name__)
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    #导入各个模块
    from app.posts.views import blue_posts
    #from app.posts.models import User
    app.register_blueprint(blue_posts,url_prefix='/')
    return app



