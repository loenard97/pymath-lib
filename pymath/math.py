import os
import ctypes

_CMATH = ctypes.CDLL(os.path.join(os.getcwd(), "lib", "math.dll"))


def fac(n):
    return _CMATH.fac(n)

def fib(n):
    return _CMATH.fib(n)

def sqroot(x):
    ret = ctypes.c_double(x)
    _CMATH.sqroot(ctypes.byref(ret), 10)
    return ret.value
