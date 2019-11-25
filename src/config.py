import os

# class Test(object):
#     """
#     Test environment configuration
#     """
#     TESTING = True
#     JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
#     SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL')

class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

app_config = {
    # 'test': Test,
    'development': Development,
    'production': Production,
}
