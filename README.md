# django-simpleforums

A simple forums app for Django. I wanted to make a barebones forums app in as little code as possible.

This code was moved into this repository from a larger Django project that I created, and thus the templates were built with that project in mind. It is not guaranteed to be installable as a reusable app at this time.

## Installation
1. Install via pip from GitHub: `pip install -e git+https://github.com/sdornan/django-simpleforums.git#egg=django-simpleforums`
2. Add `forums` to INSTALLED_APPS in your project's settings.py file
3. Create the database tables: `python manage.py syncdb`
4. Add `url(r'^forums/', include('forums.urls'))` to your project's base urls.py file

## Settings
There are a few settings that you can set. These each have sane defaults that will be used if you choose not to set them.
* FORUMS_CACHE_LENGTH - how long to cache the last post values that are displayed per forum/thread. (Default: 24 hours)
* FORUMS_EDITABLE_LENGTH - how long after posting can a user edit their post. (Default: 5 minutes)

## TODOs
* Make the user avatar locations a definable setting instead of hardcoding them in the templates. Right now, the templates expect the user avatars to be an ImageField called 'avatar' on the UserProfile.
* The templates were built with [Bootstrap](https://github.com/twitter/bootstrap) in mind. Not sure if I should include some minimal CSS directly in the app, or if it should be left up to the user.