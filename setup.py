#!/usr/bin/env python

from setuptools import setup

setup(
    name = 'bip32utils',
    version = '0.3-1',
    author = 'Johnathan Corgan, Corgan Labs',
    author_email = 'johnathan@corganlabs.com',
    maintainer = 'Pavol Rusnak, SatoshiLabs',
    maintainer_email = 'stick@satoshilabs.com',
    url = 'http://github.com/satoshilabs/bip32utils',
    description = 'Utilities for generating and using Bitcoin Hierarchical Deterministic wallets (BIP0032).',
    license = 'MIT',
    install_requires = ['ecdsa'],
    packages = ['bip32utils'],
    scripts = ['bin/bip32gen']
)
