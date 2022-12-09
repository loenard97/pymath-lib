import os
import ctypes

_CFRACTION = ctypes.CDLL(os.path.join(os.getcwd(), "lib", "fraction.dll"))


class Fraction(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c_int),
    ]

    def __repr__(self):
        return f"{self.a}/{self.b}"
    
    def __mul__(self, frac1):
        _CFRACTION.mul(ctypes.byref(self), ctypes.byref(frac1))
