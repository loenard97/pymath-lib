import os
import ctypes

_CCOMPLEX = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "cmath", "bin", "complex.dll"))
_CCOMPLEX.len.restype = ctypes.c_double


class Complex(ctypes.Structure):
    _fields_ = [
        ('real', ctypes.c_int),
        ('imag', ctypes.c_int),
    ]

    def __repr__(self):
        return f"{self.real}+i*{self.imag}"
    
    def __add__(self, comp1):
        _CCOMPLEX.add(ctypes.byref(self), ctypes.byref(comp1))

    def __sub__(self, comp1):
        _CCOMPLEX.sub(ctypes.byref(self), ctypes.byref(comp1))

    @property
    def len(self):
        return _CCOMPLEX.len(ctypes.byref(self))
