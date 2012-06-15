#!/usr/bin/env python

try:
    from setuptools import setup

except:
    from distutils.core import setup

setup(
    name = "parikstra",
    description = "Parisian transport system API client",
    
    py_modules = ["parikstra"],
    test_suite = "tests",

    install_requires = [
        "beautifulsoup4",
        "requests",
    ],

    version = "0.1",
    author = "Gawen ARAB",
    author_email = "g@wenarab.com",
    url = "https://github.com/Gawen/parikstra",
    license = "MIT",
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Utilities",
    ],
)
