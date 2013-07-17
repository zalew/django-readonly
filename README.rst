Django-Readonly 
================

.. image:: https://pypip.in/v/django-readonly/badge.png
    :target: https://crate.io/packages/django-readonly/
    :alt: Latest PyPI version

.. image:: https://pypip.in/d/django-readonly/badge.png
    :target: https://crate.io/packages/django-readonly/
    :alt: Number of PyPI downloads

Put your website into read-only mode for maintanance. It blocks any POST requests and signs users out. 
It doesn't lock any database transactions (check out https://github.com/streeter/django-db-readonly for that).


* http://pypi.python.org/pypi/django-readonly/
* https://bitbucket.org/zalew/django-readonly/
* https://github.com/zalew/django-readonly/ (mirror)
 
Usage
------
 
* ``pip install django-readonly``
* settings.py: add ``'readonly.middleware.ReadOnlyMiddleware',`` to ``MIDDLEWARE_CLASSES``
* settings.py: READ_ONLY = True
* template: ``{% if request.read_only %}<p>Website is currently in read-only mode.</p>{% endif %}``
  