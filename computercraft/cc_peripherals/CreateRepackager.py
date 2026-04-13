from computercraft.cc_peripherals._base import BasePeripheral


__all__ = ('CreateRePackagerPeripheral', )


class CreateRePackagerPeripheral(BasePeripheral):
    TYPE = 'Create_Repackager'

    def getAddress(self):
        return self._call(b'getAddress').take_string()

    # returns a dict with all strings as byte objects, might be useful to convert at least the keys somehow
    # It works though! Returns a dict with all the data about the item
    def getItemDetail(self, slot=int):
        return self._call(b'getItemDetail', slot).take()

    # Gets a list off all the items but again with bytes objects in dicts.
    def list(self):
        return self._call(b'list').take()

    # Makes a package and returns true/false if successful or not
    def makePackage(self):
        return self._call(b'makePackage').take()

    #works without issues
    def setAddress(self, address):
        return self._call(b'setAddress', address).take()