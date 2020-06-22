class Config(object):
	DEBUG = False
	TESTING = False
	# DATABASE_URI = 'sqlite:///:memory:'
	# DATABASE_URI='mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='your_user', password='password', server='localhost', database='dname')
	DATABASE_URI = 'mysql://root:@127.0.0.1/test_app'
class ProductionConfig(Config):
	DATABASE_URI = 'mysql://root:@127.0.0.1/test_app'

class DevelopmentConfig(Config):
	DEBUG = True