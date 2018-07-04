#!/usr/bin/env python
"""Strong cryptography support for PySNMP (SNMP library for Python)
"""

import sys
import os

# handle unittest discovery feature
try:
    import unittest2 as unittest
except ImportError:
    import unittest

classifiers = """\
Development Status :: 5 - Production/Stable
Environment :: Console
Intended Audience :: Developers
Intended Audience :: Education
Intended Audience :: Information Technology
Intended Audience :: System Administrators
Intended Audience :: Telecommunications Industry
License :: OSI Approved :: BSD License
Natural Language :: English
Operating System :: OS Independent
Programming Language :: Python :: 2
Programming Language :: Python :: 2.4
Programming Language :: Python :: 2.5
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.2
Programming Language :: Python :: 3.3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Topic :: Communications
Topic :: System :: Monitoring
Topic :: System :: Networking :: Monitoring
Topic :: Software Development :: Libraries :: Python Modules
"""


def howto_install_setuptools():
    print("""
   Error: You need setuptools Python package!

   It's very easy to install it, just type:

   wget https://bootstrap.pypa.io/ez_setup.py
   python ez_setup.py

   Then you could make eggs from this package.
""")


py_version = sys.version_info[:2]
if py_version < (2, 4):
    print("ERROR: this package requires Python 2.4 or later!")
    sys.exit(1)

if py_version < (2, 7) or (py_version >= (3, 0) and py_version < (3, 4)):
    requires = ['pycryptodomex']
else:
    requires = ['cryptography']

try:
    from setuptools import setup, Command

    params = {
        'install_requires': requires,
        'zip_safe': True
    }

except ImportError:
    for arg in sys.argv:
        if 'egg' in arg:
            howto_install_setuptools()
            sys.exit(1)

    from distutils.core import setup, Command

    params = {}
    if py_version > (2, 4):
        params['requires'] = requires

doclines = [x.strip() for x in (__doc__ or '').split('\n') if x]

params.update({
    'name': 'pysnmpcrypto',
    'version': open(os.path.join('pysnmpcrypto', '__init__.py')).read().split('\'')[1],
    'description': doclines[0],
    'long_description': ' '.join(doclines[1:]),
    'maintainer': 'Ilya Etingof <etingof@gmail.com>',
    'author': 'Ilya Etingof',
    'author_email': 'etingof@gmail.com',
    'url': 'https://github.com/etingof/pysnmpcrypto',
    'classifiers': [x for x in classifiers.split('\n') if x],
    'platforms': ['any'],
    'license': 'BSD',
    'packages': ['pysnmpcrypto']
})


class pytest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        suite = unittest.TestLoader().loadTestsFromNames(
            ['tests.__main__.suite']
        )

        unittest.TextTestRunner(verbosity=2).run(suite)

params['cmdclass'] = {
    'test': pytest,
    'tests': pytest,
}

setup(**params)
