# django-simpleforums

A simple forums app for Django. I wanted to make a barebones forums app in as little code as possible.

This code was moved into this repository from a larger Django project that I created. It is only meant to be used as a code sample, and is not guaranteed to be installable without a few quirks.

## Installation
1. Install via pip from GitHub: `pip install -e git+https://github.com/sdornan/django-simpleforums.git#egg=django-simpleforums`
2. Add `forums` to INSTALLED_APPS in your project's settings.py file
3. Create the database tables: `python manage.py syncdb`
4. Add `url(r'^forums/', include('forums.urls'))` to your project's base urls.py file