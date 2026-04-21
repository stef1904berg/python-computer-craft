from computercraft.cc_peripherals._base import BasePeripheral


__all__ = ('redstone_relay',)


class RedstoneRelayPeripheral(BasePeripheral):
    TYPE = 'redstone_relay'

    def setOutput(self, side:str, on:bool):
        return self._call(b'setOutput', side, on).take()

    def getOutput(self, side:str):
        return self._call(b'getOutput', side).take()

    def getInput(self, side:str):
        return self._call(b'getInput', side).take()

    def setAnalogOutput(self, side:str, value:int):
        return self._call(b'setAnalogOutput', side, value).take()

    def getAnalogOutput(self, side:str):
        return self._call(b'getAnalogOutput', side).take_int()

    def getAnalogInput(self, side:str):
        return self._call(b'getAnalogInput', side).take_int()
