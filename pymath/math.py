import os
import ctypes

_CMATH = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "cmath", "bin", "math.dll"))
_CMATH.power.restype = ctypes.c_double
_CMATH.sine.restype = ctypes.c_double
_CMATH.cosine.restype = ctypes.c_double


def fac(n):
    return _CMATH.fac(n)

def fib(n):
    return _CMATH.fib(n)

def sqroot(x):
    ret = ctypes.c_double(x)
    _CMATH.sqroot(ctypes.byref(ret), 10)
    return ret.value

def power(x, n):
    return _CMATH.power(x, n)

def sin(x, n=5):
    return _CMATH.sine(x, n)

def cos(x, n=5):
    return _CMATH.cosine(x, n)
