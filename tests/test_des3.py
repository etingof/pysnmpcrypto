#
# This file is part of pysnmpcrypto software.
#
# Copyright (c) 2018, Ilya Etingof <etingof@gmail.com>
# License: http://snmplabs.com/pysnmp/license.html
#
import sys

try:
    import unittest2 as unittest

except ImportError:
    import unittest

from pysnmpcrypto import des3


class Des3CaseBase(unittest.TestCase):
    def setUp(self):
        if sys.version_info < (2, 6):
            self.plaintext = 'quick brown fox'
            self.plaintext += '!' * (16 - len(self.plaintext) % 16)
            self.ciphertext = 'XO9\xe8H\x11Try\x1b\xfe)\x07{\x8bu'
            self.key = 'testkey123456789'
            self.iv = '01234567'
        else:
            self.plaintext = b'quick brown fox'
            self.plaintext += b'!' * (16 - len(self.plaintext) % 16)
            self.ciphertext = b'XO9\xe8H\x11Try\x1b\xfe)\x07{\x8bu'
            self.key = b'testkey123456789'
            self.iv = b'01234567'

    def testEncrypt(self):
        ciphertext = des3.encrypt(self.plaintext, self.key, self.iv)
        self.assertEqual(ciphertext, self.ciphertext)

    def testDecrypt(self):
        plaintext = des3.decrypt(self.ciphertext, self.key, self.iv)
        self.assertEqual(plaintext, self.plaintext)

suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite)
