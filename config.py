class Config:
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    SECRET_KEY = "dev"