import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRETY_KEY = os.environ.get('SECRETY_KEY') or 'hard to guess string'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	MAIL_SERVER = 'smtp.qq.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = '1021644861@qq.com'
	MAIL_PASSWORD = 'xujitao1014'
	FLASKY_MAIL_SUBJECT_PREFIX = '[FLASKY]'
	FLASKY_MAIL_SENDER = 'FLASKY Admin<1021644861@qq.com>'
	FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
		'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or \
		'sqlite:///' + os.path.join(basedir,'data-test.sqlite')

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
	'development' : DevelopmentConfig,
	'testing' : TestingConfig,
	'production' : ProductionConfig,

	'default' : DevelopmentConfig
}