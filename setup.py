#!/usr/bin/env python

from distutils.core import setup

setup(
    name='django-simpleforums',
    version='1.0',
    description='A simple forums app for Django.',
    author='Sam Dornan',
    author_email='sdornan@gmail.com',
    url='https://github.com/sdornan/django-simpleforums/',
    packages=['django-autoslug', 'django-pure-pagination'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
