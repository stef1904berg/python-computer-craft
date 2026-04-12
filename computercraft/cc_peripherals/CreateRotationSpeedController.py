from computercraft.cc_peripherals._base import BasePeripheral


__all__ = ('CreateRotationSpeedController',)


class CreateRotationSpeedController(BasePeripheral):
    TYPE = 'Create_RotationSpeedController'

    def getTargetSpeed(self):
        return self._call(b'getTargetSpeed').take_int()


    def setTargetSpeed(self, speed: int):
        return self._call(b'setTargetSpeed', speed).take()
