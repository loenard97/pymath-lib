import os
import ctypes
import platform


if platform.system() == "Windows":
    _CCOMPLEX = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "cmath", "bin", "complex.dll"))
elif platform.system() == "Linux":
    _CCOMPLEX = ctypes.cdll.LoadLibrary(os.path.join(os.path.dirname(__file__), "cmath", "bin", "complex.so"))
else:
    raise OSError

_CCOMPLEX.len.restype = ctypes.c_double


class Polar(ctypes.Structure):
    _fields_ = [("r", ctypes.c_double), ("theta", ctypes.c_double)]


class Complex(ctypes.Structure):
    _fields_ = [('real', ctypes.c_double), ('imag', ctypes.c_double)]

    def __repr__(self):
        return f"{self.real}+i*{self.imag}"
    
    def __abs__(self) -> float:
        return _CCOMPLEX.len(self)
    
    def __eq__(self, c1) -> bool:
        return self.real == c1.real and self.imag == c1.imag

    def __add__(self, c1):
        return _CCOMPLEX.add(self, c1)

    def __sub__(self, c1):
        return _CCOMPLEX.sub(self, c1)

    def __mul__(self, c1):
        return _CCOMPLEX.mul(self, c1)
    
    def __truediv__(self, c1):
        return _CCOMPLEX.div(self, c1)
    
    def polar(self):
        return _CCOMPLEX.to_polar(self)


_CCOMPLEX.add.restype = Complex
_CCOMPLEX.sub.restype = Complex
_CCOMPLEX.mul.restype = Complex
_CCOMPLEX.div.restype = Complex
_CCOMPLEX.to_polar.restype = Polar
