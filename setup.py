#!/usr/bin/env python
"""Strong cryptography support for PySNMP (SNMP library for Python)

The pysnmpcrypto package is an optional extension to SNMP library
for Python -- pysnmp 5.0+. The pysnmpcrypto library provides
stronger authentication and encryption features to the SNMP
library by way of invoking stronger crypto algorithms.

The pysnmpcrypto library runs on Python 2.6 through 3.7 and has a
dependency on either PyCryptodomex (for Python versions 2.6
and 3.2-3.3) or Cryptography (for Python versions 2.7 and 3.4+).
"""

import sys
import os
import re

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
if py_version < (2, 6):
    print("ERROR: this package requires Python 2.6 or later!")
    sys.exit(1)

requires = [ln.strip() for ln in open('requirements.txt').readlines()]

resolved_requires = []

# NOTE(etingof): older setuptools fail at parsing python_version
for requirement in requires:
    match = re.match(
        r'(.*?)\s*;\s*python_version\s*([<>=!~]+)\s*\'(.*?)\'', requirement)

    if not match:
        resolved_requires.append(requirement)
        continue

    package, condition, expected_py = match.groups()

    expected_py = tuple([int(x) for x in expected_py.split('.')])

    if py_version == expected_py and condition in ('<=', '==', '>='):
        resolved_requires.append(package)

    elif py_version < expected_py and condition in ('<=', '<'):
        resolved_requires.append(package)

    elif py_version > expected_py and condition in ('>=', '>'):
        resolved_requires.append(package)

try:
    import setuptools

    setup, Command = setuptools.setup, setuptools.Command

    observed_version = [int(x) for x in setuptools.__version__.split('.')]
    required_version = [36, 2, 0]

    # NOTE(etingof): require fresh setuptools to build proper wheels
    # See also: https://hynek.me/articles/conditional-python-dependencies/
    if ('bdist_wheel' in sys.argv and
            observed_version < required_version):
        print("ERROR: your wheels won't come out round with setuptools %s! "
              "Upgrade to %s and try again." % (
                '.'.join([str(x) for x in observed_version]),
                '.'.join([str(x) for x in required_version])))
        sys.exit(1)

    if observed_version < required_version:
        requires = resolved_requires

    params = {
        'install_requires': requires,
        'zip_safe': True
    }

except ImportError:
    if 'bdist_wheel' in sys.argv or 'bdist_egg' in sys.argv:
        howto_install_setuptools()
        sys.exit(1)

    from distutils.core import setup, Command

    params = {'requires': [
        re.sub(r'(.*?)([<>=!~]+)(.*)', r'\g<1>\g<2>(\g<3>)', r)
        for r in resolved_requires]
    }

doclines = [x.strip() for x in (__doc__ or '').split('\n')]

params.update({
    'name': 'pysnmpcrypto',
    'version': open(os.path.join('pysnmpcrypto', '__init__.py')).read().split('\'')[1],
    'description': doclines[0],
    'long_description': '\n'.join(doclines[1:]),
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
