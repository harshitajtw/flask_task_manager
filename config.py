class MasterConfig:
    SQLALCHEMY_DATABASE_URI = "sqlite:///test_master.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig:
    SQLALCHEMY_DATABASE_URI = "sqlite:///test_develop.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False