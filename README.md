
Strong crypto support for PySNMP
--------------------------------
[![PyPI](https://img.shields.io/pypi/v/pysnmpcrypto.svg?maxAge=2592000)](https://pypi.python.org/pypi/pysnmpcrypto)
[![Python Versions](https://img.shields.io/pypi/pyversions/pysnmpcrypto.svg)](https://pypi.python.org/pypi/pysnmpcrypto/)
[![Build status](https://travis-ci.org/etingof/pysnmpcrypto.svg?branch=master)](https://secure.travis-ci.org/etingof/pysnmpcrypto)
[![GitHub license](https://img.shields.io/badge/license-BSD-blue.svg)](https://raw.githubusercontent.com/etingof/pysnmpcrypto/master/LICENSE.txt)

The pysnmpcrypto package is an optional extension to the SNMP library for
Python [pysnmp](http://snmplabs.com/pysnmp/) package. Whenever one needs
strong encryption to be used for SNMP traffic authentication and ciphering,
the `pysnmpcrypto` package should be installed along with `pysnmp`.

However, `pysnmp` will work just fine without `pysnmpcrypto` for as long
as no SNMPv3 authentication/privacy protocols requiring strong crypto
algorithms are invoked.

The `pysnmpcrypto` package is distributed under terms and conditions of the
2-clause [BSD license](http://snmplabs.com/pysnmpcrypto/license.html).

Download & Install
------------------

The `pysnmpcrypto` package is freely available for download from
[PyPI](https://pypi.python.org/pypi/pysnmpcrypto)
and [GitHub](https://github.com/etingof/pysnmpcrypto.git).

Just run:

```bash
$ pip install pysnmp pysnmpcrypto
```
    
to download and install both `pysnmp` and `pysnmpcrypto`. The `pysnmpcrypto`
library is dependent on either of:

* [pyca/cryptography](http://cryptography.io/) for Python 2.7 and 3.4+
* [PyCryptodomex](https://pycryptodome.readthedocs.io) for Python 2.4-2.6 and 3.2-3.3

Documentation
-------------

The `pysnmpcrypto` library does not expose any user-intended API. Documentation
and usage examples on the `pysnmp` library can be found at the
[pysnmp project site](http://snmplabs.com/pysnmp/).

If something does not work as expected with `pysnmpcrypto`, please
[open an issue](https://github.com/etingof/pysnmpcrypto/issues) at GitHub.

Bug reports and PRs are appreciated! ;-)

Copyright (c) 2005-2018, [Ilya Etingof](mailto:etingof@gmail.com). All rights reserved.
