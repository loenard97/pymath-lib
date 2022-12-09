import os
import ctypes

_CCONSTANT = ctypes.CDLL(os.path.join(os.getcwd(), "lib", "constant.dll"))
_CCONSTANT.pi.restype = ctypes.c_double
_CCONSTANT.e.restype = ctypes.c_double


pi = _CCONSTANT.pi(2)
e = _CCONSTANT.e(34)
