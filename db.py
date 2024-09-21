from mongowrapper import MongoOptions, MongoUser

from envs import DB_USER, DB_PSWD, DB_NAME

MONGO_OPTIONS = MongoOptions(DB_USER, DB_PSWD, DB_NAME)
settings = MongoUser(MONGO_OPTIONS, "settings.project").collection
