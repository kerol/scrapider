# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='scrapider',
    version='0.1.1',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = scrapider.settings']}, requires=['requests', 'scrapy']
)
