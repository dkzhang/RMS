from unittest import TestCase

from myUtils.node_encode.base64_bytearray import to_base64
from myUtils.node_encode.base64_intarray import intarray_to_base64str, base64str_to_intarray


class Test(TestCase):
    def test_select_nodes(self):
        test_array = list(range(30)) + [0, 1, 200, 239]
        # test_array = range(128)
        base64_str = intarray_to_base64str(test_array)
        print(base64_str)
        print(len(base64_str))
        print("###########################################")
        intarray = base64str_to_intarray(base64_str)
        print(intarray)

        self.assertEqual(1, 1)
