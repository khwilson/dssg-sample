#!/usr/bin/env python
import os
from setuptools import find_packages, setup
import warnings


def parse_requirements(filename):
    """ Parse a requirements file ignoring comments and -r inclusions of other files """
    reqs = []
    with open(filename, 'r') as f:
        for line in f:
            hash_idx = line.find('#')
            if hash_idx >= 0:
                line = line[:hash_idx]
            line = line.strip()
            if line:
                reqs.append(line)
    return reqs


setup(
    name="dssg-sample",
    version="0.1.dev0",
    url="https://github.com/dssg",
    author="Awesome People",
    author_email="dssg@dssg.io",
    license="Apache v2.0",
    packages=find_packages(),
    install_requires=parse_requirements('requirements.in'),
    tests_require=parse_requirements('requirements.testing.in'),
    description="An example of a tox/travis repo"
)
