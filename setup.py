from setuptools import setup, find_packages

setup(
    name='django-simpleforums',
    version='1.0',
    description='A simple forums app for Django.',
    author='Sam Dornan',
    author_email='sdornan@gmail.com',
    url='https://github.com/sdornan/django-simpleforums/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires=[
        "Django >= 1.4",
        "django-autoslug >= 1.5.0",
        "django-pure-pagination >= 0.1"
    ],
)
