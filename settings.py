class Config(object):
    pass
    

#不同的环境有不同的配置

class ProductConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG=True
    #配置SQLAlchemy 的 uri
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.1.1:3306/blog'
    pass
class TestConfig(Config):
    pass
    
#开发环境,config会在app/__init__.py里使用
config = DevelopmentConfig()
