from decouple import config


class Config:
    SECRET_KEY = config("SECRET_KEY")


class DevelopmentConfig(config):
    DEBUG = True


config = {"development": DevelopmentConfig}
