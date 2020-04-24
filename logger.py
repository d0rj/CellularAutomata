from cell_map import CellMap
from typing import List
from serialization import serialize_cellmap


class Logger:
    def __init__(self, session: str = 'default', path: str = 'logs'):
        self.session = session
        self.path = path
        self.id = 0
        self.count = 1


    def log(self, map: List[List[int]]):
        serialize_cellmap(map, '{0}/{1}_{2}.log'.format(self.session, self.count, self.path))
        self.count += 1


    def start_session(self, map: List[List[int]], session_name: str = ''):
        if session_name == '':
            self.id += 1
            self.session = 'default_' + str(self.id)
        else:
            self.session = session_name

        self.count = 1


    def end_session(self):
        self.session = 'default'
        self.count = 1
