#
# This file is part of pysnmpcrypto software.
#
# Copyright (c) 2018-2019, Ilya Etingof <etingof@gmail.com>
# License: http://snmplabs.com/pysnmp/license.html
#
import unittest

suite = unittest.TestLoader().loadTestsFromNames(
    ['tests.test_aes.suite',
     'tests.test_des.suite',
     'tests.test_des3.suite']
)


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite)
