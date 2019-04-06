========
Overview
========

https://aws.amazon.com/transit-gateway/

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-tropo-boto-lab/badge/?style=flat
    :target: https://readthedocs.org/projects/python-tropo-boto-lab
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/natemarks/python-tropo-boto-lab.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/natemarks/python-tropo-boto-lab

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/natemarks/python-tropo-boto-lab?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/natemarks/python-tropo-boto-lab

.. |requires| image:: https://requires.io/github/natemarks/python-tropo-boto-lab/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/natemarks/python-tropo-boto-lab/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/natemarks/python-tropo-boto-lab/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/natemarks/python-tropo-boto-lab

.. |version| image:: https://img.shields.io/pypi/v/tropo-boto-lab.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/tropo-boto-lab

.. |commits-since| image:: https://img.shields.io/github/commits-since/natemarks/python-tropo-boto-lab/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/natemarks/python-tropo-boto-lab/compare/v0.0.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/tropo-boto-lab.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/tropo-boto-lab

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/tropo-boto-lab.svg
    :alt: Supported versions
    :target: https://pypi.org/project/tropo-boto-lab

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/tropo-boto-lab.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/tropo-boto-lab


.. end-badges

An example package. Generated with cookiecutter-pylibrary.

* Free software: BSD 2-Clause License

Installation
============

::

    pip install tropo-boto-lab

Documentation
=============


https://python-tropo-boto-lab.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
