from computercraft.cc_peripherals._base import BasePeripheral


__all__ = ('redstone_relay',)


class RedstoneRelayPeripheral(BasePeripheral):
    TYPE = 'redstone_relay'

    def setOutput(self, side:str, on:bool):
        return self._call(b'setOutput', side, on).take()

    def getOutput(self):
        return self._call(b'getOutput').take()

    def getInput(self):
        return self._call(b'getInput').take()

    def setAnalogOutput(self, side:str, value:int):
        return self._call(b'setAnalogOutput', side, value).take()

    def getAnalogOutput(self):
        return self._call(b'getAnalogOutput').take_int()

    def getAnalogInput(self):
        return self._call(b'getAnalogInput').take_int()
