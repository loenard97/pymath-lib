import os
import ctypes

_CLIST = ctypes.CDLL(os.path.join(os.getcwd(), "lib", "list.dll"))


class ListNode(ctypes.Structure):

    def __repr__(self):
        return f"{self.value}"

ListNode._fields_ = [("value", ctypes.c_int), ("next", ctypes.POINTER(ListNode))]


class List(ctypes.Structure):
    _fields_ = [("root", ctypes.POINTER(ListNode))]

    def __init__(self, *args):
        super().__init__()
        for e in args:
            print(e)
            self.append(e)
    
    def __repr__(self):
        ret = '['
        print(self.root[0].value)
        return ''

    def append(self, value: int):
        print("append", value)
        new_node = ListNode(value)
        _CLIST.append(ctypes.byref(self), ctypes.byref(new_node))
