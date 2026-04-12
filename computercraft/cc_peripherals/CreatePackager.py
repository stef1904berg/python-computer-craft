from computercraft.cc_peripherals._base import BasePeripheral


__all__ = ('CreatePackagerPeripheral', )


class CreatePackagerPeripheral(BasePeripheral):
    TYPE = 'Create_Packager'

    def getAddress(self):
        return self._call(b'getAddress').take_string()
