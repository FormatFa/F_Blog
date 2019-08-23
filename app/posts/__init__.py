from flask import Blueprint
import logging
blue_posts = Blueprint('posts',__name__)
logger = logging.getLogger('app.posts')

logger.debug('posts init...')
from . import views
