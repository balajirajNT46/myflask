class Config(object):
	DEBUG = False
	TESTING = False


class ProductionConfig(Config):
	API_URL = 'http://localhost:5000'

class DevelopmentConfig(Config):
	DEBUG = True