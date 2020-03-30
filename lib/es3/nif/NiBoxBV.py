from __future__ import annotations

from es3.utils.math import compose, decompose, ID33, ZERO3
from .NiBoundingVolume import NiBoundingVolume


class NiBoxBV(NiBoundingVolume):
    center: NiPoint3 = ZERO3
    rotation: NiMatrix3 = ID33
    extents: NiPoint3 = ZERO3

    bound_type = NiBoundingVolume.BoundType.BOX_BV

    def load(self, stream):
        super().load(stream)
        self.center = stream.read_floats(3)
        self.rotation = stream.read_floats(3, 3)
        self.extents = stream.read_floats(3)

    def save(self, stream):
        super().save(stream)
        stream.write_floats(self.center)
        stream.write_floats(self.rotation)
        stream.write_floats(self.extents)

    def apply_scale(self, scale):
        self.center *= scale
        self.extents *= scale

    @property
    def matrix(self):
        return compose(self.center, self.rotation, self.extents)

    @matrix.setter
    def matrix(self, value):
        self.center, self.rotation, self.extents = decompose(value)


if __name__ == "__main__":
    from es3.utils.typing import *
