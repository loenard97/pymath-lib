import os
import ctypes

_CVEC3D = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "cmath", "bin", "vec3D.dll"))
_CVEC3D.len.restype = ctypes.c_double


class Vec3D(ctypes.Structure):
    _fields_ = [("a", ctypes.c_double), ("b", ctypes.c_double), ("c", ctypes.c_double)]

    def __repr__(self):
        return f"<{self.a}, {self.b}, {self.c}>"
    
    def __add__(self, vec):
        ret = self.copy()
        _CVEC3D.add(ctypes.byref(ret), ctypes.byref(vec))
        return ret

    def __sub__(self, vec):
        ret = self.copy()
        _CVEC3D.sub(ctypes.byref(ret), ctypes.byref(vec))
        return ret
    
    def __mul__(self, vec):
        ret = self.copy()
        _CVEC3D.sprod(ctypes.byref(ret), ctypes.byref(vec))
        return ret
    
    @property
    def len(self):
        return _CVEC3D.len(ctypes.byref(self))

    def copy(self):
        return Vec3D(self.a, self.b, self.c)
    
    def mul(self, factor):
        factor = ctypes.c_double(factor)
        _CVEC3D.mul(ctypes.byref(self), factor)
        return self
    
    def norm(self):
        _CVEC3D.norm(ctypes.byref(self))
        return self
    
    def sprod(self, vec):
        return self * vec

    def cprod(self, vec):
        ret = self.copy()
        _CVEC3D.cprod(ctypes.byref(ret), ctypes.byref(vec))
        return ret
