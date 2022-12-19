import os
import ctypes
import platform


if platform.system() == "Windows":
    _CCONSTANT = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "cmath", "bin", "constant.dll"))
elif platform.system() == "Linux":
    _CCONSTANT = ctypes.cdll.LoadLibrary(os.path.join(os.path.dirname(__file__), "cmath", "bin", "constant.so"))
else:
    raise OSError


_CCONSTANT.pi_alt.restype = ctypes.c_double
_CCONSTANT.e.restype = ctypes.c_double


pi = _CCONSTANT.pi_alt(2)
e = _CCONSTANT.e(34)
