#!/usr/bin/env python3
from setuptools import setup

setup(
    name="mpdrandom",
    packages=["mpdrandom"],
    version="1.0.0",
    description="mpd albums randomizing script",
    author="IbeeX",
    author_email="",
    url="",
    install_requires=["python-mpd2"],
    keywords=["mpd", "album", "random", "shuffle", "music"],
    license="License :: OSI Approved :: GNU General Public License (GPL)",
    classifiers=["Programming Language :: Python", "Development Status :: 4 - Beta"],
    python_requires=">=3.5",
    long_description="""\
mpdrandom
---------
A script that adds the missing randomness to mpds albums

Features
* Queue albums randomly from the library
""",
    entry_points="""
        [console_scripts]
        mpdrandom=mpdrandom.mpdrandom:cli
    """,
)
