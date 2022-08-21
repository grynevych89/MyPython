from models.group import Group
import pickle


class BinaryProvider(object):

    def __init__(self):
        self._group = Group()

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, group: Group):
        self._group = group

    def save_data(self):
        with open('student.dat', 'wb') as f:
            pickle.dump(self._group, f)
        print('Save-OK')

    def load_data(self):
        with open('student.dat', 'rb') as f:
            self._group = pickle.load(f)
        print('Load-OK')
