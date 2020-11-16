from serialization import serialize_cellmap
import os
import shutil
import numpy as np


class Logger:
	def __init__(self, session: str = 'default'):
		self.session = session
		self.id = 0
		self.count = 1


	def get_file_name(self) -> str:
		return '{0}/{1}_step.log'.format(self.session, self.count)


	def log(self, cellmap: np.ndarray):
		serialize_cellmap(cellmap, self.get_file_name())
		self.count += 1


	def start_session(self, cellmap: np.ndarray, session_name: str = ''):
		if os.path.exists(self.session):
		   shutil.rmtree(self.session)
			
		os.makedirs(self.session)

		if session_name == '':
			self.id += 1
			self.session = 'default_' + str(self.id)
		else:
			self.session = session_name

		self.count = 0
		self.log(cellmap)


	def end_session(self):
		self.session = 'default'
		self.count = 1
