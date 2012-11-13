#!/usr/bin/env python
# encoding: utf-8
import os
from setuptools import setup, find_packages
from readonly import VERSION, DEV_STATUS

setup(
    name='django-readonly',
    version='.'.join(map(str, VERSION)),
    description='Put website in read-only mode for maintenance.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    keywords='django readonly',
    author='Jakub Zalewski',
    author_email='zalew7@gmail.com',
    url='https://bitbucket.org/zalew/django-readonly',
    license='public domain',
    packages=find_packages(),
    zip_safe=False,
    package_data={
        'readonly': [],
    },
    classifiers=[
        'Development Status :: %s' % DEV_STATUS,
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
      install_requires=[
        'django',
    ],
)
