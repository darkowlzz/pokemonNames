#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pokemonNames',
    version='0.1.0',
    description='Generate pokemon names.',
    long_description=readme + '\n\n' + history,
    author='Sunny (darkowlzz)',
    author_email='indiasuny000@gmail.com',
    url='https://github.com/darkowlzz/pokemonNames',
    packages=[
        'pokemonNames',
    ],
    package_dir={'pokemonNames':
                 'pokemonNames'},
    include_package_data=True,
    install_requires=requirements,
    license="GPL",
    zip_safe=False,
    keywords='pokemon',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
