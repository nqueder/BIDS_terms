from __future__ import absolute_import, division, print_function
import os.path

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 1
_version_minor = 0
_version_micro = '0'  # use '' for first of series, number for 1 and above
_version_extra = ''
# _version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: Apache Software License",
               "Operating System :: MacOS :: MacOS X",
               "Operating System :: POSIX :: Linux",
               "Programming Language :: Python :: 3",
               "Topic :: Scientific/Engineering"]

# Description should be a one-liner:
# TODO
description = "bids_terms_to_pdf_table: Utilty for creating Markdown table of BIDS terms and adding new BIDS terms "
# Long description will go up on the pypi page
long_description = """
bids_terms_to_pdf_table: Utilty for creating Markdown table of BIDS terms and adding new BIDS terms
License
=======
``bids_terms_to_pdf_table`` is licensed under the terms of the Apache License 2.0. See the file
"LICENSE" for information on the history of this software, terms & conditions
for usage, and a DISCLAIMER OF ALL WARRANTIES.
"""

NAME = "bids_term_to_table"
MAINTAINER = "Nazek Queder, David Keator"
MAINTAINER_EMAIL = "nqueder@uci.edu, dbkeator@uci.edu"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "https://github.com/nqueder/bids_terms_to_pdf_table"
DOWNLOAD_URL = ""
LICENSE = "Apache License 2.0"
AUTHOR = "Nazek Queder, David Keator"
AUTHOR_EMAIL = "nqueder@uci.edu, dbkeator@uci.edu"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
INSTALL_REQUIRES = ["pygithub",
                    "pandas", "pytest",
                    "pyld", "reportlab", "pdfkit","pynidm","argparse"]
SCRIPTS = ["bin/bids_term_to_table"]
