from computercraft.cc_peripherals._base import BasePeripheral

__all__ = ['CreatePackagerBase']

class CreatePackagerBase(BasePeripheral):

    def getAddress(self) -> str:
        return self._call(b'getAddress').take_string()

    def getItemDetail(self, slot: int) -> dict:
        return self._call(b'getItemDetail', slot + 1).take_option_dict()

    def list(self) -> dict:
        return self._call(b'list').take_dict()

    def makePackage(self) -> bool:
        return self._call(b'makePackage').take_bool()

    def setAddress(self, address: None|str) -> None:
        return self._call(b'setAddress', address).take_none()