import struct

class rotation:
    def __init__(self):
        return

    def ror1bit(self, val, bits_len):
        v = val >> 1
        return v

    def rol1bit(self, val, bits_len):
        v = val << 1
        v = v & ( 2**( bits_len) - 2)
        return v

    def ror(self, val, offset, bits_len):
        part_ror = val
        part_rol = val
        for i in range(offset):
            part_ror = self.ror1bit(part_ror, bits_len)
        for i in range(bits_len - offset):
            part_rol = self.rol1bit(part_rol, bits_len)

        return part_ror|part_rol
