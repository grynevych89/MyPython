import json


class MysqlProvider(object):

    def __init__(self):
        path = 'config_db.json'
        with open(path, 'r') as config:
            params = json.load(config)
        self._host = params['host']
        self._user = params['user']
        self._password = params['password']
        self._database = params['database']

