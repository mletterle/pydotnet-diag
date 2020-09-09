import io
import unittest
from pydotnet_diag.nettrace import utils
from pydotnet_diag.nettrace.nettypecode import NetTypeCode

class Test_bytes_to_strings(unittest.TestCase):

    def test_null_terminated_two_byte_unicode_string(self):
        data = b'H\x00e\x00l\x00l\x00o\x00\x00\x00xxxx'
        result = utils.bytes_to_nuluni(io.BytesIO(data))
        self.assertEqual(result, 'Hello')

    def test_null_terminated_ansi_string(self):
        data = b'Hello\x00xxxx'
        result = utils.bytes_to_nulans(io.BytesIO(data))
        self.assertEqual(result, 'Hello')

class Test_read_type(unittest.TestCase):

    def test_boolean_true(self):
        data = b'\x01\x00\x00\x00'
        self.assertTrue(utils.read_type(NetTypeCode.BOOLEAN, io.BytesIO(data)))

    def test_boolean_false(self):
        data = b'\x00\x00\x00\x00'
        self.assertFalse(utils.read_type(NetTypeCode.BOOLEAN, io.BytesIO(data)))

    def test_char(self):
        data = b'\x20'
        result = utils.read_type(NetTypeCode.CHAR, io.BytesIO(data))
        self.assertEqual(result, 32)

    def test_sbyte(self):
        data = b'\xFF'
        result = utils.read_type(NetTypeCode.SBYTE, io.BytesIO(data))
        self.assertEqual(result, -1)

    def test_byte(self):
        data = b'\xFF'
        result = utils.read_type(NetTypeCode.BYTE, io.BytesIO(data))
        self.assertEqual(result, 255)

    def test_int16(self):
        data = b'\xEF\xFE'
        result = utils.read_type(NetTypeCode.INT16, io.BytesIO(data))
        self.assertEqual(result, -273)

    def test_uint16(self):
        data = b'\xE8\xFD'
        result = utils.read_type(NetTypeCode.UINT16, io.BytesIO(data))
        self.assertEqual(result, 65000)

    def test_int32(self):
        data = b'\xEF\xEF\xFE\xFE'
        result = utils.read_type(NetTypeCode.INT32, io.BytesIO(data))
        self.assertEqual(result, -16846865)

    def test_uint32(self):
        data = b'\xEF\xEF\xFE\xFE'
        result = utils.read_type(NetTypeCode.UINT32, io.BytesIO(data))
        self.assertEqual(result, 4278120431)

    def test_int64(self):
        data = b'\xEF\xEF\xFE\xFE\xEF\xEF\xFE\xFE'
        result = utils.read_type(NetTypeCode.INT64, io.BytesIO(data))
        self.assertEqual(result, -72356729937006609)

    def test_uint64(self):
        data = b'\xEF\xEF\xFE\xFE\xEF\xEF\xFE\xFE'
        result = utils.read_type(NetTypeCode.UINT64, io.BytesIO(data))
        self.assertEqual(result, 18374387343772545007)

    def test_single(self):
        data = b'\xEF\xEF\xFE\xFE'
        result = utils.read_type(NetTypeCode.SINGLE, io.BytesIO(data))
        self.assertAlmostEqual(result, -1.6943485868722686e+38)

    def test_double(self):
        data = b'\xEF\xEF\xFE\xFE\xEF\xEF\xFE\xFE'
        result = utils.read_type(NetTypeCode.DOUBLE, io.BytesIO(data))
        self.assertAlmostEqual(result, -5.3039257395059307e+303)

    def test_string(self):
        data = b'T\x00e\x00s\x00t\x00S\x00t\x00r\x00i\x00n\x00g\x00\x00\x00'
        result = utils.read_type(NetTypeCode.STRING, io.BytesIO(data))
        self.assertEqual(result, 'TestString')
