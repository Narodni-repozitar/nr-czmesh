# -*- coding: utf-8 -*-


"""oarepo OAI-PMH converter."""
import os

from setuptools import find_packages, setup

tests_require = [
    'pytest'
]

extras_require = {
    "tests": tests_require
}

setup_requires = [
    'pytest-runner>=2.7',
]

install_requires = [
    'pymarc',
    'click'
]

with open("README.md", "r") as f:
    long_description = f.read()

packages = find_packages()

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('nr_czmesh', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='nr-czmesh',
    version=version,
    description=__doc__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    author='Daniel Kopecký',
    author_email='Daniel.Kopecky@techlib.cz',
    url='',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        "console_scripts": [
            "czmesh = nr_czmesh.cli:czmesh"
        ]
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
)
