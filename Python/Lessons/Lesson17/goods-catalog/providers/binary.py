from models.catalog import Catalog
import pickle


class BinaryProvider(object):

    def __init__(self):
        self._catalog = Catalog()

    @property
    def catalog(self):
        return self._catalog

    @catalog.setter
    def catalog(self, catalog: Catalog):
        self._catalog = catalog

    def save_data(self):
        with open('goods.dat', 'wb') as f:
            pickle.dump(self._catalog, f)
        print('Save-OK')

    def load_data(self):
        with open('goods.dat', 'rb') as f:
            # pickle.dump(self._catalog, f)
            self._catalog = pickle.load(f)
        print('Load-OK')
