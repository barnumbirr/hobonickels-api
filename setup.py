#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = 'hobonickels',
    version = '1.0.1',
    url = 'https://github.com/c0ding/hobonickels-api',
    download_url = 'https://github.com/c0ding/hobonickels-api/archive/master.zip',
    author = 'c0ding',
    author_email = 'me@martinsimon.me',
    license = 'Apache v2.0 License',
    packages = ['hobonickels'],
    description = 'Python API for the Hobonickels cryptocurrency.',
    long_description = file('README.md','r').read(),
    keywords = ['HBN', 'Hobonickels', 'LTC', 'Litecoin', 'BTC', 'Bitcoin', 'DOGE', 'Dogecoin', 'WDC', 'Worldcoin', 'cryptocurrency', 'API'],
)
