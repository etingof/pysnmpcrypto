
Strong crypto support for PySNMP
--------------------------------
[![PyPI](https://img.shields.io/pypi/v/pysnmpcrypto.svg?maxAge=2592000)](https://pypi.org/project/pysnmpcrypto)
[![Python Versions](https://img.shields.io/pypi/pyversions/pysnmpcrypto.svg)](https://pypi.org/project/pysnmpcrypto/)
[![Build status](https://travis-ci.org/etingof/pysnmpcrypto.svg?branch=master)](https://secure.travis-ci.org/etingof/pysnmpcrypto)
[![Coverage Status](https://img.shields.io/codecov/c/github/etingof/pysnmpcrypto.svg)](https://codecov.io/github/etingof/pysnmpcrypto)
[![GitHub license](https://img.shields.io/badge/license-BSD-blue.svg)](https://raw.githubusercontent.com/etingof/pysnmpcrypto/master/LICENSE.txt)

The `pysnmpcrypto` package is an optional extension to SNMP library for
Python [pysnmp](http://snmplabs.com/pysnmp/). The `pysnmpcrypto` library
provides stronger authentication and encryption features to the SNMP library
by way of invoking stronger crypto algorithms.

The `pysnmpcrypto` library runs on Python 2.4 through 3.7 and has a dependency
on either [PyCryptodomex](https://github.com/Legrandin/pycryptodome) (for Python
versions 2.4-2.6 and 3.2-3.3) or
[Cryptography](https://github.com/pyca/cryptography) (for Python versions
2.7 and 3.4+).

The `pysnmpcrypto` package is distributed under terms and conditions of the
2-clause [BSD license](http://snmplabs.com/pysnmpcrypto/license.html).

Download & Install
------------------

The `pysnmpcrypto` package is freely available for download from
[PyPI](https://pypi.org/project/pysnmpcrypto)
and [GitHub](https://github.com/etingof/pysnmpcrypto.git).

Just run:

```bash
$ pip install pysnmp pysnmpcrypto
```
    
to download and install both `pysnmp` and `pysnmpcrypto`.

Documentation
-------------

The `pysnmpcrypto` library does not expose any user-intended API. Documentation
and usage examples on the `pysnmp` library use can be found at the
[pysnmp project site](http://snmplabs.com/pysnmp/).

If something does not work as expected with `pysnmpcrypto`, please
[open an issue](https://github.com/etingof/pysnmpcrypto/issues) at GitHub.

Copyright (c) 2018, [Ilya Etingof](mailto:etingof@gmail.com). All rights reserved.
