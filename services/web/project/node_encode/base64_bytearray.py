import base64

def to_base64(nodes_bytearray):
    Base64Str = base64.b64encode(nodes_bytearray).decode('ascii')
    return Base64Str

def to_bytearray(nodes_base64):
    return base64.b64decode(nodes_base64)

