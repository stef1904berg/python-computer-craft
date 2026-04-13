from computercraft.cc_peripherals._base import BasePeripheral


__all__ = ('CreateRePackagerPeripheral', )


class CreateRePackagerPeripheral(BasePeripheral):
    TYPE = 'Create_Repackager'

    def getAddress(self):
        return self._call(b'getAddress').take_string()

    def getItemDetail(self, slot=int):
        return self._call(b'getItemDetail', slot).take_dict()

    def list(self):
        return self._call(b'list').take_dict()

    def makePackage(self):
        return self._call(b'makePackage').take_bool()

    def setAddress(self, address):
        return self._call(b'setAddress', address).take()