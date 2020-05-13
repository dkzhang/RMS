import base64


def to_base64(nodes_bytearray):
    base64_str = base64.b64encode(nodes_bytearray).decode('ascii')
    return base64_str


def to_bytearray(nodes_base64):
    return base64.b64decode(nodes_base64)
