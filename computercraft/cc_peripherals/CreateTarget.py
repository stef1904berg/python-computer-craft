from computercraft.cc_peripherals._base import BasePeripheral


__all__ = ('CreateTarget',)


class CreateTarget(BasePeripheral):
    TYPE = 'create_target'

    def resize(self, width:int, height:int):
        return self._call(b'resize', width, height).take()

    def getLine(self, line:int):
        return self._call(b'getLine', line).take_string()

    def dump(self):
        return self._call(b'dump').take_dict()

    def getSize(self):
        return self._call(b'getSize').take()