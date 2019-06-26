import configparser


class Config:

    __config = None

    def __init__(self, env):
        if Config.__config is None:
            Config.__config = configparser.ConfigParser()
            Config.__config.read(['config.default.ini', 'config.dev.ini'])

    @staticmethod
    def get(section, key):
        if Config.__config is not None:
            return Config.__config.get(section, key)
        else:
            raise Exception('Config was not initialized.')
