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

from pysnmpcrypto import aes


class AesCaseBase(unittest.TestCase):
    def setUp(self):
        if sys.version_info < (2, 6):
            self.plaintext = 'quick brown fox'
            self.ciphertext = '\x19g*A\xad\x84\xb8c\xe4\xfa\x95J\xd1\xbe\xc1'
            self.key = 'testkey123456789'
            self.iv = '0123456789012345'
        else:
            self.plaintext = b'quick brown fox'
            self.ciphertext = b'\x19g*A\xad\x84\xb8c\xe4\xfa\x95J\xd1\xbe\xc1'
            self.key = b'testkey123456789'
            self.iv = b'0123456789012345'

    def testEncrypt(self):
        ciphertext = aes.encrypt(self.plaintext, self.key, self.iv)
        self.assertEqual(ciphertext, self.ciphertext)

    def testDecrypt(self):
        plaintext = aes.decrypt(self.ciphertext, self.key, self.iv)
        self.assertEqual(plaintext, self.plaintext)

suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite)
