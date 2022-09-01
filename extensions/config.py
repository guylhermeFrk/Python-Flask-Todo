class Config:
    SECRET_KEY = '123456790'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class LocalConfig(Config):
    AMBIENTE = 'Local'
    DEBUG = True
    PORT = 5000
    SQLALCHEMY_DATABASE_URI = 'sqlite:///todo.db'