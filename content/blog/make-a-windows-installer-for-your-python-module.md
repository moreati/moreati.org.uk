---
date: 2009-03-17
title: Make a Windows installer for your python module
type: post
---

To help you build and distribute your Python packges, Python provides
[distutils](http://docs.python.org/distutils/introduction.html "distutils introduction").
This library knows how to bring together your modules, where to put
scripts and how to compile C extensions. The process is driven by a
setup.py file, written by the package author or maintainer. Depending on
what argument is passed, setup.py can install the package, build an
archive or build an installer. To create a Windows installer for a
module called wibble.py proceeed as follows. Create a setup.py file in
the same directory as your existing module(s), describing what is to be
installed:

    from distutils.core import setup
    setup(name='Wibble',
          version='1.0',
          description='A utility to deal with underpants and pencils.',
          author='Fred Bloggs',
          author_email='fbloggs@example.org',
          py_modules=['wibble'], # Add more modules as desired
          )

Run the following command:

    python setup.py bdist_wininst

This will generate wibble-1.0.win32.exe, which can install Wibble on any
Windows PC already having a version of Python. As a bonus the
bdist\_wininst command doesn't itself require Windows, so you can create
the installer on Linux or Mac OS.
