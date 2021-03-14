SQLALCHEMY_DATABASE_URI = 'sqlite:///auth.db'
STATIC_ROOT = None


try:
    from config_local import *
except ImportError:
    pass
